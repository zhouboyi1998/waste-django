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
<img src="https://img.shields.io/badge/Django CORS Header-3.13.0-darkgreen">
<img src="https://img.shields.io/badge/MySQL Client-1.4.6-darkgreen">
<img src="https://img.shields.io/badge/Requests-2.28.1-blue">
<img src="https://img.shields.io/badge/lxml-4.9.1-darkgreen">
</p>

### 📖 Language

[简体中文](./README.md) | English

### ⌛ Start

#### Create Virtualenv

* Create Virtualenv in the `/src` directory

#### Install third-party libraries

```
pip install django==3.2.14

pip install djangorestframework==3.13.1

pip install django-cors-headers==3.13.0

pip install requests==2.28.1

pip install lxml==4.9.1

pip install mysqlclient==1.4.6
```

#### Command list

```bash
# Run
python manage.py runserver

# Install new module
python manage.py startapp <module-name>

# Update models
python manage.py makemigrations

# Update database's table
python manage.py migrate
```

### 📜 Licence

[MIT License](https://opensource.org/licenses/MIT) Copyright (c) 2022 周博义
