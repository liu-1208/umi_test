# _*_ coding: utf-8 _*_
import json
import requests


NODE_IP = "172.18.123.73"
NODE_PORT = "8000"


requests_url = f"http://{NODE_IP}:{NODE_PORT}/cluster/volume/start"


headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


json_data = {
    "req_host": "127.0.0.1",
    "vol_name": "vol-01"
}


if __name__ == '__main__':
    response = requests.post(url=requests_url, headers=headers, json=json_data)
    # response.json()["data"]
    response_json = json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ":"))
    print(response_json)


