import paramiko
import os
import sys
import json
import requests
# import logging


volname = 'pytestvol'
lvmvol = 'pytestlvm'
# 需要测试的url链接，如下是cluster_api接口测试
BASEURL = 'http://172.26.172.12:8000'
# 集群名称和集群ip
cluster_host_list = ['node12', 'node13', 'node14']
cluster_ip = ['172.26.172.12', '172.26.172.13', '172.26.172.14']
# 初始化为lvm卷磁盘路径
lvm_brick_names = ["/dev/sdc"]
# 初始化为xfs系统磁盘路径
dev_path = "/dev/sdb"
uuid = "12345678-1234-1234-1234-12345678a010"


file_path = os.path.realpath(__file__)
BASE_CONFIG_FILE = "base.conf"
lst = __file__.split('/')
base_path = '/'.join(lst[:-1])
# base_path = "/opt/XDFS-UMI/MyPytest"
sys.path.append(base_path)


def read_base_conf():
    f_dir = os.path.dirname(file_path)
    f_path = BASE_CONFIG_FILE
    path = os.path.join(f_dir, f_path)

    with open(path, "r") as f:
        f_list = f.read().split("\n")

    conf_dict = {}
    for s in f_list:
        if s.strip() == "" or s.strip().startswith("#"):
            continue
        k = s.strip().split("=")[0]
        v = s.strip().split("=")[1]
        conf_dict[k] = v
    return conf_dict


def ssh_run_cmd(hostname="", cmd=":"):
    conf_dict = read_base_conf()
    username = conf_dict.get("username", "")
    port = conf_dict.get("port", "")
    passwd = conf_dict.get("passwd", "")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=passwd)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout_str = stdout.read().decode("utf-8")
    stderr_str = stderr.read().decode("utf-8")
    exit_code = stdout.channel.recv_exit_status()

    ssh.close()
    return exit_code, stdout_str, stderr_str

# def test_ganesha_nfs_list():
#     url = BASEURL + '/cluster/nfs/share/list'
#     rdata = {
#         "req_host": "127.0.0.1",
#         "nfs_mode": "Ganesha"
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     a = result.json()["data"]
#     if len(a) != 0:
#         nfs_path = a[0]['path']
#     # for i in a:
#     #     nfs_path = i['path']
#     #     return nfs_path
#     # print(json.dumps(result.json(), indent=4))
#     return nfs_path


class Basetest(object):
    def __init__(self, uri, rdata):
        self.BASEURL = BASEURL
        self.uri = uri
        self.rdata = rdata

    def base_test(self):
        url = self.BASEURL + self.uri
        jsonstr = json.dumps(self.rdata)
        result = requests.post(url, jsonstr)
        print(result)
        status_code = result.status_code
        # reouput = json.dumps(result.json(), indent=4)
        return status_code, result

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# logger = logging.getLogger('test_umi')
# logger.setLevel(logging.DEBUG)
# #sh = logging.StreamHandler()
# #sh.setLevel(logging.DEBUG)
# fh = logging.FileHandler('api.log', mode='a', encoding='utf-8')
# fh.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# fh.setFormatter(formatter)
# #sh.setFormatter(formatter)
# #logger.addHandler(sh)
# logger.addHandler(fh)
#
# if __name__ == "__main__":
#     logger.debug('----调试信息 [debug]------')
#     logger.info('[info]')
#     logger.warning('警告信息[warning]')
#     logger.error('错误信息[error]')
#     logger.critical('严重错误信息[crtical]')

# if __name__ == "__main__":
#     rdata = {
#         "req_host": "127.0.0.1",
#         "dev_names": [
#             "/dev/sde"
#         ]
#     }
#     base = Basetest("/node/gsnap/thin_lvm/enable", rdata)
#     a, c = base.base_test()
