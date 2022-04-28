# NOTE: Generated By HttpRunner v3.1.6
# FROM: umi_cluster/volume_cifs_uninit_node3.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseVolumeCifsUninitNode3(HttpRunner):

    config = Config("${ENV(umi_cluster_test_title)}").base_url(
        "${ENV(umi_cluster_url)}"
    )

    teststeps = [
        Step(
            RunRequest("Cifs User Delete")
            .post("/cluster/cifs/user/delete")
            .with_json({"req_host": "127.0.0.1", "user": "usr-01"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("Cifs Share Delete")
            .post("/cluster/cifs/share/delete")
            .with_json({"req_host": "127.0.0.1", "name": "share-01"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseVolumeCifsUninitNode3().test_start()