import os
import pytest
from conftest import ssh_run_cmd, BASEURL
import json
import requests

client_ip = '172.26.172.9'
server_ip = '172.26.172.12'

num, mount_path, err = ssh_run_cmd(client_ip, 'showmount -e %s | sed -n 2p | cut -d \' \' -f1 ' % server_ip)

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
#
if mount_path != "":
    mount_path = str(mount_path).strip()
    @pytest.mark.nfs_client
    @pytest.mark.dependency(name="client_nfs_test")
    def test_client_nfs():
        res, a, b = ssh_run_cmd(client_ip, "mount -t nfs -o vers=3 %s:%s /pytest " % (server_ip, mount_path))
        print(res,a,b)
        if res == 0:
            echo_mount = ssh_run_cmd(client_ip, "echo nfstest > /pytest/nfstest")
            print(a, mount_path)
        assert res == 0, '挂载失败：{0}'.format(b)
        assert echo_mount[0] == 0

    if "gan" not in mount_path:
        @pytest.mark.nfs_service()
        def test_gluster_nfs_client_status():
            url = BASEURL + '/cluster/nfs/client/status'
            rdata = {
                "req_host": "127.0.0.1"
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))
            data = result.json()['data']
            c = data['127.0.0.1']
            assert c != []
            print(json.dumps(result.json(), indent=4))
    else:
        @pytest.mark.nfs_service
        def test_ganesha_client_status():
            url = BASEURL + '/cluster/ganesha/client/status'
            rdata = {
                "req_host": "127.0.0.1"
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            data = result.json()['data']
            # for i in data:
            #     # print(i)
            #     print(i['data'])
            #     a = i['data']
            assert data != []
            print(json.dumps(result.json(), indent=4))

    @pytest.mark.nfs_client
    @pytest.mark.dependency(depends=["client_nfs_test"])
    def test_client_nfs_umount():
        umount_cmd = ssh_run_cmd(client_ip, "umount -l /pytest")
        print(umount_cmd)
        assert umount_cmd[0] == 0
else:
    print("请确认共享是否存在！")
