# 原理架构
     通过底层使用pytest+allure可以实现最简版自动化测试；
     通过jenkins可以集成allure插件并拉去代码构建测试；
     通过docker可以将jenkins所有插件及其数据打包，放在任意节点使用。

 具体使用可参考：\\192.168.1.10\研发\TEST\xdfs_test\xdfs6.0

 MyPytest为根目录进行开发，根目录下存放pytest配置文件及脚本；二级目录存放测试用例

 ![Image text](http://192.168.1.11/liusl/image-storage/raw/master/xdfs6_api/%E6%96%B9%E6%A1%88%E7%AE%80%E4%BB%8B.jpg)

# 程序简介

Ansible 部署jenkins和docker环境/部署xdfs6.0

Docker 将数据持久化并运行jenkins（docker打包好jenkins数据及Pipeline）

Jenkins 通过Pipeline实现部署xdfs6.0或是一键测试

Java 是jenkins与节点之间互相通信的依赖

Pytest 该框架实现编写测试用例

Allure 将测试的结果以可视化界面展示

![Image text](http://192.168.1.11/liusl/image-storage/raw/master/xdfs6_api/%E7%A8%8B%E5%BA%8F%E7%AE%80%E4%BB%8B.jpg)

# 使用说明

1、git clone http://gitlab.taocloud.com/liusl/mytest.git

2、修改需要测试集群conftest.py文件，集群及其ip

#后执行sh cluster_api_auto.sh > api.log(本次操作无需执行，)

3、git push -m origin master 提交

4、后登录jenkins（http://172.26.172.8:8080）查看测试报告

    通过git克隆修改集群ip提交后jenkins自动触发测试；
    运行完成会有两个报告，一个是所有协议服务创建更新等，一个是清空环境报告。

- 集群节点的数据盘必须大于2
- 可通过执行单个文件或目录运行单个服务，例如： pytest -vs test_user
    执行单个用例，可参考：用例文件名::用例类::用例函数
- 本次测试使用的是双副本，卷名可自定义
- 客户端需要安装nfs，cifs，glusterfs包进行挂载验证

# 结果输出
- report.html

pytest默认输出测试报告，依赖pytest-html

运行时指定参数： --html=report.html

- allure

需要安装：allure-pytest

执行时指定参数：--alluredir=./allure_results

用例运行完成后如下转换为html格式：

allure generate ./allure_results/ -o ./allure_report

通过如下端口映射访问：

allure serve allure_report -h 172.26.172.12 -p 8888

如下测试报告

![Image text](http://192.168.1.11/liusl/image-storage/raw/master/xdfs6_api/allure_results.jpg)


# 遗留问题
1、无法找到gluster.info信息导致无法enable服务，需手动启动gluterd后执行cluster用例

2、创建GNFS共享返回222,需要单节点下发

3、部分接口存在bug，待修复状态，具体可查看用例结果输出

具体看参考语雀链接：https://taocloud.yuque.com/xdfs/fqnguu/uqbiwq#IK69
