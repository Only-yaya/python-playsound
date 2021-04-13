# 使用python-playsound模块播放音乐


修复playsound模块,解除资源占用

使用python-playsound模块播放音乐,执行dome.py

使用线程和进程两种方式进行后台播放,播放不阻塞主程序执行

playsound模块只提供了一个播放功能

通过杀死进程,多次重复播放可终止前一次播放未完成任务


弃坑playsound了,用pygame它不香吗,pygame自带线程播放功能,完全符合功能需求

pygame测试代码demo_new.py
