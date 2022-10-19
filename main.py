from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("550x550")
root.title("Drink Water Notification")
#root.resizable(False,False)





main = LabelFrame(root,padx= 100, pady = 7, borderwidth=3, relief="raised")
main.grid(row=0,column=1,padx=20,pady=60)

text_label = Label(main,text="Drinking Water reminder", font=("comic Sans ms",14,"bold"),bg="#C4C4C4")
text_label.grid(row=0,column=20,padx=20,pady=10)

image = ImageTk.PhotoImage(Image.open("dc.jpg"))

img_label = Label(main,image=image)
img_label.grid(row = 1,column = 0, pady=10,padx=20)


root.mainloop()