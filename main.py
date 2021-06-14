import pyautogui
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import os
import sys

win = tkinter.Tk()
win.title('EPIC RPG AUTOTYPE')
win.maxsize(410, 108)
win.minsize(410, 108)
win.attributes('-topmost', 1)

cmd = 10
sec = 3
btnw = 8
isStop = False
isStart = False
def start():
    global isStart
    if isStart is True:
        print('執行中')
        return

    if not cmdbox.get() == '' and not secbox.get() == '':
        t = threading.Thread(target=box)
        t.start()
        isStart = True

    if not cmdbox2.get() == '' and not secbox2.get() == '':
        t2 = threading.Thread(target=box2)
        t2.start()

    if not cmdbox3.get() == '' and not secbox3.get() == '':
        t3 = threading.Thread(target=box3)
        t3.start()

    if not cmdbox4.get() == '' and not secbox4.get() == '':
        t4 = threading.Thread(target=box4)
        t4.start()

def stop():
    global isStop
    isStop = True

def reset():
    cmdbox.set('')
    cmdbox2.set('')
    cmdbox3.set('')
    cmdbox4.set('')

    secbox.set('')
    secbox2.set('')
    secbox3.set('')
    secbox4.set('')

def box():
    sec = int(secbox.get())
    p = sec
    count = 0
    while count < sec:
        global isStop
        global isStart
        if isStop is True:
            secbox.set(sec)
            isStop = False
            isStart = False
            count = 0
            break

        time.sleep(1)
        count += 1
        p -= 1
        secbox.set(p)

        if count == sec:
            count = 0
            p = sec
            pyautogui.typewrite(cmdbox.get(), interval=0.02)
            pyautogui.press('enter')

def box2():
    sec = int(secbox2.get())
    p = sec
    count = 0
    while count < sec:
        global isStop
        global isStart
        if isStop is True:
            secbox2.set(sec)
            isStop = False
            isStart = False
            count = 0
            break

        time.sleep(1)
        count += 1
        p -= 1
        secbox2.set(p)
        if count == sec:
            count = 0
            p = sec
            pyautogui.typewrite(cmdbox2.get(), interval=0.03)
            pyautogui.press('enter')

def box3():
    sec = int(secbox3.get())
    p = sec
    count = 0
    while count < sec:
        global isStop
        global isStart
        if isStop is True:
            secbox3.set(sec)
            isStop = False
            isStart = False
            count = 0
            break

        time.sleep(1)
        count += 1
        p -= 1
        secbox3.set(p)
        if count == sec:
            count = 0
            p = sec
            pyautogui.typewrite(cmdbox3.get(), interval=0.03)
            pyautogui.press('enter')

def box4():
    sec = int(secbox4.get())
    p = sec
    count = 0
    while count < sec:
        global isStop
        global isStart
        if isStop is True:
            secbox4.set(sec)
            isStop = False
            isStart = False
            count = 0
            break

        time.sleep(1)
        count += 1
        p -= 1
        secbox4.set(p)
        if count == sec:
            count = 0
            p = sec
            pyautogui.typewrite(cmdbox4.get(), interval=0.03)
            pyautogui.press('enter')

def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False

def label(row, column, text):
    lb = ttk.Label(win, text=text)
    lb.grid(row=row, column=column)

def entry(row, column, width, strvar):
    cmdEntry = ttk.Entry(win,width=width)
    cmdEntry.grid(row=row, column=column)
    cmdEntry.configure(textvariable=strvar)

def entryNumber(row, column, width, strvar):
    vcmd = (win.register(validate), '%P')
    cmdEntry = ttk.Entry(win,width=width, validate='key', validatecommand=vcmd)
    cmdEntry.grid(row=row, column=column)
    cmdEntry.configure(textvariable=strvar)

def button(row, column, text, width, command):
    btn = ttk.Button(win, text=text)
    btn.grid(row=row, column=column)
    btn.configure(width=width, command=command)

#GUI
#Label object
label(0,0,'Command')
label(1,0,'Command')
label(2,0,'Command')
label(3,0,'Command')

label(0,2,'sec')
label(1,2,'sec')
label(2,2,'sec')
label(3,2,'sec')

#command entrybox
cmdbox = tkinter.StringVar()
entry(0,1,cmd, cmdbox)

cmdbox2 = tkinter.StringVar()
entry(1,1,cmd, cmdbox2)

cmdbox3 = tkinter.StringVar()
entry(2,1,cmd, cmdbox3)

cmdbox4 = tkinter.StringVar()
entry(3,1,cmd, cmdbox4)

#Sec entrybox
secbox = tkinter.StringVar()
entryNumber(0,3,sec, secbox)

secbox2 = tkinter.StringVar()
entryNumber(1,3,sec, secbox2)

secbox3 = tkinter.StringVar()
entryNumber(2,3,sec, secbox3)

secbox4 = tkinter.StringVar()
entryNumber(3,3,sec, secbox4)

#Button object
button(0,4,'START',btnw, start)
button(1,4,'RESET',btnw, reset)
button(2,4,'STOP',btnw, stop)
button(3,4,'GITHUB',btnw, None)

#image lable
photo = ImageTk.PhotoImage(file='rpg.gif')
imglb = ttk.Label(win,image=photo)
imglb.grid(row=0, column=5,rowspan=100,padx=4, pady=4)

win.mainloop()
