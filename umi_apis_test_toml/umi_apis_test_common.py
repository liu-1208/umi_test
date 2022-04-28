# _*_ coding: utf-8 _*_
import json

import requests
import toml
from loguru import logger as umi_cluster_test_log


def interface_post_request(request_url, request_data):
    post_ret = requests.post(
        request_url,
        json=request_data
    )
    post_ret_json = json.dumps(post_ret.json(), sort_keys=True, indent=4, separators=(",", ":"))
    return post_ret_json


def all_files_run(file_list, node_path):

    for file_name in file_list:
        module_content = toml.load(file_name + f".toml")
        umi_cluster_test_log.info("------------")
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
                    post_ret_json = interface_post_request(
                        request_url=request_url,
                        request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                    )
                    print(f"接口请求响应{i}:")
                    print(post_ret_json)
                    print("\n")


# @umi_cluster_test_log.catch
def single_file_run(file_name, node_path):
    print(file_name+f".toml")
    module_content = toml.load(file_name + f".toml")
    print("------------")
    umi_cluster_test_log.info("------------")
    print(module_content["module"])
    umi_cluster_test_log.info(module_content["module"])
    print("------------")
    umi_cluster_test_log.info("------------")
    for interface_name in module_content.get("interface_names"):
        print("接口名:\n" + str(interface_name).replace("_", " ") + "\n")
        umi_cluster_test_log.info("接口名:" + str(interface_name).replace("_", " "))
        print("接口描述:\n" + module_content.get(interface_name)["interface_desc"] + "\n")
        umi_cluster_test_log.info("接口描述:" + module_content.get(interface_name)["interface_desc"])
        interface_path = module_content.get(interface_name)["interface_path"]
        request_url = f"{node_path}{interface_path}"
        requests_data_time = module_content.get(interface_name)["requests_data_time"]
        for i in range(1, requests_data_time + 1):

            if f"requests_data_{i}" in module_content.get(interface_name):
                print(f"接口请求数据{i}:")
                umi_cluster_test_log.info(f"接口请求数据{i}:")
                print(module_content.get(interface_name)[f"requests_data_{i}"])
                umi_cluster_test_log.info(module_content.get(interface_name)[f"requests_data_{i}"])
                post_ret_json = interface_post_request(
                    request_url=request_url,
                    request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                )
                print(f"接口请求响应{i}:")
                umi_cluster_test_log.info(f"接口请求响应{i}:")
                print(post_ret_json)
                umi_cluster_test_log.info(post_ret_json)
                print("\n")
                umi_cluster_test_log.info("\n")


def single_interface_run(file_name, interface_name, node_path):

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
                post_ret_json = interface_post_request(
                    request_url=request_url,
                    request_data=module_content.get(interface_name)[f"requests_data_{i}"]
                )
                print(f"接口请求响应{i}:")
                print(post_ret_json)
                print("\n")



