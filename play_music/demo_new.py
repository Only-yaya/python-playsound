#-*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-

import pygame
import time

# 初始化音频模块
pygame.mixer.init()

for i in range(3):
    print('是否有音乐在播放(1:是/0:否):',pygame.mixer.music.get_busy())
    pygame.mixer.music.load(r'D:\code\play_music\xx_long.mp3')
    # play函数立即返回,音乐播放在后台进行
    # loops:重复的次数,start:开始播放的位置
    pygame.mixer.music.play(loops=1, start=0.0)
    time.sleep(1.5)

time.sleep(10)
