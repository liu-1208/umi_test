import json
import requests
import pytest
from conftest import BASEURL, volname

rdata = {
    "req_host": "127.0.0.1"
}
sub_dir = "/minio"
user1 = "minio1"
configname = "config01"
adminuser = "admin"
adminpasswd = "12345678"
password = "11111111"


@pytest.mark.minio
class Test_gateway_service(object):
    def test_gateway_service_init(self):
        url = BASEURL + '/cluster/minio/gateway/service/init'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.dependency()
    def test_gateway_config_update(self):
        url = BASEURL + '/cluster/minio/gateway/config/update'
        rdata = {
            "req_host": "127.0.0.1",
            "config": configname,
            "minio_admin_user": adminuser,
            "minio_admin_password": adminpasswd,
            "api_port": 9000,
            "console_port": 19000,
            "vol_name": volname,
            "sub_dir": sub_dir
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.dependency(depends=["Test_gateway_service::test_gateway_config_update"])
    def test_gateway_service_enable(self):
        url = BASEURL + '/cluster/minio/gateway/service/enable'
        rdata = {
            "req_host": "127.0.0.1",
            "config_list": [
                configname
            ]
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    # @pytest.mark.minio
    # @pytest.mark.dependency(depends=["test_gateway_service_enable"])
    # def test_gateway_service_disable(self=None):
    #     url = BASEURL + '/cluster/minio/gateway/service/disable'
    #     rdata = {
    #         "req_host": "127.0.0.1",
    #         "config_list": [
    #             configname
    #         ]
    #     }
    #     jsonstr = json.dumps(rdata)
    #     result = requests.post(url, jsonstr)
    #     assert result.status_code == 200
    #     print(json.dumps(result.json(), indent=4))

    @pytest.mark.minio
    def test_gateway_service_status(self):
        url = BASEURL + '/cluster/minio/gateway/service/status'
        rdata = {
            "req_host": "127.0.0.1",
            "config_list": [
                configname
            ]
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        #    print(json.dumps(result.json(), indent=4))
        assert result.status_code == 200
        a = result.json()["data"]
        for i in a:
            minio = i['status']
            return minio
        assert str(minio) == "True"


@pytest.mark.minio
def test_gateway_config_list():
    url = BASEURL + '/cluster/minio/gateway/config/list'
    rdata = {
      "req_host": "127.0.0.1",
      "config_list": [
        configname
      ]
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()["data"]
    assert a != []

# @pytest.mark.minio
# def test_gateway_bucket_update():
#     url = BASEURL + '/cluster/minio/gateway/bucket/update'
#     rdata = {
#       "req_host": "127.0.0.1",
#       "config": configname,
#       "bucket": "bucket01",
#       "policy": "none"
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))


@pytest.mark.minio
# @pytest.mark.dependency(depends=["Test_gateway_service::test_gateway_service_enable"])
def test_gateway_policy_update():
    url = BASEURL + '/cluster/minio/gateway/policy/update'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "policy": "policy01",
      "raw": {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "s3:*"
            ],
            "Resource": [
              "arn:aws:s3:::*"
            ]
          }
        ]
      }
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.minio
def test_gateway_policy_list():
    url = BASEURL + '/cluster/minio/gateway/policy/list'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []


@pytest.mark.minio
def test_gateway_policy_info():
    url = BASEURL + '/cluster/minio/gateway/policy/info'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "policy_list": [
        "policy01"
      ]
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []


@pytest.mark.minio
def test_gateway_user_update():
    url = BASEURL + '/cluster/minio/gateway/user/update'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "username": user1,
      "password": password,
      "group_list": [
      ],
      "policy_list": [
          "policy01"
      ],
      "enable": "true"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.minio
def test_gateway_user_list():
    url = BASEURL + '/cluster/minio/gateway/user/list'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    print(json.dumps(result.json(), indent=4))
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []


@pytest.mark.minio
def test_gateway_user_info():
    url = BASEURL + '/cluster/minio/gateway/user/info'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "username_list": [
        user1
      ]
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    a = result.json()['data']
    assert a != []


@pytest.mark.minio
def test_gateway_group_update():
    url = BASEURL + '/cluster/minio/gateway/group/update'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "group": "group01",
      "username_list": [
        user1
      ],
      "policy_list": [
        "policy01"
      ],
      "enable": 'true'
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.minio
def test_gateway_group_list():
    url = BASEURL + '/cluster/minio/gateway/group/list'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []
    print(json.dumps(result.json(), indent=4))

@pytest.mark.minio
def test_gateway_group_info():
    url = BASEURL + '/cluster/minio/gateway/group/info'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "username_list": [
        user1
      ]
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []
    print(json.dumps(result.json(), indent=4))

@pytest.mark.minio
def test_gateway_bucket_update():
    url = BASEURL + '/cluster/minio/gateway/bucket/update'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname,
      "bucket": "pytest-bucket",
      "policy": "none"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.minio
def test_gateway_bucket_list():
    url = BASEURL + '/cluster/minio/gateway/bucket/list'
    rdata = {
      "req_host": "127.0.0.1",
      "config": configname
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()['data']
    assert a != []
    print(json.dumps(result.json(), indent=4))

