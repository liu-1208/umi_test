# _*_ coding: utf-8 _*_
import os
from loguru import logger as umi_cluster_test_log
from umi_test.umi_apis_test_toml.umi_apis_test_common import single_file_run


NODE_IP = "172.18.123.73"
NODE_PORT = "8000"
node_path = f"http://{NODE_IP}:{NODE_PORT}"


init_files_path_list = [

    # # 网络组件
    # "/Network/cluster_network",
    #
    # # 硬盘设备组件
    # "/Storage/StorageInit",
    # # "/Storage/LVMInit",
    #
    # # 用户组件
    # "/User/cluster_user_add",

    # 卷组件
    "/Volume/ReplicaVolumeStart",
    "/Volume/ReplicaArbiterVolumeStart",
    # "/Volume/ReplicaArbiterVolumeStart2",
    # "/Volume/ECVolumeStart2",
    # "/Volume/ECVolumeStart",

    # # Posix组件
    # "/Posix/PosixInit",
    #
    # # NFS组件
    # # "/NFS/KnfsInit",
    # "/NFS/GnfsInit",
    #
    # # CIFS组件
    # "/CIFS/CIFSInit",
    #
    # # FTP组件
    # "/FTP/SmbftpdInit",
    #
    # # # iSCSI组件
    # # "/iSCSI/iSCSIInit",
    #
    # # minio组件
    # "/Minio/MinioInit",

    # Peer组件
    "/Cluster/ClusterInit"

]

uninit_files_path_list = [

    # minio组件
    # "/Minio/MinioUninit",

    # # # iSCSI组件
    # # "/iSCSI/iSCSIUninit",
    #
    # # FTP组件
    # "/FTP/SmbftpdUninit",
    #
    # # CIFS组件
    # "/CIFS/CIFSUninit",
    #
    # # NFS组件
    # # "/NFS/KnfsUninit",
    # "/NFS/GnfsUninit",
    #
    # # Posix组件
    # "/Posix/PosixUninit",
    #
    # 卷组件
    "/Volume/VolumeStop",
    "/Volume/VolumeStop2",
    # "/Volume/VolumeStop3",
    #
    # # 用户组件
    # "/User/cluster_user_del",
    #
    # # 硬盘设备组件
    # "/Storage/StorageUninit",
    # # "/Storage/LVMUninit",

    # Peer组件
    "/Cluster/ClusterUninit"

]


def cluster_test_log():

    # 清空文件
    open("/tmp/umi_cluster_test.log", 'w').close()

    # 日志不输出到console控制台
    umi_cluster_test_log.remove(handler_id=None)
    umi_cluster_test_log.add("/tmp/umi_cluster_test.log", format="{time}|{level}|{message}", level="INFO")

    return


def init_interface():

    for file_path in init_files_path_list:
        file_name = current_path + file_path
        single_file_run(file_name=file_name, node_path=node_path)

    return


def uninit_interface():

    for file_path in uninit_files_path_list:
        file_name = current_path + file_path
        single_file_run(file_name=file_name, node_path=node_path)

    return


if __name__ == '__main__':

    # 获取当前路径
    current_path = os.getcwd()

    # 日志
    cluster_test_log()

    # 初始化
    # init_interface()

    # 去初始化
    uninit_interface()




