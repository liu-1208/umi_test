import csv
import os
import sys
import sh
import time

import paramiko
import requests
from httprunner import __version__

file_path = os.path.realpath(__file__)

BASE_CONFIG_FILE = "base.conf"

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


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


def read_csv(file_path=''):
    # switch  csv file to list of dict
    conf_list = []
    key_list = []
    n = 0
    with open(file_path) as f:
        r = csv.reader(f)
        for line in r:
            d = {}
            if n == 0:
                key_list = line
                n += 1
                continue

            v = 0
            for k in key_list:
                d[k] = line[v]
                v += 1
            conf_list.append(d)
            n += 1
    return conf_list


def get_node_url():
    node_url = read_base_conf().get("node_url", "")
    return node_url


def get_cluster_url():
    cluster_url = read_base_conf().get("cluster_url", "")
    return cluster_url


def pytest_volume_clean(vol_name=''):
    node_url = get_node_url()
    url_list_volume = node_url + "/gluster/volume/list"
    url_stop_volume = node_url + "/gluster/volume/stop"
    url_delete_volume = node_url + "/gluster/volume/delete"

    r = requests.post(url=url_list_volume, json={})
    if r.status_code == 200 and vol_name in r.json()["data"]:
        json = {"vol_name": vol_name}
        requests.post(url=url_stop_volume, json=json)
        requests.post(url=url_delete_volume, json=json)
    return None


def get_value_from_dict(dic_str={}, key=None):
    return dic_str.get(key, '')


def get_host_once(host=''):
    f_dir = os.path.dirname(file_path)
    f_path = 'umi_node/data/storage.csv'
    path = os.path.join(f_dir, f_path)

    v = read_csv(file_path=path)[0]['host01']
    return v


def get_uuid_with_uuid_mark(uuid_mark=''):
    uuid = read_base_conf().get(uuid_mark, "")
    return uuid


def switch_nfs_opts(opt1, opt2):
    new_opts = []
    if opt1.strip() != "":
        new_opts.append(opt1.strip())
    if opt2.strip() != "":
        new_opts.append(opt2.strip())
    return new_opts


def get_value_by_mode(mode="replica", value_mode="replica"):
    if mode == "disperse-data":
        v = {"arbiter": "0", "replica": "0", "disperse_data": "2", "redundancy": "1"}
    elif mode == "arbiter":
        v = {"arbiter": "1", "replica": "3", "disperse_data": "0", "redundancy": "0"}
    else:
        v = {"arbiter": "0", "replica": "3", "disperse_data": "0", "redundancy": "0"}
    return v.get(value_mode)


def convert_for_idempotence(src=''):

    filestr = ''
    stepstr = ''
    start_new_step = False

    skip_idemp_api = [
        'testcase',
        '/file_system/mount',
        '/network/connection/down',
        '/gluster/brick/add',
        '/gluster/brick/add',
        '/gluster/brick/remove/start',
        '/gluster/brick/remove/stop',
        '/gluster/brick/remove/force',
        '/gluster/brick/remove/commit',
        '/gluster/brick/replace/commit',
        '/gluster/volume/rebalance/stop',
        '/gluster/volume/reset/brick/commit',
        '/gluster/volume/delete',
        '/gluster/peer/detach'
    ]

    skip_idemp = lambda x: [s in x for s in skip_idemp_api]

    with open(src) as f:
        fstr = f.read()

    for line in fstr.split('\n'):
        if line.startswith('-'):
            if stepstr != '':
                if True not in skip_idemp(stepstr):
                    filestr += stepstr

                stepstr = ''
            start_new_step = True

        if line.strip().startswith('#') is False and start_new_step:
            stepstr += line + '\n'

        filestr += line + '\n'
    
    if stepstr != '' and True not in skip_idemp(stepstr):
        filestr += stepstr
    
    with open(src, 'w') as f:
        f.write(filestr)


def run_convert_idemp():
    if os.path.exists('umi_node_origin') is False:
        sh.cp(['-r', 'umi_node', 'umi_node_origin'])
    else:
        sh.rm(['-f','-r', 'umi_node'])
        sh.cp(['-r', 'umi_node_origin', 'umi_node'])
    
    for root, dirs, files in os.walk('umi_node'):
        for f in files:
            fpath = os.path.join(root, f)
            if fpath.endswith('summary.yml'):
                continue
            if fpath.endswith('.yml'):
                convert_for_idempotence(src=fpath)


def create_test_dir():
    iplist = []
    iplist = read_base_conf().get("ip_list", "").split(",")

    for ip in iplist:
        cmd = ""
        mount_dir = "/tmp/pytest_xdfs"
        bind_dir = "/tmp/pytest_xdfs_bind"
        copy_test_file = "/var/lib/glusterd/pytestfile"

        cmd += f"test -e {mount_dir} || mkdir -p {mount_dir};"
        cmd += f"test -e {bind_dir} || mkdir -p {bind_dir};"
        cmd += f"touch {copy_test_file};"

        for u_mark in ["uuid_01", "uuid_02", "uuid_03", "uuid_04", "uuid_05", "uuid_06"]:
            uuid = get_uuid_with_uuid_mark(u_mark)
            uuid_path = f"/data/{uuid}"
            cmd += f"test -e {uuid_path} || mkdir -p {uuid_path};"

        print(f"Create test directories in node {ip}")
        exit_code, stdout_str, stderr_str = ssh_run_cmd(hostname=ip, cmd=cmd)
        if exit_code != 0:
            print(stderr_str)


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'idempotence':
        run_convert_idemp()
    else:
        create_test_dir()
