<<<<<<< HEAD
#importing libraries
from tkinter import *
from pytube import YouTube

#creating a GUI using tkinter
root = Tk()
root.geometry('500x300') 
root.resizable(0, 0)
root.title("DataFlair-Youtube video downloader")

# label for the title
Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

# field to enter the link
link = StringVar()

# corrected variable names and placement
Label(root, text="Paste Link Here:", font="arial 15 bold").place(x=16, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                             y=150)

root.mainloop()
=======
#importing libraries
from tkinter import *
from pytube import YouTube

#creating a GUI using tkinter
root = Tk()
root.geometry('500x300')  # corrected the syntax for setting window size
root.resizable(0, 0)
root.title("DataFlair-Youtube video downloader")

# label for the title
Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

# field to enter the link
link = StringVar()

# corrected variable names and placement
Label(root, text="Paste Link Here:", font="arial 15 bold").place(x=16, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                             y=150)

root.mainloop()
>>>>>>> a7f142599a61b4fdf430ed806214de709513b54b
