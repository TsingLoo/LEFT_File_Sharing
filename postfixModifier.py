import os
from tkinter import *
from tkinter import filedialog


targetFolderPath = ""

def setTargetFolder():
    global  targetFolderPath
    targetFolderPath = filedialog.askdirectory();
    L4.config(text = targetFolderPath,fg="blue")
    print(targetFolderPath)

def checkPostfix():

    if not E1.get():
        L3.config(text = "plz fill blank", fg="red")
        return

    if not E2.get():
        L3.config(text = "plz fill blank", fg="red")
        return

    if not E1.get()[0] == ".":
        E1.clear()
        L3.config(text="postfix starts with .", fg="red")
        return

    if not E2.get()[0] == ".":
        E2.clear()
        L3.config(text="postfix starts with .", fg="red")
        return

    changePostfix(E1.get(),E2.get())


def changePostfix(rawPostfix,targetPostfix):
    global  targetFolderPath
    fileNameList = os.listdir(targetFolderPath)
    for fileName in fileNameList:
        portion = os.path.splitext(fileName)
        if portion[1] == rawPostfix:
            newFileName = portion[0] + targetPostfix
            filepath = os.path.join(targetFolderPath,fileName)
            newFileName =  os.path.join(targetFolderPath,newFileName)
            os.rename(filepath,newFileName)

    L3.config(text="Done", fg="green")



top = Tk()
top.title ( "PostfixModifier")
top.geometry("260x110+10+10")
L1 = Label(top, text="Source Postfix:")
L1.grid(row=0,column= 0)
L2 = Label(top, text="Target Postfix:")
L2.grid(row=1,column= 0)
L3 = Label(top, text ="")
L3.grid(row=3,column= 1)
L4 = Label(top, text ="")
L4.grid(row=2,column= 1)

E1 = Entry(top, bd = 2,)
E1.grid(row=0,column= 1)
E2= Entry(top, bd = 2)
E2.grid(row=1,column= 1)

B1 = Button(top,command=checkPostfix,text="Do it")
B1.grid(row=3,column=0)
B2 = Button(top,command=setTargetFolder,text="Set Folder")
B2.grid(row=2,column=0)
top.mainloop()












