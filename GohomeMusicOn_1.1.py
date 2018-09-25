import time
import pygame
import os, shutil
import random


# 遍历目录下所有音乐文件
ip = '192.168.1.200'
pygame.mixer.init()
played_musiclist=[]
def musicTree():
    music_list = open('/Users/zhangyaoke/Documents/python/Project/SmartHome/music_list.txt', 'w+')
    work_dir = '/Users/zhangyaoke/Documents/MP3/'
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            # print(filename)
            music_list.write(filename+"\n")
            #print('文件完整路径：%s\n' % file_path)

    music_list.close()
musicTree()

def music_play():

    open_musicName = open('/Users/zhangyaoke/Documents/python/Project/SmartHome/music_list.txt','r')
    read_musicName  = open_musicName.read()
    musicName = []
    musicName.append(read_musicName.split('\n'))
    print(musicName[0])
    # del musicName[0][0]
    # print(musicName[0])
    # open_musicName.close()
    # return(musicName)


    def music_do():

        # pygame.mixer.init()
        # music_number = random.randint(0,len(musicName[0]))
        # 加载音乐
        # pygame.mixer.music.load("/Users/zhangyaoke/Desktop/MP3/" + musicName[0][music_number])
        while True:
            # pygame.mixer.music.load("/Users/zhangyaoke/Music/QQ音乐/" + musicName[0][1])
            # 检查音乐流播放，有返回True，没有返回False
            # 如果没有音乐流则选择播放
            if pygame.mixer.music.get_busy() == False:
                music_number = random.randint(0,len(musicName[0])-2)#随机音乐选取
                # print(music_number)
                if len(played_musiclist)<len(musicName[0]):
                    if music_number in played_musiclist:
                        continue

                    else:
                        played_musiclist.append(music_number)
                else:
                    played_musiclist.clear()
                    played_musiclist.append(music_number)

                pygame.mixer.music.load("/Users/zhangyaoke/Documents/MP3/" + musicName[0][music_number])
                pygame.mixer.music.play()
                #
                print('当前正在播放：' +musicName[0][music_number])
                while pygame.mixer.music.get_busy() == True:

                    backinfo = os.system('ping -c 1 -W 300 %s' % ip)
                    # print(backinfo)
                    if backinfo:
                        pygame.mixer.music.pause()
                        print("-----------离开了----------\n")

                        # while pygame.mixer.music.get_busy() == False:
                            # backinfo = os.system('ping -c 1 %s'%ip)
                            # print("暂停了\n")
                            # if backinfo:
                            #     continue
                    else:
                        print('----------在线----------\n')
                        pygame.mixer.music.unpause()

                    # else:
                    #     continue


                # pygame.mixer.music.queue("/Users/zhangyaoke/Desktop/MP3/" + musicName[0][random.randint(0,len(musicName[0]))
    music_do()




def findPhone():

    # iplist = list()
    # ip = '192.168.1.101' #本地服务器ip
    # ip = '172.24.186.191'
    notAtHome = True
    while notAtHome:
        backinfo = os.system('ping -c 1 -W 300 %s' % ip)  # 实现pingIP地址的功能，-c 指发送报文次数
        # print (backinfo)
        # print (backinfo)
        # print (type(backinfo))
        print("----------未连线----------\n")
        if backinfo:
            print("Not At Home.")
            continue
        else:
            print("Welcome!")
            # iplist.append(ip)
            # notAtHome = false
            music_play()
            notAtHome = false

findPhone()






# def music_play():
#
#     pygame.mixer.init()
#     #加载音乐
#     pygame.mixer.music.load("/Users/zhangyaoke/Music/QQ音乐/"+)
#     while True:
#         #检查音乐流播放，有返回True，没有返回False
#         #如果没有音乐流则选择播放
#         if pygame.mixer.music.get_busy()==False:
#             pygame.mixer.music.play()
#             print('当前正在播放：'+)
#             # pygame.mixer.music.queue(filename)
# music_play()


#遍历目录下所有音乐文件

# import os, shutil
#
# def musicName():
#     music_list = open('music_list.txt', 'a+')
#     work_dir = '/Users/zhangyaoke/Music/QQ音乐/'
#     for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
#         for filename in filenames:
#             file_path = os.path.join(parent, filename)
#             print(filename)
#             music_list.write(filename+"\n")
#             # print('文件完整路径：%s\n' % file_path)
#
#     music_list.close()
# musicName()

