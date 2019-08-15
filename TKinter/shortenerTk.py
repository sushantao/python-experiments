from tkinter import *
import requests

window = Tk()
window.geometry("400x400")
window.title("URL Shortener")

label1 = Label(window,text="Welcome to Tkinter",font=("arial",16,"bold"))
label1.pack()

label2 = Label(window,text="Enter the URL:",font=("arial",12,"bold")).place(x=10,y=100)

name = StringVar()
entry_box = Entry(window, textvariable=name, width=25, bg="lightgreen").place(x=150,y=105)


def do_it():

    try:
        test = requests.get('https://tinyurl.com/api-create.php?url=' + str(name.get()))
        print(test.text)

    except TimeoutError:
        print("Server request time out")
    except ConnectionError:
        print("Connection error")


enter = Button(window,text="Enter",fg="white",bg="brown",font=("arial",12,"bold"),command=do_it)
enter.place(x=200,y=130)
window.mainloop()




