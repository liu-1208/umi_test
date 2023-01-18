import pytest
from conftest import ssh_run_cmd

client_ip = '172.26.172.9'
server_ip = '172.26.172.13'

mount_path = '/ftp_share'
if mount_path != "":
    @pytest.mark.ftp_client()
    def test_client_ftp():
        ssh_run_cmd(client_ip, "mkdir %s"  %mount_path )
        ssh_run_cmd(client_ip,"yum -y install curlftpfs")
        res, a, b = ssh_run_cmd(client_ip, "curlftpfs -o codepage=utf8 ftp://pytest-01:111111@%s/%s  %s" % ( server_ip, mount_path,mount_path)) # 挂载rw 用户
        echo_mount = ssh_run_cmd(client_ip, "echo 1 > %s/1" %mount_path)
        umount_cmd = ssh_run_cmd(client_ip, "umount -l %s" %mount_path)
        assert res == 0
        assert echo_mount[0] == 0
        assert umount_cmd[0] == 0


