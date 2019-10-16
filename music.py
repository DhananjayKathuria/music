from tkinter import *
import tkinter
import re
import pygame.mixer
import file_search
from pygame.mixer import Sound
pygame.init()
pygame.mixer.init()
global a
a=1
global files
files=[]
def start():
    c=box.get(ACTIVE)
    for file in files:
        b=file.split("/")
        if c ==b[-1]:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play() 

def stop():
    pygame.mixer.music.stop()
def volume(any):
    d=int(any)
    d=d/100
    pygame.mixer.music.set_volume(d)
def search():
    p=v1.get()
    file_search.set_root("/home/dev/Desktop/")
    global files
    files.clear()
    files=file_search.searchFile(p)
    box.delete(0,END)
    for file in files:
        b=file.split("/")
        b=b[-1]
        if re.match(r".*[mp3]",b):
            box.insert(END,b)
       
            

def pause():
    global a
    a=a*-1
    if a==-1:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
root=Tk()
root.geometry("380x470")
root.configure()
v1=StringVar()
v2=StringVar()
pygame.mixer.music.set_volume(0)
Entry(root,width=35,textvariable=v1).grid()
box=Listbox(root,font=("verdana",16),selectmode=SINGLE)
box.grid()
Button(root,text="Search",width=3,font=("verdana",9),command=search,bg="#4295f5",relief=SUNKEN).grid(row=0,column=1)
Button(root,text="play",width=20,font=("verdana",16),command=start,bg="#4295f5",relief=SUNKEN).grid()
Button(root,text="pause",width=20,font=("verdana",16),command=pause,bg="#4295f5",relief=SUNKEN).grid()
Button(root,text="stop",width=20,font=("verdana",16),command=stop,bg="#4295f5",relief=SUNKEN).grid()
Scale(root,from_=0,to=100,command=volume,bg="#4295f5",relief=SUNKEN).grid(row=1,column=1)
root.mainloop()