## 测试用例组织结构
- [测试组织结构图](http://192.168.1.11/gluster/XDFS-UMI/blob/UMI_Test/umi_test/umi_apis_test/Docs/测试组织结构图.png)

## 测试说明
- 此测试用例集是基于httprunner 3框架编写。
- 目前测试实现了基于数据驱动的测试，测试时仅需要对data/目录的下面数据的文件 进行适当的配置后，即可执行测试。


## 准备工作
- 环境准备
  - 每次测试 要求服务端节点数 最小为 3，且每台节点都需要配置好glusterfs的初始环境。
  - 每个节点需要配置 4块网卡 （ 其中glusterfs需要两块配置IP， 测试网卡需要两块不配置IP）
    - 注意：为了方便测试，测试环境中可以通过修改内核参数的方式设置网卡命名方式为传统的方式(如eth2，eth3)，这不是必须的。
  - 每个节点除系统盘外， 配置一块用于用于测试的数据磁盘
    - 注意：磁盘必须是空闲的： 没有挂载且没有其他的应用占用的
  - 另外需要一台可以和服务端通信的测试节点。 网段配置到glusterfs 的网络上。
   
- 创建测试目录
  - 创建测试目录的操作已经集成到debugtalk.py中， 执行 python debugtalk.py 即可。debugtalk.py 会根据data/ 下面的配置自动创建测试目录

- 数据驱动
   - 数据驱动的文件位于data/ 目录下面
   - base.conf 这个文件存储全局的配置。具体配置说明参考文件注释
   - glusterfs.csv 中配置的是除api 所在节点之外的其他节点
   - network.csv 中配置的是 api接口所在节点的两块测试网卡
   - nfs.csv，samba.csv, user.csv ,iscsi.csv: 配置的是nfs的api接口部分参数, 具体可参考api接口说明
   - storage.csv: 这个文件中存储卷测试 和 磁盘测试 有关的参数。 
     - 文件中mode（replica, arbiter, disperse-data）为必选项。
     - host01-host06 主要用在brick名中:
       - 在volume sync 测试中要求host01和host02为不同的节点
       - 其他可以为相同的主机名，也可以是不同的主机名。
     - block01是host01对应节点上面的空闲块设备。 
      

## 运行测试
- 特别注意
  - 运行测试之前必须先执行 python debugtalk.py 初始化环境
  - 运行测试之前需要确认空闲磁盘设备没有被占用

- 单步测试如下： 
```
hrun -s user.yml
```

- 测试集测试如下：
```
hrun -s users/
hrun -s network/network_in_summary.yml
```

- 全部测试
```
hrun -s summary.yml
```

- 幂等性测试
  - 原则上，需要上述的其他测试均测试通过后再执行幂等性测试。测试步骤同上。
  - 幂等性测试前需要执行 python debugtalk.py idempotence 将常规测试用例转换为幂等性测试用例。原始测试用例目录 umi_node 备份为 umi_node_origin

- 错误重试
  - 当运行全部测试出现报错之后，可以对出现的报错的测试用例执行的单步测试进一步确定问题。

## 测试报告
- 生成报告 
  - 执行测试时添加 --alluredir=dir 选项生成 allure 报告数据, 例如:
  ```
   hrun summary.yml --alluredir=./report
   hrun users/ --alluredir=./report
  ```
- 查看报告
  - 测试运行完成后，执行命令启动allure的页面访问
   ```
   allure serve ./report -p 8080
   ```
   
- 收集报告
   - 测试完成后， 将report目录打包发送至开发即可


## 问题说明

参考：[上一级目录的ReadMe.md](http://192.168.1.11/gluster/XDFS-UMI/tree/UMI_Test/umi_test/umi_apis_test#存在问题)

