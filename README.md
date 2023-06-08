# 不再更新！！！！已经完全可以使用了，毕竟是个小工具。

Keep your Telegram Always Online.
让你的 Telegram 永远"在线"

使用了开源项目 - Many Thanks to project: https://github.com/LonamiWebs/Telethon/

# 背景

Don't let others peak on your daily routine with recent online! So keep yourself always online. XD  
如果你不想被人通过在线时间判断作息规律，那就让自己一直保持在线吧！  
（这样子就算你让所有人看见你的在线时间也无所谓咯，同时你还可以看到别人的）  

# 需求 Prerequisite

`一台可以连接到Telegram的服务器`  

# 如何使用？ How to use

### 安装`docker`

### 首先，你需要一个 `Client Token`(这个可以在 https://my.telegram.org 申请)

```shell
docker run -it --name alwaysOnline --restart=always -e api_id="xxx" \ 
-e api_hash="xxx" -e phone="+86111111111111" -e password="password" jp0id/telegram-always-online
```

### 二次验证的话需要输入telegram验证码。

### 有人提议可以像验证码那样通过输入形式输入手机和密码，是可以，只是我懒得弄了，毕竟是自己用的，而且是运行在自己的服务器上，还有二次验证，所以安全性有保证。如果有人还是觉得不放心，可以fork本项目进行修改。

#### fork from https://github.com/abusetelegram/AlwaysOnline-
