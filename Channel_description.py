from tkinter import *
#from pyyoutube import Api
#from urllib.request import urlopen

import urllib.request
import json


key=""
#api=Api(key)

def channel_data():
    name=e1.get()
    data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
    #print("result code :",str(data.getCode()))
    sub=json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    total_view=json.loads(data)['items'][0]["statistics"]["viewCount"]
    total_videos=json.loads(data)['items'][0]["statistics"]["videoCount"]
    l2.config(text=sub)
    l4.config(text=total_view)
    l6.config(text=total_videos)





root=Tk()
root.geometry("500x200")
ch_name=StringVar()
e1=Entry(root,textvariable=ch_name)
e1.grid(row=1,column=2)
b1=Button(root,text="DETAILS",command=channel_data)
b1.grid(row=2,column=2)


l1=Label(root,text="Total number of subscribers",font="times 15 bold")
l1.grid(row=4,column=1)
l2=Label(root,text="",font="times 15 bold")
l2.grid(row=4,column=3)

l3=Label(root,text="Total number of views",font="times 15 bold")
l3.grid(row=6,column=1)
l4=Label(root,font="times 15 bold")
l4.grid(row=6,column=3)

l5=Label(root,text="Total number of videos",font="times 15 bold")
l5.grid(row=8,column=1)
l6=Label(root,font="times 15 bold")
l6.grid(row=8,column=3)

root.mainloop()

