# 概述
- 一个基于httprunner测试api的项目

#  安装httprunner

```
pipenv shell
pip install httprunner
pip show httprunner
```
# 创建测试项目

```
# 创建一个名为demo的测试项目
#  hrun --startproject demo  新版本中这条命令不可用， 使用下面的命令代替
httprunner startproject demo 
```
- 创建过程

```
(XDFS-UMI) [root@d01 httprunner]# httprunner startproject demo
2021-08-19 14:22:54.043 | INFO     | httprunner.scaffold:create_scaffold:43 - Create new project: demo
Project Root Dir: /root/httprunner/demo

created folder: demo
created folder: demo/har
created folder: demo/testcases
created folder: demo/reports
created file: demo/testcases/demo_testcase_request.yml
created file: demo/testcases/demo_testcase_ref.yml
created file: demo/debugtalk.py
created file: demo/.env
created file: demo/.gitignore

$ tree demo -a
demo
├── debugtalk.py
├── .env
├── .gitignore
├── har
├── reports
└── testcases
    ├── demo_testcase_ref.yml
    └── demo_testcase_request.yml

3 directories, 5 files

Sentry is attempting to send 0 pending error messages
Waiting up to 2 seconds
Press Ctrl-C to quit
(XDFS-UMI) [root@d01 httprunner]# 
```

# 项目组织结构
```
                   |-- ReadMe.md
                   |-- debugtalk.py
                   |-- Docs/
${projectRootDir} -|-- logs/
                   |-- har/
                   |-- reports/
                   |-- testcases/
                   |-- xdfscases/
```

# 运行测试示例
```
# httprunner  创建的默认项目中包含两个测试实例 ，  位于 testcases/   下面
# hrun testcases --html=report.html --self-contained-html  可以生成测试报告
hrun testcases/
```

# 编写并运行自己的测试用例
- 编写规则： 
  - 官方文档： https://docs.httprunner.org/
  - 一个中文页面：  https://ontheway-cool.gitee.io/httprunner3doc_cn/
- 运行方式：  
  - 启动XDFS_UMI项目，参考 http://192.168.1.11/gluster/XDFS-UMI/tree/ffc#项目启动
  - 进入测试项目根目录
  - 修改httprunner全局变量文件.env中的base_url为自己的api地址
  - 运行hrun xdfstest/

# 存在问题
- httprunner  执行yml文件的测试时， 如果 api返回的值是None ，hrun 运行会报错。（类似 https://githubmemory.com/repo/samuelcolvin/pydantic/issues/3049 ）
  - 1、目前还没有找到公开的解决方法
  - 2、在httprunner 3.1.1 版本中 fix了一个关于的none的bug ，  似乎和当前这个问题没关系（当前版本是3.1.6）：  https://docs.httprunner.org/CHANGELOG/
  - 3、一个临时的解决方式。 对httprunner 中的 models.py 作如下修改， vim   .venv/lib/python3.6/site-packages/httprunner/models.py

```
130 class ResponseData(BaseModel):
131     status_code: int
132     headers: Dict
133     cookies: Cookies
134     encoding: Union[Text, None] = None
135     content_type: Text
136     # body: Union[Text, bytes, List, Dict]
137     body: Union[Text, bytes, List, Dict, None]
```
- 在最新版本3.1.6没有找到通过自定义模板 生成测试报告的方式， 但是可以生成 pytest 和 allure 格式的报告。  通过模板生成报告的这种方式  应该是被去掉了， 或者3.x的httprunner中还没有开发完成




