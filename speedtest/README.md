# Speedtest
***
## 一、安装apache2 php服务
    sudo apt install apache2 php

## 二、下载LibreSpeed
    git clone https://github.com/librespeed/speedtest.git

## 三、复制主页文件到apache2 /var/www/html
### 进入speedtest文件夹
    cd speedtest
### 拷贝文件到/var/www/html
    sudo cp -R backend example-singleServer-gauges.html *.js /var/www/html/
### 进入 /var/www/html
    cd /var/www/html  
### 查看是否拷贝成功
    ls -la
### 复制到index.html
    sudo mv example-singleServer-gauges.html index.html
## 四、修改文件夹权限
    sudo chown -R www-data *
## 五、启动服务
    sudo /etc/init.d/apache2 start




[//]: # (## 安装php或者nginx和apache任何一个)

[//]: # ()
[//]: # (    sudo apt install php nginx apache)

[//]: # ()
[//]: # (## git speedtest)

[//]: # (  sudo git clone https://github.com/librespeed/speedtest.git)

[//]: # (## 进入speedtest文件夹)

[//]: # (  cd /speedtest)

[//]: # (## 查看当前目录下文件夹-竖列)

[//]: # (  ls -la)

[//]: # (## 复制文件)

[//]: # (  sudo cp -R backend example-singleServer-pretty.html *.js /var/www/html/)

[//]: # (## 复制文件)

[//]: # (  sudo cp -R backend example-singleServer-pretty.html *.js /var/www/html/)

[//]: # (## 进入文件夹)

[//]: # (  cd /var/www/html)

[//]: # (## 查看当前目录下文件夹-竖列)

[//]: # (  ls -la)

[//]: # (## 复制文件)

[//]: # (  sudo mv example-singleServer-pretty.html index.html)

[//]: # (## 更改)

[//]: # (  sudo chown -R www-data *)

[//]: # ()
[//]: # ()
[//]: # (## 1、然后安装apache2 与 php)

[//]: # ()
[//]: # (    sudo apt-get install apache2 php git)

[//]: # ()
[//]: # (## 2、从github下载项目)

[//]: # ()
[//]: # (    sudo git clone https://github.com/librespeed/speedtest.git)

[//]: # ()
[//]: # (## 3、配置librespeed)

[//]: # ()
[//]: # (    sudo cd speedtest)

[//]: # ()
[//]: # (    sudo cp -R backend example-singleServer-pretty.html *.js /var/www/html/)

[//]: # ()
[//]: # (    sudo cd /var/www/html/)

[//]: # ()
[//]: # (    sudo mv example-singleServer-pretty.html index.html)

[//]: # ()
[//]: # (    sudo chown -R www-data)
