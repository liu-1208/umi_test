# _*_ coding: utf-8 _*_

# https://testerhome.com/topics/20466

import requests
import toml

NODE_IP = "172.18.123.73"
NODE_PORT = "8001"
node_path = f"http://{NODE_IP}:{NODE_PORT}"


file_list = [
    "node_physic_disk",
    "node_logic_disk",
    "node_file_system",
    "node_nic",
    "node_dns",
    "node_time",
    "node_local_user",
    "node_gluster",
    "node_nfs",
    "node_cifs",
    "node_iscsi"
]


def interface_post_request(request_url, request_data):
    post_ret = requests.post(
        request_url,
        json=request_data
    )
    return post_ret


def all_files_run(file_list):

    for file_name in file_list:
        module_content = toml.load(file_name + f".toml")
        print("------------")
        print(module_content["module"])
        print("------------")
        for interface_name in module_content.get("interface_names"):
            print("接口名:\n" + str(interface_name).replace("_", " ") + "\n")
            print("接口描述:\n" + module_content.get(interface_name)["interface_desc"] + "\n")
            interface_path = module_content.get(interface_name)["interface_path"]
            request_url = f"{node_path}{interface_path}"
            requests_data_time = module_content.get(interface_name)["requests_data_time"]
            for i in range(1, requests_data_time + 1):

                if f"requests_data_{i}" in module_content.get(interface_name):
                    print(f"接口请求数据{i}:")
                    print(module_content.get(interface_name)[f"requests_data_{i}"])
                    post_ret = interface_post_request(
                        request_url=request_url,
                        request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                    )
                    print(f"接口请求响应{i}:")
                    print(post_ret.text)
                    print("\n")


def single_file_run(file_name):

    module_content = toml.load(file_name + f".toml")
    print("------------")
    print(module_content["module"])
    print("------------")
    for interface_name in module_content.get("interface_names"):
        print("接口名:\n" + str(interface_name).replace("_", " ") + "\n")
        print("接口描述:\n" + module_content.get(interface_name)["interface_desc"] + "\n")
        interface_path = module_content.get(interface_name)["interface_path"]
        request_url = f"{node_path}{interface_path}"
        requests_data_time = module_content.get(interface_name)["requests_data_time"]
        for i in range(1, requests_data_time + 1):

            if f"requests_data_{i}" in module_content.get(interface_name):
                print(f"接口请求数据{i}:")
                print(module_content.get(interface_name)[f"requests_data_{i}"])
                post_ret = interface_post_request(
                    request_url=request_url,
                    request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                )
                print(f"接口请求响应{i}:")
                print(post_ret.text)
                print("\n")


def single_interface_run(file_name, interface_name):

    module_content = toml.load(file_name + f".toml")
    print("------------")
    print(module_content["module"])
    print("------------")
    if interface_name in module_content.get("interface_names"):
        print("接口名:\n" + str(interface_name).replace("_", " ") + "\n")
        print("接口描述:\n" + module_content.get(interface_name)["interface_desc"] + "\n")
        interface_path = module_content.get(interface_name)["interface_path"]
        request_url = f"{node_path}{interface_path}"
        requests_data_time = module_content.get(interface_name)["requests_data_time"]
        for i in range(1, requests_data_time + 1):

            if f"requests_data_{i}" in module_content.get(interface_name):
                print(f"接口请求数据{i}:")
                print(module_content.get(interface_name)[f"requests_data_{i}"])
                post_ret = interface_post_request(
                    request_url=request_url,
                    request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                )
                print(f"接口请求响应{i}:")
                print(post_ret.text)
                print("\n")


def glusterfs_env_init():
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Stop")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Delete")


def glusterfs_env_info():
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_List")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Info")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Cfg_List")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Status")


def create_single_replica_volume():
    glusterfs_env_init()
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Create_Single_Replica")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Start")
    glusterfs_env_info()


def create_three_replica_volume():
    glusterfs_env_init()
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Create_Three_Replica")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Start")
    # glusterfs_env_info()
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Add")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Replace_Commit")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Remove_Force")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Option_Get")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Option_Reset")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Option_Set")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Group_List")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Group_Set")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Rebalance_Start")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Rebalance_Status")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Rebalance_Stop")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Reset")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Heal_Enable")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Heal_Info")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Heal_Disable")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Sync")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_System_Copy")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Add")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Remove_Start")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Remove_Stop")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Remove_Status")
    # single_interface_run(file_name="node_gluster", interface_name="Gluster_Brick_Remove_Commit")


def create_arbiter_volume():
    glusterfs_env_init()
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Create_Arbiter")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Start")
    glusterfs_env_info()


def create_ec_volume():
    glusterfs_env_init()
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Create_EC")
    single_interface_run(file_name="node_gluster", interface_name="Gluster_Volume_Start")
    glusterfs_env_info()


if __name__ == '__main__':


    single_file_run(file_name="node_local_user")
    # single_file_run(file_name="node_physic_disk")
    # single_file_run(file_name="node_logic_disk")
    # single_file_run(file_name="node_file_system")
    # single_file_run(file_name="node_nic")
    # single_file_run(file_name="node_time")
    # single_file_run(file_name="node_dns")
    # single_file_run(file_name="node_gluster")
    # single_file_run(file_name="node_nfs")
    # single_file_run(file_name="node_cifs")
    # single_file_run(file_name="node_iscsi")

    # create_single_replica_volume()
    # create_three_replica_volume()
    # create_arbiter_volume()
    # create_ec_volume()



