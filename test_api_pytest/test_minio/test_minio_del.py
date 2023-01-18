import json
import requests
import pytest
from conftest import BASEURL


rdata = {
    "req_host": "127.0.0.1"
}

sub_dir = "/minio"
user1 = "minio1"
configname = "config01"
password = "11111111"


@pytest.mark.delete
@pytest.mark.minio
class TestMinioDel(object):
    def test_gateway_bucket_delete(self):
        url = BASEURL + '/cluster/minio/gateway/bucket/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "config": configname,
          "bucket": "pytest-bucket",
          "force": 'false'
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.dependency()
    def test_gateway_user_delete(self):
        url = BASEURL + '/cluster/minio/gateway/user/delete'
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

    # @pytest.mark.dependency(depends=["TestMinioDel::test_gateway_user_delete"])
    def test_gateway_group_delete(self):
        url = BASEURL + '/cluster/minio/gateway/group/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "config": configname,
          "group_list": [
            "group01"
          ]
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    def test_gateway_policy_delete(self):
        url = BASEURL + '/cluster/minio/gateway/policy/delete'
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
        print(json.dumps(result.json(), indent=4))

    def test_gateway_service_disable(self):
        url = BASEURL + '/cluster/minio/gateway/service/disable'
        rdata = {
            "req_host": "127.0.0.1",
            "config_list": [
                "config01"
            ]
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
