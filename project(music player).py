import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *
root=Tk()
root.minsize(300,300)
listofsongs=[]

v=StringVar()
songlabel=Label(root,textvariable=v,width=35)

index=0
def playsong(event):
    global index
    index=0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def pausesong(event):
    global index
    pygame.mixer.music.load(listofsongs[index])

    updatelabel()

def unpausesong(event):

    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    updatelabel()

def setvolume(val):
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)




def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
   # return songname


def directorychooser():
    directory=askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.pause()
    pygame.mixer.music.unpause()
    #pygame.mixer.music.set_volume()

directorychooser()



label=Label(root,text="music player")
label.pack()
listbox=Listbox(root)
listbox.pack()
listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()

playbutton=Button(root,text="play song",foreground="orange")
playbutton.pack()
nextbutton=Button(root,text="next song",foreground="green")
nextbutton.pack()
previousbutton=Button(root,text="last song",foreground="green")
previousbutton.pack()
pausebutton=Button(root,text="pause song",foreground="yellow")
pausebutton.pack()
unpausebutton=Button(root,text="unpause song",foreground="yellow")
unpausebutton.pack()


stopbutton=Button(root,text="stop song",foreground="red")
stopbutton.pack()
#volumebutton=Button(root,text="volume up")
#volumebutton.pack()
scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=setvolume,foreground="blue")
scale.pack()

playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
pausebutton.bind("<Button-1>",pausesong)
unpausebutton.bind("<Button-1>",unpausesong)
stopbutton.bind("<Button-1>",stopsong)
#volumebutton.bind("<Button-1>",setvolume)
#scale.bind("<Button-1>",setvolume)
songlabel.pack()



root.mainloop()