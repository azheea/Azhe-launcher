@ECHO off
echo 开始编译启动器，请稍等
pyinstaller -F -i .\res\photos\azhehead.ico launcher.py
echo 已经编译完成，输出到./dist文件夹
del Launcher.exe
copy ./dist/launcher.exe ./launcher.exe
pause