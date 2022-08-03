<h1 align="center">🔋 waste-django</h1>

<p align="center">
<a target="_blank" href="https://github.com/zhouboyi1998/waste-django"> 
<img src="https://img.shields.io/github/stars/zhouboyi1998/waste-django?logo=github">
</a>
<a target="_blank" href="https://opensource.org/licenses/MIT"> 
<img src="https://img.shields.io/badge/license-MIT-red"> 
</a>
<img src="https://img.shields.io/badge/Python-3.7-blue">
<img src="https://img.shields.io/badge/Django-3.2.14-darkgreen">
<img src="https://img.shields.io/badge/Django REST Framework-3.13.1-darkgreen">
<img src="https://img.shields.io/badge/MySQL Client-1.4.6-darkgreen">
<img src="https://img.shields.io/badge/Requests-2.28.1-blue">
<img src="https://img.shields.io/badge/lxml-4.9.1-darkgreen">
</p>

### 📖 语言

简体中文 | [English](./README.en.md)

### ⌛ 开始

#### 创建虚拟环境

* 在 `/src` 目录下创建虚拟环境

#### 安装第三方库

```
pip install django==3.2.14 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install djangorestframework==3.13.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install requests==2.28.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install lxml==4.9.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install mysqlclient==1.4.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### pip 国内镜像源

```
# 清华大学
https://pypi.tuna.tsinghua.edu.cn/simple

# 中国科学技术大学
https://pypi.mirrors.ustc.edu.cn/simple

# 阿里云
https://mirrors.aliyun.com/pypi/simple

# 豆瓣
https://pypi.douban.com/simple
```

#### 命令列表

```bash
# 运行
python manage.py runserver

# 安装新模块
python manage.py startapp <module-name>

# 更新模型
python manage.py makemigrations

# 更新数据库表
python manage.py migrate
```

### 📜 开源协议

[MIT License](https://opensource.org/licenses/MIT) Copyright (c) 2022 周博义
