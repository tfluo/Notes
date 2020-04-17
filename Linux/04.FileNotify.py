# !/usr/bin/env python
# encoding:utf-8

# https://blog.csdn.net/luopeiyuan1990/article/details/88861691

# Event Name	Is an Event	Description
# IN_ACCESS	Yes	file was accessed.
# IN_ATTRIB	Yes	metadata changed.
# IN_CLOSE_NOWRITE	Yes	unwrittable file was closed.
# IN_CLOSE_WRITE	Yes	writtable file was closed.
# IN_CREATE	Yes	file/dir was created in watched directory.
# IN_DELETE	Yes	file/dir was deleted in watched directory.
# IN_DELETE_SELF	Yes	自删除，即一个可执行文件在执行时删除自己
# IN_DONT_FOLLOW	No	don’t follow a symlink (lk 2.6.15).
# IN_IGNORED	Yes	raised on watched item removing. Probably useless for you, prefer instead IN_DELETE*.
# IN_ISDIR	No	event occurred against directory. It is always piggybacked to an event. The Event structure automatically provide this information (via .is_dir)
# IN_MASK_ADD	No	to update a mask without overwriting the previous value (lk 2.6.14). Useful when updating a watch.
# IN_MODIFY	Yes	file was modified.
# IN_MOVE_SELF	Yes	自移动，即一个可执行文件在执行时移动自己
# IN_MOVED_FROM	Yes	file/dir in a watched dir was moved from X. Can trace the full move of an item when IN_MOVED_TO is available too, in this case if the moved item is itself watched, its path will be updated (see IN_MOVE_SELF).
# IN_MOVED_TO	Yes	file/dir was moved to Y in a watched dir (see IN_MOVE_FROM).
# IN_ONLYDIR	No	only watch the path if it is a directory (lk 2.6.15). Usable when calling .add_watch.
# IN_OPEN	Yes	file was opened.
# IN_Q_OVERFLOW	Yes	event queued overflowed. This event doesn’t belongs to any particular watch.
# IN_UNMOUNT	Yes	宿主文件系统被 umount
 
 
import os
from pyinotify import WatchManager, Notifier, \
    ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY, IN_CLOSE_WRITE
 
 
def call_back(file):
    print("call back at file:{}".format(file))
 
 
class EventHandler(ProcessEvent):
    """事件处理"""
    def __init__(self,fun):
        self.fun = fun
 
    def process_IN_CREATE(self, event):
        print(
            "Create file: %s " % os.path.join(event.path, event.name))
 
    def process_IN_DELETE(self, event):
        print(
            "Delete file: %s " % os.path.join(event.path, event.name))
 
    def process_IN_MODIFY(self, event):
        print(
            "Modify file: %s " % os.path.join(event.path, event.name))
 
    def process_IN_CLOSE_WRITE(self, event):
        print(
            "Close Write file: %s " % os.path.join(event.path, event.name))
        if self.fun != None:
            self.fun(os.path.join(event.path, event.name))
 
 
def FSMonitor(path='.',fun=None):
    wm = WatchManager()
    mask = IN_DELETE | IN_CREATE | IN_MODIFY | IN_CLOSE_WRITE
    notifier = Notifier(wm, EventHandler(fun))
    wm.add_watch(path, mask, rec=True)
    print('now starting monitor %s' % (path))
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break
 
 
if __name__ == "__main__":
    FSMonitor(path=".",fun=call_back)
