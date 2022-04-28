# _*_ coding: utf-8 _*_
import pandas as pd
import xlwt
import yaml

from umi_node.restapi import (
    storage_physic_disk_apis,
    storage_logic_disk_apis,
    storage_lvm_apis,
    storage_file_system_apis,
    network_nic_apis,
    network_dns_apis,
    network_ntp_apis,
    users_user_apis,
    users_ad_user_apis,
    users_ldap_user_apis,
    gluster_glusterd_apis,
    gluster_peer_apis,
    gluster_volume_apis,
    gluster_monitor_performance_apis,
    gluster_brick_apis,
    gluster_auth_apis,
    gluster_thread_apis,
    gluster_cache_apis,
    gluster_heal_apis,
    gluster_rebalance_apis,
    gluster_snap_apis,
    gluster_tier_apis,
    gluster_shard_apis,
    gluster_trash_apis,
    gluster_read_only_apis,
    gluster_bitrot_apis,
    gluster_quota_apis,
    gluster_halo_apis,
    minio_gateway_apis,
    share_nfs_apis,
    share_cifs_apis,
    share_iscsi_tgt_apis,
    share_iscsi_tcmu_apis,
    share_ftp_apis,
    ctdb_apis
)

MODULES = [
    storage_physic_disk_apis,
    storage_logic_disk_apis,
    storage_lvm_apis,
    storage_file_system_apis,
    network_nic_apis,
    network_dns_apis,
    network_ntp_apis,
    users_user_apis,
    users_ad_user_apis,
    users_ldap_user_apis,
    gluster_glusterd_apis,
    gluster_peer_apis,
    gluster_volume_apis,
    gluster_monitor_performance_apis,
    gluster_brick_apis,
    gluster_auth_apis,
    gluster_thread_apis,
    gluster_cache_apis,
    gluster_heal_apis,
    gluster_rebalance_apis,
    gluster_snap_apis,
    gluster_tier_apis,
    gluster_shard_apis,
    gluster_trash_apis,
    gluster_read_only_apis,
    gluster_bitrot_apis,
    gluster_quota_apis,
    gluster_halo_apis,
    minio_gateway_apis,
    share_nfs_apis,
    share_cifs_apis,
    share_iscsi_tgt_apis,
    share_iscsi_tcmu_apis,
    share_ftp_apis,
    ctdb_apis
]


def get_interface_desc(doc):
    func_descrip_mark = ":Descrip"
    for key, value in yaml.safe_load(doc).items():
        if key == func_descrip_mark:
            desc_str = value
    return desc_str


def create_sheet(
        uml_summary,
        module_name
):
    sheet = uml_summary.add_sheet(module_name)
    sheet.col(0).width = 256 * 35
    sheet.col(1).width = 256 * 30
    sheet.col(2).width = 256 * 135
    sheet.col(3).width = 256 * 15
    sheet.col(4).width = 256 * 50
    sheet.write(0, 0, "接口名")
    sheet.write(0, 1, "接口路径")
    sheet.write(0, 2, "接口描述")
    sheet.write(0, 3, "是否成功(Y/N/~)")
    sheet.write(0, 4, "错误描述")
    return sheet


def write_sheet(
        sheet,
        mark,
        interface_name,
        interface_path,
        interface_desc,
        interface_result,
        interface_error
):
    sheet.write(mark, 0, interface_name)
    sheet.write(mark, 1, interface_path)
    sheet.write(mark, 2, interface_desc)
    sheet.write(mark, 3, interface_result)
    sheet.write(mark, 4, interface_error)


def xls_to_csv_pd(cumstom_file):
    data_xls = pd.read_excel(f"{cumstom_file}.xls", index_col=0)
    data_xls.to_csv(f"{cumstom_file}.csv", encoding="utf_8_sig")


if __name__ == '__main__':

    # 修改这里，自定义文件名
    cumstom_file = "umi_node_test_summary"
    uml_summary = xlwt.Workbook(encoding="utf-8")
    total_mark = 1
    summary_sheet = create_sheet(uml_summary, module_name="summary")

    for module in MODULES:
        single_sheet = create_sheet(uml_summary, module.DEFAULT_TAGS[0])
        mark = 1
        for method in module.METHODS:
            interface_name = method.get("name")
            interface_path = method.get("path")
            interface_desc = get_interface_desc(method.get("func").__doc__)
            interface_status = "Y"
            interface_error = "~"

            write_sheet(
                single_sheet,
                mark,
                str(interface_name),
                str(interface_path),
                str(interface_desc),
                str(interface_status),
                str(interface_error)
            )

            write_sheet(
                summary_sheet,
                total_mark,
                str(interface_name),
                str(interface_path),
                str(interface_desc),
                str(interface_status),
                str(interface_error)
            )
            mark = mark + 1
            total_mark = total_mark + 1

    uml_summary.save(f"{cumstom_file}.xls")
    # csv文件只保存活动工作簿，当前只保存summary
    xls_to_csv_pd(cumstom_file)

