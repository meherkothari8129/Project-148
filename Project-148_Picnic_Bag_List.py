from tkinter import *
import random
root=Tk()
root.title("Picnic Items")
root.geometry("600x600")

listdisplay=Label(root)
randomvalue=Label(root)
items=["Bottle", "Tiffin", "ID Card", "Chocolates", "Chips", "Tickets", "Hanky"]
listdisplay["text"]="Listed items - " + str(items)
disclaimer = Label(root, text="DISCLAIMER: The item range starts from 0 in a list, so item 0 is actually the first item, and item 6 is the last item.")
def genrandomnum():
    random_num1 = random.randint(0, len(items)-1)
    randomvalue["text"]="Put item number " + str(random_num1) + " in the bag."

button1 = Button(root, text="Which item to put in the bag?", command=genrandomnum, fg="white", bg="orange")
button1.place(relx=0.5, rely=0.4, anchor=CENTER)
listdisplay.place(relx=0.5, rely=0.2, anchor=CENTER)
randomvalue.place(relx=0.5, rely=0.6, anchor=CENTER)
disclaimer.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()