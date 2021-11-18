@echo off
:: 编译代码
pyinstaller -F -w main.py
:: 将结果复制出去
copy dist\main.exe ..\dist\SBK.exe
:: 删除中间文件
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__
del main.spec /-q