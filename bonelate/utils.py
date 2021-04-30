#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/25 22:15
# @Author : 詹荣瑞
# @File : utils.py
# @desc : 本代码未经授权禁止商用
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("文件被修改了 %s" % event.src_path)

    def on_created(self, event):
        print("文件被创建了 %s" % event.src_path)


if __name__ == "__main__":
    path = "./"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
