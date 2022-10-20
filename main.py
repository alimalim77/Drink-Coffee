from tkinter import *
from PIL import Image, ImageTk
import time
import notification

root = Tk()
root.geometry("550x550")
root.title("Take Caffeine Notification")
root.resizable(False,False)


main = LabelFrame(root,padx= 100, pady = 7, borderwidth=3, relief="raised")
main.grid(row=0,column=1,padx=20,pady=60)

text_label = Label(main,text="Drinking Coffee Reminder", font=("comic Sans ms",14,"bold"),bg="#C4C4C4")
text_label.grid(row=0,column=0,padx=20,pady=10)

image = Image.open("dc.jpg")
img = image.resize((150,150))
my_img = ImageTk.PhotoImage(img)




img_label = Label(main,image=my_img)
img_label.grid(row = 1,column = 0, pady=10,padx=20)

inp = Entry(main,width=30)
inp.insert(0,"Enter Time: ")
inp.grid(row=10,column=0,padx=30)

def bar():
    val = int(inp.get())
    while True:
        time.sleep(val)
        notification.Notification()
    
button = Button(main, text="SET", bg="#C4C4C4", pady=16,padx=40,borderwidth=3,relief=SOLID,command=bar)
button.grid(row=12,column=0,pady=10)

root.mainloop()