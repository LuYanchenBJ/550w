#输出标题
from Walimaker import*
t=0
import pygame
import random
import time
pygame.init()
pygame.mixer.music.load("550.flac")
pygame.mixer.music.play(-1)  # -1 表示循环播放，0 表示只播放一次
print('覆写550系列程序中，请稍后')
while True:
    a= random.randint(2,100)
    t=t+a
    print('已完成',t,'共计约641758件文件')
    if t==97:
        time.sleep(4)
    if t==641758:
        print('覆写已完成，欢迎登陆550W')
        break
    if t>641758:
        print('覆写已完成，欢迎登陆550W')
        break
setup(1152,648)
w=Character('550W.png')
w.scale(0.15)
while True:
    update()
