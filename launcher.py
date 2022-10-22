import os
from tkinter import *
import configparser
from webbrowser import get
import time as t
import wget
import zipfile

#基础设置
vision = "1.0.0"
gcvision = "3155"
yspath = ""


#日志反馈
log = open("log.txt","w")
def feedback(back):
    output = t.asctime() + str(back)
    print(output)
    log.write(output+"\n")
    


#读取配置项
config = configparser.ConfigParser()
config.read("./config/config.ini", encoding="utf-8")
feedback(config.sections())
feedback(config.options("AzheLauncher"))
feedback(config.has_option("AzheLauncher","yspath"))


#检测yspath是否存在
if config.has_option("AzheLauncher", "yspath") == True:
    yspath = config["AzheLauncher"]["yspath"]


#窗口设置
window = Tk()
window.title("AzheLauncher")
window.geometry("1000x600")
window.iconbitmap('./res/photos/azhehead.ico')


#标题设置
title = Label(window, text="欢迎使用AzheLauncher")
title.grid(column=0, row=0)


#路径基础
patht = Entry(window, width=10)
patht.grid(column=0, row=1)


#路径设置
patht.insert(END, yspath)
def setpath():
    config.set("AzheLauncher", "yspath", str(patht.get()))
    config.write(open("./config/config.ini", "w"))
    feedback("path set!")
    feedback(config.options("AzheLauncher"))

startbtn = Button(window, text="设置", command=setpath)
startbtn.grid(column=2, row=1)


#启动
def openys():
    os.system(yspath+"\genshinimpact.exe")
    os.system(yspath+"\yuanshen.exe")
startbtn = Button(window, text="启动", command=openys)
startbtn.grid(column=3, row=1)


#下载割草机
def downloadgc():
    
    feedback("zipstart")

    fz = zipfile.ZipFile(./res/grasscutter/Azhe3155.zip, 'r')
    for file in fz.namelist():
        fz.extract(file, ./res/grasscutter/Azhe3155)  
    feedback("zip done")

startbtn = Button(window, text="下载割草机", command=downloadgc)
startbtn.grid(column=0, row=2)


#开始
window.mainloop()