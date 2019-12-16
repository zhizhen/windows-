# -*- coding: utf-8 -*-

import tkinter as tk
from pynput.keyboard import Key, Listener

num1=2
num2=2
num3=2
num4=2
num5=2

ck = tk.Tk(className='yeah')
ck.geometry('200x200+0+0')
#隐藏窗体边框
ck.overrideredirect(True)
#置顶
ck.wm_attributes('-topmost',1)
#透明色
ck.wm_attributes('-transparentcolor','black')
#窗口背景色
bg=tk.Frame(ck,bg='black',width=400,height=400)
bg.pack()

kaiguan = tk.Label(ck,bg='black', text='OFF', fg='#A52A2A', width=10, height=1, font=("Arial", 20, 'bold'))
kaiguan.place(x=32,y=0)
#——第一列标签——
#枪械种类
zhonglei1=tk.Label(ck,bg='black',text='  Type:',anchor='w',fg='#8B4513',width=9,height=1,font=("Times new roman", 15,'bold'))
zhonglei1.place(x=0, y=40)
#枪械
name1=tk.Label(ck,bg='black',text='  Name:',anchor='w',fg='#8B4513',width=9,height=1,font=("Times new roman", 15,'bold'))
name1.place(x=0, y=70)
#配件
peijian1=tk.Label(ck,bg='black',text='  part:',anchor='w',fg='#8B4513',width=9,height=1,font=("Times new roman", 15,'bold'))
peijian1.place(x=0,y=100)
#连狙枪械
ljname1=tk.Label(ck,bg='black',text='  Auto:',anchor='w',fg='#2F4F4F',width=9,height=1,font=("Times new roman", 15,'bold'))
ljname1.place(x=0, y=130)
#连狙配件
ljpeijian1=tk.Label(ck,bg='black',text='  part:',anchor='w',fg='#2F4F4F',width=9,height=1,font=("Times new roman", 15,'bold'))
ljpeijian1.place(x=0, y=160)
#——第二列标签——
#枪械种类
zhonglei=tk.Label(ck,bg='black',text='-',fg='#8B4513',width=6,height=1,font=("Times new roman", 15,'bold'))
zhonglei.place(x=115, y=40)
#枪械
name=tk.Label(ck,bg='black',text='-',fg='#8B4513',width=6,height=1,font=("Times new roman", 15,'bold'))
name.place(x=115, y=70)
#配件
peijian=tk.Label(ck,bg='black',text='-',fg='#8B4513',width=6,height=1,font=("Times new roman", 15,'bold'))
peijian.place(x=115,y=100)
#连狙枪械
ljname=tk.Label(ck,bg='black',text='-',fg='#2F4F4F',width=6,height=1,font=("Times new roman", 15,'bold'))
ljname.place(x=115,y=130)
#连狙配件
ljpeijian=tk.Label(ck,bg='black',text='-',fg='#2F4F4F',width=6,height=1,font=("Times new roman", 15,'bold'))
ljpeijian.place(x=115,y=160)

#开关
def dianjikg():
    if kaiguan["text"] == "OFF":
        kaiguan["text"] = "ON"
        zhonglei["text"] = "5.56"
        name["text"] = "M4"
        peijian["text"] = "0"
        ljname["text"] = "SKS"
        ljpeijian["text"] = "0"
    else:
        kaiguan["text"] = "OFF"
        zhonglei["text"] = "-"
        name["text"] = "-"
        peijian["text"] = "-"
        ljname["text"] = "-"
        ljpeijian["text"] = "-"
#种类
def panduanzlup():
    #print('2')
    if zhonglei["text"] == "others":
        zhonglei["text"] = "5.56"
        name["text"] = "M4"
        peijian["text"] = "0"
    elif zhonglei["text"] == "5.56":
        zhonglei["text"] = "7.62"
        name["text"] = "AK"
        peijian["text"] = "0"
    elif zhonglei["text"] == "7.62":
        zhonglei["text"] = "others"
        name["text"] = "111"
        peijian["text"] = "0"
def panduanzldown():
    if zhonglei["text"] == "others":
        zhonglei["text"] = "7.62"
        name["text"] = "AK"
        peijian["text"] = "0"
    elif zhonglei["text"] == "7.62":
        zhonglei["text"] = "5.56"
        name["text"] = "M4"
        peijian["text"] = "0"
    elif zhonglei["text"] == "5.56":
        zhonglei["text"] = "others"
        name["text"] = "111"
        peijian["text"] = "0"
#枪械
def panduanqxup():
    if zhonglei["text"] == "5.56":
        if name["text"] == "M4":
            name["text"] = "Scar"
            peijian["text"] = "0"
        elif name["text"] == "Scar":
            name["text"] = "QBZ"
            peijian["text"] = "0"
        elif name["text"] == "QBZ":
            name["text"] = "M4"
            peijian["text"] = "0"
    elif zhonglei["text"] == "7.62":
        if name["text"] == "33":
            name["text"] = "AK"
            peijian["text"] = "0"
        elif name["text"] == "AK":
            name["text"] = "22"
            peijian["text"] = "0"
        elif name["text"] == "22":
            name["text"] = "33"
            peijian["text"] = "0"
    elif zhonglei["text"] == "others":
        if name["text"] == "333":
            name["text"] = "111"
            peijian["text"] = "0"
        elif name["text"] == "111":
            name["text"] = "222"
            peijian["text"] = "0"
        elif name["text"] == "222":
            name["text"] = "333"
            peijian["text"] = "0"
def panduanqxdown():
    if zhonglei["text"] == "5.56":
        if name["text"] == "M4":
            name["text"] = "QBZ"
            peijian["text"] = "0"
        elif name["text"] == "QBZ":
            name["text"] = "Scar"
            peijian["text"] = "0"
        elif name["text"] == "Scar":
            name["text"] = "M4"
    elif zhonglei["text"] == "7.62":
        if name["text"] == "33":
            name["text"] = "22"
            peijian["text"] = "0"
        elif name["text"] == "22":
            name["text"] = "AK"
            peijian["text"] = "0"
        elif name["text"] == "AK":
            name["text"] = "33"
            peijian["text"] = "0"
    elif zhonglei["text"] == "others":
        if name["text"] == "333":
            name["text"] = "222"
            peijian["text"] = "0"
        elif name["text"] == "222":
            name["text"] = "111"
            peijian["text"] = "0"
        elif name["text"] == "111":
            name["text"] = "333"
            peijian["text"] = "0"
#配件
def panduanpjup():
    if peijian["text"] == "1":
        peijian["text"] = "2"
    elif peijian["text"] == "2":
        peijian["text"] = "0"
    elif peijian["text"] == "0":
        peijian["text"] = "1"
def panduanpjdown():
    if peijian["text"] == "1":
        peijian["text"] = "0"
    elif peijian["text"] == "0":
        peijian["text"] = "2"
    elif peijian["text"] == "2":
        peijian["text"] = "1"
#连狙
def panduanljup():
    ljpeijian["text"] = "0"
    if ljname["text"] == "Mini14":
        ljname["text"] = "SKS"
    elif ljname["text"] == "SKS":
        ljname["text"] = "SLR"
    elif ljname["text"] == "SLR":
        ljname["text"] = "Mini14"
def panduanljdown():
    ljpeijian["text"] = "0"
    if ljname["text"] == "Mini14":
        ljname["text"] = "SLR"
    elif ljname["text"] == "SLR":
        ljname["text"] = "SKS"
    elif ljname["text"] == "SKS":
        ljname["text"] = "Mini14"
#连狙配件
def panduanljpjup():
    if ljpeijian["text"] == "1":
        ljpeijian["text"] = "2"
    elif ljpeijian["text"] == "2":
        ljpeijian["text"] = "0"
    elif ljpeijian["text"] == "0":
        ljpeijian["text"] = "1"
def panduanljpjdown():
    if ljpeijian["text"] == "1":
        ljpeijian["text"] = "0"
    elif ljpeijian["text"] == "0":
        ljpeijian["text"] = "2"
    elif ljpeijian["text"] == "2":
        ljpeijian["text"] = "1"

#监听摁键
def press(key):
    global num1
    global num2
    global num3
    global num4
    global num5
    #种类前置摁键shift_l
    if key == Key.shift_l:
        num1=1
    #配件前置摁键alt_l
    if key == Key.alt_l:
        num2=1
    #连狙前置摁键ctrl_l
    if key == Key.ctrl_l:
        num3 = 1
    #连狙配件前置摁键alt_r
    if key == Key.alt_r:
        num4 = 1
def release(key):
    global num1
    global num2
    global num3
    global num4
    global num5
    #开关摁键
    if key == Key.f12 :
        dianjikg()
    #种类摁键
    if key == Key.shift_l:
        num1=2
    if num1 == 1 and key == Key.f11:
        panduanzlup()
    if num1 == 1 and key == Key.f9:
        panduanzldown()
    #枪械摁键
    if num1 == 2 and num2 == 2 and num3 == 2 and num4 == 2 and key == Key.f11:
        panduanqxup()
    if num1 == 2 and num2 == 2 and num3 == 2 and num4 == 2 and key == Key.f9:
        panduanqxdown()
    #配件摁键
    if key == Key.alt_l:
        num2 = 2
    if num2 == 1 and key == Key.f11:
        panduanpjup()
    if num2 == 1 and key == Key.f9:
        panduanpjdown()
    #连狙
    if key == Key.ctrl_l:
        num3 = 2
    if num3 == 1 and key == Key.f11:
        panduanljup()
    if num3 == 1 and key == Key.f9:
        panduanljdown()
    #连狙配件
    if key == Key.alt_r:
        num4 = 2
    if num4 == 1 and key == Key.f11:
        panduanljpjup()
    if num4 == 1 and key == Key.f9:
        panduanljpjdown()

with Listener( on_press=press, on_release=release) as listener:
    ck.mainloop()
    listener.join()