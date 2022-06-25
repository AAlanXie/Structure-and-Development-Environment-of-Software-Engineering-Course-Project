## 运行方法

- 在当前目录下执行命令

``` bash
./runserver.sh #这里默认使用8000端口
```

- 若想要更换端口使用如下指令

  - ``` python
    python manage.py runserver + 端口号
    ```

运行进入页面后在网页地址后加入/login即可进入登录页面
用户名不限，密码为 123456

### 文件说明

- Course_task文件夹中都是django自带的配置文件
- db.sqlite3为存储数据库
- login文件夹中是用户实现的各种文件，其中template文件夹中是各种页面文件
- static中存放使用的js，css，图片等文件
- runserver.sh为运行脚本

