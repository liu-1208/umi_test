# 执行环境
- pip install httprunner
- pip3 install xlrd xlwt xlutils

# umi cluster 接口冒烟测试
- nohup python main_cluster.py 2>&1 &
- nohup python main_node.py 2>&1 & 
- 组合测试：hrun -s umi_cluster_test_summary.yml
- 分开测试：hrun -s *.yml

# 执行过程
- 基础描述：设置3节点（172.18.123.71/72/73）集群，每个节点配置一块硬盘；配置3副本gluster卷，并配置nfs/cifs/iscsi共享。集群中每个
         节点的agent都要开启。req_host指的是：web地址；node_addr指的是：存储私有地址。

- 原理描述：冒烟测试，一旦出现问题就停止。

# 参考资料

- 运行测试用例
https://ontheway.cool/HttpRunner3DocsForCN/user_guide/run_testcase/

- Python 操作 Excel
http://www.ityouknow.com/python/2019/12/29/python-excel-103.html
https://www.xiaoheidiannao.com/53232.html
https://www.jianshu.com/p/c8ae6852f1da
https://www.cxyzjd.com/article/qq_41725214/103511099

- 多个sheet合成一个sheet
```
    Sub 合并当前工作簿下的所有工作表()
    Application.ScreenUpdating = False
    For j = 1 To Sheets.Count
    If Sheets(j).Name <> ActiveSheet.Name Then
    X = Range("A65536").End(xlUp).Row + 1
    Sheets(j).UsedRange.Copy Cells(X, 1)
    End If
    Next
    Range("B1").Select
    Application.ScreenUpdating = True
    MsgBox "当前工作簿下的全部工作表已经合并完毕！", vbInformation, "提示"
    End Sub
```