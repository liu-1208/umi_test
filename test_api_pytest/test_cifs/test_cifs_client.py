import pytest
import test_cifs
from conftest import ssh_run_cmd

client_ip = '172.26.172.9'
server_ip = '172.26.172.12'


mount_path = str(test_cifs.share_dir).strip()


@pytest.mark.cifs_client()
def test_client_nfs():
    res, a, b = ssh_run_cmd(client_ip, "mount -t cifs -o username=1,password=1 //%s%s /pytest " % (server_ip, mount_path))
    print(res, a, b, mount_path)
    echo_mount = ssh_run_cmd(client_ip, "echo cifs_share > /pytest/cifs_share_test")
    umount_cmd = ssh_run_cmd(client_ip, "umount -l /pytest")
    assert res == 0
    assert echo_mount[0] == 0
    assert umount_cmd[0] == 0

#username = pytest00
# @pytest.mark.cifs_client()
# def test_clent_nfs():
#     res, a, b = ssh_run_cmd(client_ip, "mount -t cifs -o username=%s //%s:%s /pytest " % (username, server_ip, mount_path))
#     print(res, a, b)
#     echo_mount = ssh_run_cmd(client_ip, "echo 1 > /pytest/1")
#     umount_cmd = ssh_run_cmd(client_ip, "umount -l /pytest")
#     assert res == 0
#     assert echo_mount[0] != 0
#     assert umount_cmd[0] == 0