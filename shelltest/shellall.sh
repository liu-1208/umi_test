#!/bin/bash


# 并发清理所有卷对应磁盘数据
function Bf_Clean_Brick(){
  local com=$(gluster v info | grep Brick[0-9] | awk -F: '{print $2, $3}')
  local server=$(gluster v info | grep Brick[0-9] | awk -F: '{print $2}' | sort |  uniq  -d)
#  local brick_path=$(gluster v info | grep Brick[0-9] | awk -F: '{print $3}' )
  for i in ${server[@]};do
    for a in ${brick_path[@]};do
    {
      sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no "rm -rf  ${a}/*"
    }&
  done
done
wait
}

# 清理系统日志及其gluster日志信息（包含新旧时间戳）
function Gluster_Log_Clean(){
    local log_out=/root/logs
    local logdate=$(date +%Y%m%d)
    local vol_all=`gluster v list`
    local vol_list=(${vol_all//,/ })

    [ -d ${log_out} ] || mkdir -p ${log_out}
    #messages log
    cd /var/log/
    cp messages messages-${logdate}
    > messages
    #mv `find /var/log/ -maxdepth 1 -type f  -name "*-*" ` $log_out
    find ./ -maxdepth 1 -type f  -name "*-*" -exec mv {} ${log_out} \;
    cp ./glusterfs/glusterd.log  ./glusterfs/glusterd-${logdate}.log
    > ./glusterfs/glusterd.log
    
    ########
    for i in ${vol_list[@]};do
      {
      cp ./glusterfs/export-${i}.log export-${i}.log-${logdate}
      [ $? -eq 0 ] && > ./glusterfs/export-${i}.log
      }&
    done
    wait
    
    find ./glusterfs -maxdepth 1 -type f  -name "*-*.gz" -exec mv {} ${log_out} \;
    find ./glusterfs -type f  -name "*202[2|3]*" -exec mv {} ${log_out} \;
    
    ###
    cd /tmp/
    cp umi_node.log umi_node-${logdate}.log
    cp umi_cluster.log umi_cluster-${logdate}.log
    > umi_node.log
    > umi_cluster.log
    find . -maxdepth 1 -type f  -name "*-*.log"
#cd ${log_out}
#find ./ -atime +60 |xargs rm -f 
}

function Sys_Network_Disable(){
    systemctl stop firewalld
    systemctl disable firewalld
    
    setenforce 0
    sed -i 's#SELINUX=enforcing#SELINUX=disabled#g'/etc/selinux/config
    
    systemctl stop NetworkManager
    systemctl disable NetworkManager
}


function Sys_brick_clean(){
    local host_list=('node81' 'node82' 'node83')
    local vol_name=('testvol')
    local uuid=12345678-1234-1234-1234-12345678901b
    local dev_name=('/dev/sdb' '/dev/sdc')
    for i in ${vol_name[@]};do
      gluster v reset $i all
    done

    for i in ${host_list[@]};do
      for s in ${dev_name[@]};do
        ssh $i umount $uuid
        ssh $i wipefs --all $s
        ssh $i mkfs.xfs -L DataDisk -i size=2k -n size=64k -d su=128k,sw=4 $s -f
        ssh $i xfs_admin -L DataDisk -U $uuid $s
      done
    done
}
