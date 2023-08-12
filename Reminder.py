import time
from tkinter import *
from tkinter.messagebox import showinfo, showerror

from PIL import Image, ImageTk
from plyer import notification

root= Tk()
root.title("Notification app")
root.geometry("600x400")
img=Image.open('notify-label.png')
tk_image = ImageTk.PhotoImage(img)


# get info
def get_info():
    get_title=title.get()
    get_msg=msg.get()
    get_time=time1.get()

    if get_title=="" or get_msg=="" or get_time=="":
        showerror("Alert","All fields must be filled")
    else:
        int_time=int(float(get_time))
        min_to_sec =int_time * 60
        showinfo("Reminder set","set notification")
        root.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,message=get_msg,app_name="Reminder",app_icon="Download.ico",toast=True,timeout=10)

img_label= Label(root, image=tk_image).grid()

# label1

title_label=Label(root,text="Title for reminder ")
title_label.place(x=12 , y=70)

# entry 1
title=Entry(root, width="25")
title.place(x=123,y=70)

# label 2
msg_label=Label(root,text="Message",font=("poppins",10))
msg_label.place(x=12,y=120)

# entry 2
msg=Entry(root,width="40")
msg.place(x=123,y=120,height=30)

# label 3
time_label=Label(root,text="Set time",font=("poppins",10))
time_label.place(x=12,y=175)

# Entry 3
time1=Entry(root,width=5)
time1.place(x=123,y=175)

# label 4
time_min_label=Label(root,text="mins",font=("poppins",10))
time_min_label.place(x=175,y=180)

# Button
button= Button(root,text="Set",font="poppins",fg="#ffffff",bg="#528DFF",width=20,relief="raised",command=get_info)
button.place(x=170,y=230)

root.resizable(0,0)
root.mainloop()



