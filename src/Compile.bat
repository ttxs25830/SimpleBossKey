@echo off
pyinstaller -F -w main.py
copy dist\main.exe ..\dist\SBK.exe
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__
del main.spec /-q