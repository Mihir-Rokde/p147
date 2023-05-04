from tkinter import*
root=Tk()
root.title("Ascii encryption")
root.geometry("400x400")
root.configure(bg="light green")

textbox=Entry(root)
textbox.place(relx=0.5,rely=0.4,anchor=CENTER)
label=Label(root,text="name in ascii : ",bg="yellow",fg="black")
label2=Label(root,text="encrypted name : ",bg="cyan",fg="black")
def asciiConverter():
    input_word=str(textbox.get())
    for letter in input_word:
        label["text"]+=str(ord(letter))+"  "
        ascii=int(ord(letter))
        encrypted=ascii-1
        label2["text"]+=str(chr(encrypted))
btn=Button(root,text="display the ascii code and encrypted value ",command=asciiConverter,bg="royalblue",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
