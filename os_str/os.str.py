#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os.path

def find_file(dir_path, str):
    for f in os.listdir(dir_path):

        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path):
            if str in f:
                print(f_path)
        elif os.path.isdir(f_path):
            find_file(os.path.join(dir_path, f), str)

if __name__ == '__main__':
    find_file('.','os')
