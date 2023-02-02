# other
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
