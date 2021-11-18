import ctypes
import PyHook3
import pythoncom
import pyhk
import win32con
import win32gui
import sys

# pyhk对象
hotKey = pyhk.pyhk()
# 摸鱼窗口列表
play = []
# 工作窗口
work = 0
# 记录摸鱼窗口更改显示状态目标
show = win32con.SW_HIDE

# 清除摸鱼窗口列表
def cleanPlay():
    global play
    play = []

# 添加前景窗口到摸鱼窗口列表
def addPlay():
    global play
    play.append(win32gui.GetForegroundWindow())

# 将前景窗口设为工作窗口
def updateWork():
    global work
    work = win32gui.GetForegroundWindow()

# 隐藏/显示摸鱼窗口，并将工作窗口最大化显示
def hide():
    global show
    # 遍历摸鱼窗口，将其隐藏/显示
    for window in play:
        # 如果摸鱼与工作窗口重合则优先执行工作窗口职能
        if window == work:
            continue
        # 判断窗口是否存在
        if win32gui.IsWindow(window):
            win32gui.ShowWindow(window, show)
    # 刷新show
    if show == win32con.SW_HIDE:
        show = win32con.SW_SHOW
        # 如果刚刚隐藏了摸鱼窗口，则最大化工作窗口
        if win32gui.IsWindow(work):
            win32gui.ShowWindow(work, win32con.SW_MAXIMIZE)
        else:
            # 窗口如果不存在则刷新
            updateWork()
    else:
        show = win32con.SW_HIDE

# 初始化摸鱼窗口队列与工作窗口
cleanPlay()
updateWork()

# 绑定快捷键
hotKey.addHotkey(['Alt', 'N'], cleanPlay)
hotKey.addHotkey(['Alt', 'V'], addPlay)
hotKey.addHotkey(['Alt', 'B'], updateWork)
hotKey.addHotkey(['Alt', 'C'], hide)
hotKey.addHotkey(['Alt', 'X'], sys.exit)

# 开始运行
hotKey.start()