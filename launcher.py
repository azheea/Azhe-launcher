import os
from tkinter import *
import configparser
from webbrowser import get
import time as t
import wget
import zipfile
from tkinter import messagebox




#基础设置
vision = "1.0.1"
gcvision = "3155"
yspath = ""


#日志反馈
log = open("log.txt","w")
def feedback(back):
    output = t.asctime() +":"+ str(back)
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
window.geometry("600x250")
window.iconbitmap('./azhehead.ico')



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
    feedback("path set:"+yspath)
    feedback(config.options("AzheLauncher"))

startbtn = Button(window, text="设置", command=setpath)
startbtn.grid(column=2, row=1)



#启动
def openys():
    grasscutterpath = os.path.dirname(sys.argv[0])
    feedback("start grasscutter in" + grasscutterpath)
    os.popen(grasscutterpath + "\grasscutter\启动.bat")
    messagebox.showinfo("提示","请等待割草机完全启动后在点击确定")
    feedback("start genshin in" + yspath)
    os.popen(yspath + "\genshinimpact.exe")
    os.popen(yspath + "\yuanshen.exe")

startbtn = Button(window, text="启动", command=openys)
startbtn.grid(column=4, row=1)



#结束进程
def openys():
    os.system("taskkill /f /im java.exe")
    os.system("taskkill /f /im mongod.exe")
    os.system("taskkill /f /im mitmdump.exe")
    os.system("taskkill /f /im yuanshen.exe")
    os.system("taskkill /f /im genshinimpact.exe")
startbtn = Button(window, text="结束", command=openys)
startbtn.grid(column=6, row=1)






#下载割草机

#从github下载
def downloadgc():
    messagebox.showinfo("提示", "即将从github下载割草机，请耐心等待，出现未响应为正常现象")
    feedback("downloadgc start")
    wget.download("https://github.com/azheea/grasscutter-azhe/releases/download/Azhe3155/Azhe3155.zip","./grasscutter")
    feedback("downloadgc done")
    messagebox.showinfo("提示", "下载完成，请手动解压")
    
startbtn = Button(window, text="下载割草机(自github)", command=downloadgc)
startbtn.grid(column=0, row=2)

#从github下载
def downloadgc():
    messagebox.showinfo("提示", "即将从啊这云盘下载割草机，请耐心等待，出现未响应为正常现象")
    feedback("downloadgc start")
    wget.download("http://117.50.186.115:6010/api/alien/download/ceeaf2dd-435d-471e-6d5b-37b09ec6573c/Azhe3155.zip","./grasscutter")
    feedback("downloadgc done")
    messagebox.showinfo("提示", "下载完成，请手动解压")
    
startbtn = Button(window, text="下载割草机(自啊这的服务器，不建议使用)", command=downloadgc)
startbtn.grid(column=1, row=2)




#开始
window.mainloop()