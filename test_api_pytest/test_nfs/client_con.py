import os
import pytest
from conftest import ssh_run_cmd

client_ip = '172.26.172.9'
server_ip = '172.26.172.12'

mount_path = os.popen('showmount -e %s | sed -n 2p | cut -d \' \' -f1 ' % server_ip).read().strip()
# @pytest.mark.nfs_client()
# def test_clent_nfs():
#     mount_cmd = 'sshpass -p 111111 ssh root@%s -o StrictHostKeyChecking=no \'mount -t nfs -o vers=3 %s:%s /pytest \'' % (client_ip,server_ip,mount_path)
# #    mount_cmd = 'sshpass -p 111111 ssh root@172.26.172.9 -o StrictHostKeyChecking=no \'mount -t nfs -o vers=3 172.26.172.13:/testvol/ganeshag /pytest \' '
#     res = os.system(mount_cmd)
#     echo_mount = os.system('sshpass -p 111111 ssh root@%s -o StrictHostKeyChecking=no \'echo 1 > /pytest/1 \'' % (client_ip))
#     umount_client = os.system('sshpass -p 111111 ssh root@%s -o StrictHostKeyChecking=no \'umount -l /pytest \'' % (client_ip))
#     assert res == 0
#     assert echo_mount == 0
#     assert umount_client == 0
if mount_path != 0:
    @pytest.mark.nfs_client()
    def test_client_nfs():
        res, a, b = ssh_run_cmd(client_ip, "mount -t nfs -o vers=3 %s:%s /pytest " % (server_ip, mount_path))
        echo_mount = ssh_run_cmd(client_ip, "echo 1 > /pytest/1")
        umount_cmd = ssh_run_cmd(client_ip, "umount -l /pytest")
        print(a, echo_mount, umount_cmd)
        assert res == 0
        assert echo_mount[0]  == 0
        assert umount_cmd[0]  == 0
