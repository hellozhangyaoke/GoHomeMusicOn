# GoHomeMusicOn
when I come home,My computer will play the song.when I leave home,the music will pause.

# 这个是我刚学习Python时候做的小东西
## 能干什么？
我回到家的时候家里的音响会自动播放音乐。
## 实现方式
* 这个脚本我运行在我家里的树莓派上；
* 我在路由器绑定了我手机的ip地址；
* 这个脚本会一直ping我手机ip，如果我到家了，手机会自动接上wifi，ping通了会自动播放音乐，同时还在定时监听手机是否还在线上；
* 如果我出门了，手机断开了wifi，ping不通了会断开音乐；
* 音乐文件夹我设定在NAS上，使用的random随机循环播放。
