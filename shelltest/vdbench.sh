#!/bin/bash
#date: 2022-10-27
#author: Mr.liu
#The host_list variable must be secret-free
#node_password=111111
#sh_path=./output.sh

set -x
vol_list=('vol-01' 'vol-02' 'vol-03' 'ec-01' 'ec-02' )
vdb_file=('vol1_file' 'vol2_file' 'vol3_file' 'ec1_file' 'ec2_file')
share_ip=10.10.10.81
host_list=('node81' 'node82' 'node83')

function vdb_posix_test(){
    local agree=posix
    local mount="        sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no \"mount -t glusterfs ${share_ip}:${s} \/mnt\/${s}\""
#    sed -i  "s/^share_ip.*/share_ip=127.0.0.1/1" $sh_path
    echo "------POSIX_RUNING------"
    [ -d Posix ] || mkdir Posix
    #sed -i  "s/^agree.*/agree=posix/1" $sh_path
    #sed -i '19s#.*#        sshpass -p 111111 ssh root@node${i}  -o StrictHostKeyChecking=no \"mount -t glusterfs ${share_ip}:${s} \/mnt\/${s}\"#1' $sh_path
    Bf_vdb_test "$agree" "$mount"  > POSIX_A.log
#    sh $sh_path > POSIX_A.log
    mv ./POSIX* ./Posix/
    mv ./posix* ./Posix/
    mv ./Posix* ./Posix/
    echo "------complete------" 
}
function vdb_knfsv3_test(){
    local agree=knfsv3
    local mount="        sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=3 ${share_ip}:\/export\/${s}\/knfs \/mnt\/${s}\""
    echo "------KNFSV3_RUNING------"
    for i in ${vol_list[@]} ;do
    {
       gluster v set ${i} nfs.disable on
       mkdir /export/${i}/knfs ; chmod 777  /export/${i}/knfs
       mkdir /export/${i}/gnfs ; chmod 777  /export/${i}/gnfs
       rm -rf /export/${i}/vdb* no*
       rm -rf /export/${i}/knfs/*
       rm -rf /export/${i}/gnfs/*
    }&
    done
    wait
    # for i in ${vol_list[@]};do
    #    gluster v set ${i} nfs.disable on
    #    mkdir /export/${i}/knfs && chmod 777  /export/${i}/knfs
    #    mkdir /export/${i}/gnfs && chmod 777  /export/${i}/gnfs
    #    rm -rf /export/${i}/vdb* no*
    # done
    for i in ${host_list[@]};
    do
      ssh ${i} umount -l /mnt/*
      ssh ${i} umount -l /mnt/*
      ssh ${i} systemctl restart nfs
    done
    [ -d KNFSV3 ] || mkdir -p KNFSV3
#    sed -i  "s/^agree.*/agree=knfsv3/1" $sh_path
#    sed -i '19s#.*#        sshpass -p 111111 ssh root@node${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=3 ${share_ip}:\/export\/${s}\/knfs \/mnt\/${s}\"#1' $sh_path
#    sh $sh_path > Knfsv3_A.log
    Bf_vdb_test "$agree" "$mount" > Knfsv3_A.log
    mv ./Knfsv3* ./KNFSV3/
    mv ./knfsv3* ./KNFSV3/
    echo "------complete------" 
}

function vdb_knfsv4_test(){
    local agree=knfsv4
    local mount="        sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=4 ${share_ip}:\/export\/${s}\/knfs \/mnt\/${s}\""
    echo "------KNFSV4_RUNING------"
    for i in ${host_list[@]};
    do
      ssh ${i} umount -l /mnt/*
    done
    for i in ${vol_list[@]};do
       rm -rf /export/${i}/knfs/*
    done
    [ -d KNFSV4 ] || mkdir -p KNFSV4
#    sed -i  "s/^agree.*/agree=knfsv4/1" $sh_path
#    sed -i '19s#.*#        sshpass -p 111111 ssh root@node${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=4 ${share_ip}:\/export\/${s}\/knfs \/mnt\/${s}\"#1' $sh_path
#    sh $sh_path > Knfsv4_A.log
    Bf_vdb_test "$agree" "$mount" > knfsv4_A.log
    mv ./Knfsv4* ./KNFSV4/
    mv ./knfsv4* ./KNFSV4/
    echo "------complete------" 
}

function vdb_gnfs_test(){
    local agree=gnfs
    local com="        sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=3 ${share_ip}:\/${s}\/gnfs \/mnt\/${s}\""
    echo "------GNFS_RUNING------"
    for i in  ${host_list[@]};do
      ssh ${i} umount -l /mnt/*
      ssh ${i} systemctl stop nfs
    done
    for i in ${vol_list[@]};do
       gluster v set ${i} nfs.disable off
       rm -rf /export/${i}/knfs/*
    done
    
    [ -d GNFS ] || mkdir -p GNFS
#    sed -i  "s/^agree.*/agree=gnfs/1" $sh_path
#    sed -i '19s#.*#        sshpass -p 111111 ssh root@node${i}  -o StrictHostKeyChecking=no \"mount -t nfs -o vers=3 ${share_ip}:\/${s}\/gnfs \/mnt\/${s}\"#1' $sh_path
#    sh $sh_path > Gnfs_A.log
    Bf_vdb_test "$agree" "$mount" > Gnfs_A.log
    mv ./Gnfs* ./GNFS/
    mv ./gnfs* ./GNFS/
    echo "------complete------" 
}


#set -x
#share_ip=10.10.10.81
#agree=knfsv3
#vdb_file=('vol1_file' 'vol2_file' 'vol3_file' 'ec1_file' 'ec2_file')
##vdb_file=(lsl_test lsl_test1)
#vol_list=('vol-01' 'vol-02' 'vol-03' 'ec-01' 'ec-02')

function Bf_vdb_test(){
#  local local_dir
#  local_dir=/mnt/posix_share
#  rm -rf ${local_dir}/*
  local agree=$1
  local com=$2
  echo '------server_mount_Posix------'
  for i in  ${host_list[@]}
  do
      for s in ${vol_list[@]}
      do
        ssh ${i} [ -d /mnt/${s} ] || mkdir /mnt/${s}
        ${com}
#        sshpass -p 111111 ssh root@${i}  -o StrictHostKeyChecking=no "mount -t nfs -o vers=3 ${share_ip}:/export/${s}/knfs /mnt/${s}"
        rm -rf /mnt/${s}/vdb* no_dismount.txt
      done
  done
  [ $? -eq 0 ] && echo "mount_succeed:" `mount | grep mnt` || echo '------mount_error------'
  echo '------mount_end------'
  echo "------vdbench_test_start------"
  cd /root/vdbench
  for i in ${vdb_file[@]};
  do
    {
    ./vdbench -f ${i}  > ${agree}_${i}.log
    }&
  done
  wait
  for i in ${vol_list[@]};do
    echo '------${i}_heal_info------'
    gluster v heal ${i} info >> ${agree}_heal_info
    gluster v heal ${i} info summary >> ${agree}_heal_info
    echo ${i}_file_num: `tree /mnt/${i} | tail -1` >> ${agree}_heal_info
  done
  echo "------vdbench_end------"
#  [ -d ./Posix ] || mkdir -p ./Posix
#  mv ${agree}*.log ./Posix/
#  cp -rp ./output ./Posix/
#  for a in ${vol_list[@]};do
#  cp -rp ./output ./posix/${a}
#  done
}

vdb_posix_test
vdb_knfsv3_test
vdb_knfsv4_test
vdb_gnfs_test
