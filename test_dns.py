# Run in python3.6
# test_dns.py
import pytest
from network.dns import (
    get_hostname_static_table,
    add_hostname_static_table_entry,
    del_hostname_static_table_entry,
    get_nsswitch_config,
    update_nsswitch_config
)

@pytest.mark.dependency()
def test_get_hostname_static_table():
    '''
    Get Hostname Static Table
    '''
    try:
        hosts_list = get_hostname_static_table()
        assert isinstance( hosts_list, list )
        for h in hosts_list:
            print(h)
    except Exception as e:
        assert False, e

@pytest.mark.dependency(depends=['test_get_hostname_static_table'])
def test_add_hostname_static_table_entry():
    '''
    Add Hostname Static Table Entry
    '''
    add_hosts_list = [
        {
            "ip_address": "172.26.172.12",
            "hostnames": [
                "node12"
            ]
        },
        {
            "ip_address": "172.26.172.13",
            "hostnames": [
                "node13"
            ]
        }
    ]

    try:
        add_hostname_static_table_entry( add_hosts_list )
        hosts_list = get_hostname_static_table()
        for h in add_hosts_list:
            assert h in hosts_list

    except Exception as e:
        assert False, e


@pytest.mark.dependency(depends=['test_add_hostname_static_table_entry'])
def test_del_hostname_static_table_entry():
    '''
    Del Hostname Static Table Entry
    '''
    del_hosts_ip_list = [ 
        "11.11.11.11"
    ]

    try:
        del_hostname_static_table_entry( del_hosts_ip_list )

        hosts_list = get_hostname_static_table()
        hosts_ip_list = [ h['ip_address'] for h in hosts_list ]
        for ip in del_hosts_ip_list:
            assert ip not in hosts_ip_list

        for i in hosts_list:
            print(i)
    except Exception as e:
        assert False, e

@pytest.mark.dependency()
def test_get_nsswitch_config():
    '''
    Get Nsswitch Config
    '''
    try:
        cfg_dict = get_nsswitch_config()
        assert isinstance(cfg_dict, dict)
        print(cfg_dict)
    except Exception as e:
        assert False, e

@pytest.mark.dependency(depends=['test_get_nsswitch_config'])
def test_update_nsswitch_config():
    '''
    Update Nsswitch Config
    '''
    hosts = "files dns"
    new_cfg_dict = { "hosts": "files dns" }
    try:
        update_nsswitch_config( new_cfg_dict )
        cfg_dict = get_nsswitch_config()
        assert cfg_dict['hosts'] == hosts
        print(cfg_dict)
    except Exception as e:
        assert False, e
