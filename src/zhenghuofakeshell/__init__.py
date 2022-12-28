#!/usr/bin/env python
'''
你导入这个鬼东西有意义吗
'''
import os
import signal
import random

PASSWORD = "password" # 孩子，你是相信命运之神，还是相信流控制？
PS1 = "[root@archlinux] $"


def fresh_ps1() -> None:
    '''
    如果你觉得更新这玩意有必要的话
    '''


def ignore(signum, frame):
    pass

def run():
    try:
        data: str = "abcdefghijklmnopqrstuvwxyz123456-_"
        signal.signal(signal.SIGINT, ignore)
        signal.signal(signal.SIGTERM, ignore)
        while True:
            fresh_ps1()
            input_command: str = input(PS1 + " ")  # TODO: 回显为随机字符
            if input_command == PASSWORD:
                os.system("bash")
            random_command: str = ""
            split_input = input_command.split(" ")
            if len(split_input[0]) < 4:
                split_input[0] += random.choice(data) + random.choice(
                    data) + random.choice(data)
            for i in split_input:
                for g in range(len(i) + random.randint(1, 10)):
                    random_command += random.choice(data)
                random_command += " "
            output = os.popen("bash -c '" + random_command + "'").read()
            print(output, end='')
    
    except Exception:  # 鬼知道会出什么奇奇怪怪的问题，别露馅就对了
        pass
    
    except KeyboardInterrupt:
        pass
