# NOTE: Generated By HttpRunner v3.1.6
# FROM: umi_cluster/volume_build_uninit_node3.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseVolumeBuildUninitNode3(HttpRunner):

    config = Config("${ENV(umi_cluster_test_title)}").base_url(
        "${ENV(umi_cluster_url)}"
    )

    teststeps = [
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
        Step(
            RunRequest("Cluster Node Remove")
            .post("/cluster/volume/delete")
            .with_json({"req_host": "127.0.0.1", "node_addr": "172.169.100.71"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Node Remove")
            .post("/cluster/volume/delete")
            .with_json({"req_host": "127.0.0.1", "node_addr": "172.169.100.72"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cluster Node Remove")
            .post("/cluster/volume/delete")
            .with_json({"req_host": "127.0.0.1", "node_addr": "172.169.100.73"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Block Device Disable")
            .post("/storage/block_device/disable")
            .with_json({"req_host": "127.0.0.1", "dev_path": "/dev/sdb1"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseVolumeBuildUninitNode3().test_start()