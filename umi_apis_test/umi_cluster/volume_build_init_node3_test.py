# NOTE: Generated By HttpRunner v3.1.6
# FROM: umi_cluster/volume_build_init_node3.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseVolumeBuildInitNode3(HttpRunner):

    config = Config("${ENV(umi_cluster_test_title)}").base_url(
        "${ENV(umi_cluster_url)}"
    )

    teststeps = [
        Step(
            RunRequest("Block Device Wipe")
            .post("/storage/block_device/wipe")
            .with_json({"req_host": "127.0.0.1", "dev_path": "/dev/sde"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Block Device Init")
            .post("/storage/block_device/init")
            .with_json({"req_host": "127.0.0.1", "dev_path": "/dev/sde"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Block Device Enable")
            .post("/storage/block_device/enable")
            .with_json({"req_host": "127.0.0.1", "dev_path": "/dev/sde"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Volume Create")
            .post("/cluster/volume/create")
            .with_json(
                {
                    "req_host": "127.0.0.1",
                    "vol_name": "umi_test",
                    "remote_mnts": [
                        "node1.tc.com:/interface_todo_list/d6ca1aa5-3c4f-4379-ad02-37f6390786c7",
                        "node2.tc.com:/interface_todo_list/68b18b4d-63ed-474c-87e3-c4ffad7aacfe",
                        "node3.tc.com:/interface_todo_list/d050633b-1735-49ca-a897-bf883c8d9b41",
                    ],
                    "vol_type": "Repalica",
                    "vol_pattern": "3",
                    "rdma": False,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Volume Start")
            .post("/cluster/volume/start")
            .with_json({"req_host": "127.0.0.1", "vol_name": "umi_test"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Volume Stop")
            .post("/cluster/volume/stop")
            .with_json({"req_host": "127.0.0.1", "vol_name": "umi_test"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Volume Delete")
            .post("/cluster/volume/delete")
            .with_json({"req_host": "127.0.0.1", "vol_name": "umi_test"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseVolumeBuildInitNode3().test_start()