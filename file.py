# Importing libraries
from tkinter import *
from pytube import YouTube

# Creating the gui
root = Tk()
root.geometry('500x300') 
root.resizable(0, 0) 
root.title('YouTube Video Downloader') #Title of the program
root.configure(bg='#AACDE2') # Background

# This is the title of the program
Label(root, text='Download your videos', font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)
link = StringVar()

# With this we request to the user the link of the youtube video
Label(root, text='Paste link:', font='arial 12', bg='#AACDE2').place(x=190, y=90)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

# The following function allows us to download youtube video with the class from pytube librarie
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='DONE', font='arial 13 bold', bg='#AACDE2', fg='#B57199').place(x=180, y=240)  
    

# The following code line is for a button to download the video
Button(root,text='DOWNLOAD', font='arial 13 bold italic', bg='#B57199', padx=2, command=Downloader).place(x=180, y=180)
root.mainloop()