#-*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-

from playsound import playsound
import threading
import inspect
import ctypes
import time
import multiprocessing


# 播放
def play(path, cyc=False):
    if cyc:
        # 循环播放
        while 1:
            playsound(path)
    else:
        playsound(path)


def _async_raise(tid, exctype):
    # 引发异常,根据需要执行清理
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        print('线程id无效,可能已释放')
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError('PyThreadState_SetAsyncExc failed')
    print('杀死线程')


def stop_thread(thread):
    # 杀死线程
    _async_raise(thread.ident, SystemExit)

if __name__ == "__main__":

    # 播放音乐绝对路径
    path = r"D:\code\play_music\xx_long.mp3"

    # 音乐播放线程或进程
    music = None
    '''
        线程
        代码bug:
        杀死线程后,并不能结束playsound上个播放任务,导致多个播放任务混音
        分析原因:music线程创建另外的一个线程来播放音乐,只杀死了music线程,播放音乐线程还在运行,
                未找到播放音乐线程
    '''
    # for i in range(3):
    #     list = threading.enumerate()
    #     print('程序中的线程数量:',len(list))
    #     for ii in list:
    #         print(ii.ident)
    #     # 检查线程
    #     if music:
    #         # 存在,杀死线程
    #         print(music.ident)
    #         stop_thread(music)
    #
    #     # target调用play函数,args赋值元组.mp3文件
    #     music = threading.Thread(target=play, args=(path,))
    #     music.start()
    #     print('当前线程id:',music.ident,music.name)
    #     print('循环当前次数:',i)
    #     time.sleep(5)
    # time.sleep(20)
    '''
        进程使用
    '''
    for i in range(3):
        # 检查进程
        if music:
            # 存在,杀死进程
            music.terminate()

        # 开启子进程
        music = multiprocessing.Process(target=play, args=(path,))
        music.start()

        print('循环当前次数:', i, '当前进程id:', music.pid)
        time.sleep(5)
    time.sleep(20)

    # 检查进程
    if music:
        # 存在,杀死进程
        music.terminate()
