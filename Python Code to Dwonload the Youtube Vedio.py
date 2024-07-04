# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

import os
import math
import random
import smtplib

# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():

	head_label = Label(root, text="YouTube Video Downloader Using Tkinter",padx=15,pady=15,font="SegoeUI 14",bg="palegreen1",fg="red")
	head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)

	link_label = Label(root,text="YouTube link :",bg="salmon",pady=5,padx=5)
	link_label.grid(row=2,column=0,pady=5,padx=5)

	root.linkText = Entry(root,width=35,textvariable=video_Link,font="Arial 14")
	root.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)

	destination_label = Label(root,text="Destination :",bg="salmon",pady=5,	padx=9)
	destination_label.grid(row=3,column=0,pady=5,padx=5)


	root.destinationText = Entry(root,width=27,textvariable=download_Path,font="Arial 14")
	root.destinationText.grid(row=3,column=1,pady=5,padx=5)


	browse_B = Button(root,text="Browse",command=Browse,width=10,bg="bisque",relief=GROOVE)
	browse_B.grid(row=3,column=2,pady=1,padx=1)

	Download_B = Button(root,text="Download Video",command=Download,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
	Download_B.grid(row=4,column=1,pady=20,padx=20)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
	# Presenting user with a pop-up for
	# directory selection. initialdir
	# argument is optional Retrieving the
	# user-input destination directory and
	# storing it in downloadDirectory
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	# Displaying the directory in the directory
	# textbox
	download_Path.set(download_Directory)

# Defining Download() to download the video


def Download():
    def otp():
        def verify():
            if(OTP1 == E2.get()):
                #print("Verified")
                # getting user-input Youtube Link
                Youtube_link = video_Link.get()

                # select the optimal location for
                # saving file's
                download_Folder = download_Path.get()

                # Creating object of YouTube()
                getVideo = YouTube(Youtube_link)

                # Getting all the available streams of the
                # youtube video and selecting the first
                # from the
                videoStream = getVideo.streams.first()

                # Downloading the video to destination
                # directory
                videoStream.download(download_Folder)

                # Displaying the message
                messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n"+ download_Folder)
                root1.destroy()
                root.destroy()
            else:
                print("Check your OTP again")
                
        OTP1=str(random.randint(1000,9999))
        s=smtplib.SMTP_SSL("smtp.gmail.com",465)
        s.login('shilpakondhalkar011@gmail.com',"rkntvzjepmmvjtlp")
        send_to=E1.get()
        s.sendmail('shilpakondhalkar011@gmail.com',send_to,OTP1)
        l2=Label(root1,text="Enter OTP:",font=('Calibri',10,'bold'),bg="salmon")
        l2.place(x=20,y=50)
        E2=Entry(root1,font=('Calibri',10,'bold'))
        E2.place(x=110,y=50)
        B2=Button(root1,text='Submit',command=verify,font=('Calibri',8,'bold'),bg="bisque",relief=GROOVE)
        B2.place(x=260,y=50)
          
    
    #accepting sender email
    root1=tk.Tk()
    root1.geometry("400x100")
    root1.title("Email details")
    root1.config(background="PaleGreen1")
    l1=Label(root1,text="Enter email id:",font=('Calibri',10,'bold'),bg="salmon")
    l1.place(x=20,y=20)
    E1=Entry(root1,font=('Calibri',10,'bold'))
    E1.place(x=110,y=20)
    B1=Button(root1,text='Send OTP',command=otp,font=('Calibri',8,'bold'),bg="bisque",relief=GROOVE)
    B1.place(x=260,y=20)
                   
            

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()
