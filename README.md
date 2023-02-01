***
## xui
### 更新软件源
    apt update
### 启用 BBR TCP 拥塞控制算法

```
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
```

### 安装x-ui：
    bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)

### 安装nginx
    apt install nginx
### 安装acme：
    curl https://get.acme.sh | sh
### 添加软链接：
    ln -s  /root/.acme.sh/acme.sh /usr/local/bin/acme.sh
### 切换CA机构： 
    acme.sh --set-default-ca --server letsencrypt
### 申请证书： 
    acme.sh  --issue -d 你的域名 -k ec-256 --webroot  /var/www/html
### 安装证书：
    acme.sh --install-cert -d 你的域名 --ecc --key-file       /etc/x-ui/server.key  --fullchain-file /etc/x-ui/server.crt --reloadcmd     "systemctl force-reload nginx"
***
### 寻找合适的伪装站
    示例关键字：intext:登录 Cloudreve
### 配置nginx
    配置文件路径：/etc/nginx/nginx.conf
X
```
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 1024;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    gzip on;

    server {
        listen 443 ssl;
        
        server_name nicename.co;  #你的域名
        ssl_certificate       /etc/x-ui/server.crt;  #证书位置
        ssl_certificate_key   /etc/x-ui/server.key; #私钥位置
        
        ssl_session_timeout 1d;
        ssl_session_cache shared:MozSSL:10m;
        ssl_session_tickets off;
        ssl_protocols    TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers off;

        location / {
            proxy_pass https://bing.com; #伪装网址
            proxy_redirect off;
            proxy_ssl_server_name on;
            sub_filter_once off;
            sub_filter "bing.com" $server_name;
            proxy_set_header Host "bing.com";
            proxy_set_header Referer $http_referer;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header User-Agent $http_user_agent;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto https;
            proxy_set_header Accept-Encoding "";
            proxy_set_header Accept-Language "zh-CN";
        }


        location /ray {   #分流路径
            proxy_redirect off;
            proxy_pass http://127.0.0.1:10000; #Xray端口
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        
        location /xui {   #xui路径
            proxy_redirect off;
            proxy_pass http://127.0.0.1:9999;  #xui监听端口
            proxy_http_version 1.1;
            proxy_set_header Host $host;
        }
    }

    server {
        listen 80;
        location /.well-known/ {
               root /var/www/html;
            }
        location / {
                rewrite ^(.*)$ https://$host$1 permanent;
            }
    }
}
```

### 重启niginx 每次修改nginx配置文件后必须使用 systemctl reload nginx 命令重新加载配置文件
    systemctl reload nginx
***
### 多用户合租
```

location /ray {   #分流路径
    proxy_redirect off;
    proxy_pass http://127.0.0.1:10000; #Xray端口
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```
***
## Trojan
## 新建trojan
```
mkdir trojan
cd trojan/
```
## 下载trojan-go

    wget https://github.com/p4gefau1t/trojan-go/releases/download/v0.10.6/trojan-go-linux-amd64.zip
    
## 解压文件
    
    unzip trojan-go-linux-amd64.zip

##  创建 trojan.json


    touch trojan.json
    
### trojan配置文件：
```
{
    "run_type": "server",
    "local_addr": "0.0.0.0",
    "local_port": 443,
    "remote_addr": "192.168.1.1",
    "remote_port": 80,
    "password": [
        "your_awesome_password"
    ],
    "ssl": {
        "cert": "server.crt",
        "key": "server.key"
    }
}
```
***
## 申请证书：

### 安装acme：
    curl https://get.acme.sh | sh
### 安装socat：
    apt install socat
### 添加软链接：
    ln -s  /root/.acme.sh/acme.sh /usr/local/bin/acme.sh
### 注册账号： 
    acme.sh --register-account -m my@example.com
### 开放80端口：
    ufw allow 80
### 申请证书： 
    acme.sh  --issue -d 替换为你的域名  --standalone -k ec-256
### 安装证书： 
    acme.sh --installcert -d 替换为你的域名 --ecc  --key-file   /root/trojan/server.key   --fullchain-file /root/trojan/server.crt 

### 如果默认CA无法颁发，则可以切换下列CA：
### 切换 Let’s Encrypt：
    acme.sh --set-default-ca --server letsencrypt
#### 切换 Buypass：
    acme.sh --set-default-ca --server buypass
### 切换 ZeroSSL：
    acme.sh --set-default-ca --server zerossl
***
## 自签证书：

### 生成私钥：
    openssl ecparam -genkey -name prime256v1 -out ca.key
### 生成证书：
    openssl req -new -x509 -days 36500 -key ca.key -out ca.crt  -subj "/CN=bing.com"
### 后台运行：

    nohup ./trojan-go > trojan.log 2>&1 &
***

```
x-ui面板：https://github.com/vaxilu/x-ui
CF优选IP：https://github.com/XIU2/CloudflareSpeedTest
CF官网：https://cloudflare.com
CF-CDN-IP段：https://www.cloudflare.com/zh-cn/ips/
```
***
```
#查询当前使用的 TCP 拥塞控制算法
sysctl net.ipv4.tcp_congestion_control
#查询当前Linux版本
uname -r

#启用BBR TCP拥塞控制算法
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
```


