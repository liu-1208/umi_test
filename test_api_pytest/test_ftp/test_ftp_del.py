import  json
import  requests
import  pytest
from conftest import BASEURL

share_name = 'ftp_share'

rdata = {
  "req_host": "127.0.0.1"
}

@pytest.mark.ftp_service()
def test_gluster_ftp_share_del():
    url = BASEURL + '/cluster/ftp/share/delete'
    rdata = {
        "req_host":"127.0.0.1",
        "share_name":share_name
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url,jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(),indent=4))


@pytest.mark.ftp_service()
def test_gluster_ftp_service_disable():
    url = BASEURL + '/cluster/ftp/service/disable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url,jsonstr)
    assert  result.status_code == 200
    print(json.dumps(result.json(), indent=4))



