from tkinter import *
from janela1 import *
from janela2 import *

class Application:
    def __init__(self, master=None):
#container 1
        self.Container1 = Frame(master,bg="red")
        self.Container1.pack()
        self.Container1.place(bordermode=OUTSIDE, height=400, width=400, x=1)
#labels
        self.lbl11= Label(self.Container1, text="Texto1 - Container 1")
        self.lbl11.grid(row=0,column=0, padx= 20, pady=10)
        self.lbl12= Label(self.Container1, text="Texto2 - Container 1")
        self.lbl12.grid(row=1,column=0, padx= 10, pady=10)
        self.lbl13= Label(self.Container1, text="Texto3 - Container 1")
        self.lbl13.grid(row=2,column=0, padx= 10, pady=40)
        self.lbl14= Label(self.Container1, text="Texto4 - Container 1")
        self.lbl14.grid(row=3,column=1, padx= 10, pady=10)
#buttons
        self.btn1 = Button(self.Container1, text="Janela 1", bg="yellow", command=criaJanela1)
        self.btn1.grid(row=4,column=1, pady=20, ipadx=50)

        self.btn2 = Button(self.Container1, text="Janela 2", bg="green", command=criaJanela2)
        self.btn2.grid(row=5,column=1, pady=20, ipadx=50)

#container 2
        self.Container2 = Frame(master,bg="blue")
        self.Container2.pack()
        self.Container2.place(bordermode=OUTSIDE, height=400, width=400, x=400)
#labels
        self.lbl21= Label(self.Container2, text="Texto1 - Container 2")
        self.lbl21.grid(row=0,column=0, padx= 10, pady=10)
        self.lbl22= Label(self.Container2, text="Texto2 - Container 2")
        self.lbl22.grid(row=1,column=0, padx= 10, pady=10)
        self.lbl23= Label(self.Container2, text="Texto3 - Container 2")
        self.lbl23.grid(row=2,column=0, padx= 10, pady=40)
        self.lbl24= Label(self.Container2, text="Texto4 - Container 2")
        self.lbl24.grid(row=3,column=1, padx= 10, pady=10)

        self.Container3 = Frame(master,bg="blue")
        self.Container3.pack()
        self.Container3.place(bordermode=OUTSIDE, height=400, width=400, x=400)

        self.lbl21= Label(self.Container2, text="Texto1 - Container 2")
        self.lbl30.grid(row=0,column=0, padx= 10, pady=10)
        self.lbl31= Label(self.Container2, text="Texto2 - Container 2")
        self.lbl32.grid(row=1,column=0, padx= 10, pady=10)
        self.lbl33= Label(self.Container2, text="Texto3 - Container 2")
        self.lbl34.grid(row=2,column=0, padx= 10, pady=40)
        self.lbl35= Label(self.Container2, text="Texto4 - Container 2")
        self.lbl36.grid(row=3,column=1, padx= 10, pady=10)

root = Tk()
root.title("AJUSTANDO CONTAINERS")
root.geometry('800x400')
root.mainloop()
Application(root)