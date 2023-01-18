#!/bin/bash

if [ -d "/opt/XDFS-UMI" ];then
    source /opt/XDFS-UMI/.venv/bin/activate
    pip install pytest allure-pytest pytest-ordering  pytest-dependency pytest-html httprunner pytest-rerunfailures
else
    pip install pytest allure-pytest pytest-ordering  pytest-dependency  paramiko pytest-html pytest-rerunfailures
fi
rpm -qa | grep sshpas  || yum -y install sshpass
#pip list  | grep -E "allure-pytest|pytest-ordering|pytest-rerunfailures|pytest-dependency|paramiko|pytest-html|pytest-rerunfailures" | wc -l

master_ip=`cat test_api_pytest/conftest.py | grep BASEURL | awk -F: 'NR==1{print $2}'| cut -c 3-16`
master_passwd=111111

#thr_num=$(sshpass -p ${master_passwd} ssh root@${master_ip} -o StrictHostKeyChecking=no 'ps -aux | grep main | grep -v grep | wc -l')
thr_num=$(sshpass -p ${master_passwd} ssh root@${master_ip} -o StrictHostKeyChecking=no 'systemctl  | grep xdfs | wc -l')
datelog=$(date +%Y%m%d)
a=$(sshpass -p ${master_passwd} ssh root@${master_ip} -o StrictHostKeyChecking=no 'lsblk  -P  | grep -w disk | wc -l')
brick_num=$((a - 1))
path=./test_api_pytest
#filepath=./test_api_pytest/conftest.py
#volname=test1 


function somck_com()
{
    pytest -vs --alluredir=../update_results  --html=../report.html  ./test_storage/test_block.py \
test_cluster/test_cluster_service.py  \
test_user/test_local_user.py  \
test_volume/test_vol_create.py \
test_nfs/test_gluster.py \
test_nfs/test_client_con.py \
test_nfs/test_kernel.py  \
test_nfs/test_client_con.py \
test_nfs/test_ganesha_gluster.py \
test_nfs/test_client_con.py \
test_iscsi/test_t*  \
test_cifs/test_cifs.py \
test_cifs/test_cifs_client.py \
test_minio/test_minio.py \
test_ftp/test_ftp.py
    pytest -vs --alluredir=../delete_results -m delete .
}

#sed -i "s/^volname.*/volname = \'${volname}\'/1" ${filepath}
cd ${path}
if [[ ${thr_num} -eq 2 ]] && [[ ${brick_num} -gt 1 ]];then
    somck_com  
    else
    echo "Check whether the number of disks is greater than two !"
fi

cd ..
dir=`pwd`
#dirname=`pwd | awk -F\/ '{print $(NF-1)}'`
dirname=`pwd | awk -F\/ '{print $NF}'`
tar zcf ${datelog}-${dirname}.tar.gz ${dir} > /dev/null
[ -d /var/log/allure ] || mkdir /var/log/allure  2>&1
mv ${datelog}-${dirname}.tar.gz /var/log/allure/ 


