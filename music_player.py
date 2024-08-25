#!/usr/bin/env python
# *-* coding: utf-8 *-*
# Future
from __future__ import print_function
from __future__ import unicode_literals

import threading
import time

# Gen/Builtins Lib
# Standard Lib
# Others/Owned Lib

"""
@File:  music_player.py
@Auth:  Aaron
@Time:  2024-08-25
@Desc:  
@Logs:
"""

# from playsound import playsound

# playsound('blue_elf.mp3')

# from pydub import AudioSegment

# from pydub.playback import play

# song = AudioSegment.from_mp3('blue_elf.mp3')

# play(song)

# import os

# os.system('mpg123' + 'blue_elf.py')


# import pygame
#
# # 初始化pygame音频引擎
# pygame.mixer.init()
# # 加载音乐文件
# # music_file = '/d/AarPython/AarFlask/Demo_Restx/blue_elf.mp3'
# music_file = 'blue_elf.mp3'
# pygame.mixer.music.load(music_file)
# # 播放音乐
# pygame.mixer.music.play()

# C:\Program Files\VideoLAN\VLC

import os

os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc

print(vlc.__file__)
from service.vlc_player import Player


class MusicPlayer(object):
    def __init__(self, path):
        self.path = path
        self.player = Player()
        # self.player.play(path)
        self.flag = False

    def play(self):
        self.flag = True
        self.player.play(self.path)
        while self.flag:
            if self.player.get_state() == -1:
                self.player.play(self.path)
            time.sleep(1)

    def stop(self):
        self.flag = False
        self.player.stop()

    def status(self):
        return self.player.get_state()


if "__main__" == __name__:
    # player = MusicPlayer()
    # player.add_callback(vlc.EventType.MediaPlayerTimeChanged, my_call_back)
    # 在线播放流媒体视频
    # player.play("blue_elf.mp3")

    # 播放本地mp3
    # player.play("D:/abc.mp3")

    # 防止当前进程退出
    # threading.Thread(my_call_back2).start()
    # my_call_back2()

    player = MusicPlayer("blue_elf.mp3")
    # player.play("blue_elf.mp3")
    threading.Thread(target=player.play).start()
    # player.play()

    # while True:
    #     print(player.status())
    #     print(1111111111)

    print(11111)
    time.sleep(5 * 60)
    print(22222)
    threading.Thread(target=player.stop).start()
