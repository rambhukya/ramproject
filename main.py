from quote import quote
from tkinter import *

window=Tk()
window.geometry('1000x550')
window.title("Quotes")

def get_quotes():
    e1_value.get()
    quotes=quote(e1_value.get(),limit=25)
    for i in range(len(quotes)):
        value=quotes[i]['quote']
        #print(value)
        l1.insert(END,value)
        


window.configure(bg='grey')
b1=Button(window,text="Click Here",bg='black',fg='white',command=get_quotes)
#b1.grid(row=3,column=4)

b1.place(x=510,y=38)
#b1.pack()
#b1.pack(side=BOTTOM,padx=5,pady=5)



e1_value=StringVar()
e1=Entry(window,width=20,textvariable=e1_value)
e1.place(x=340,y=40)

#t1=Text(window,height=8,width=60)
#t1.grid(row=4,column=6)
#t1.place(x=80,y=80)
#t1.pack()

sb=Scrollbar(window)
sbb=Scrollbar(window)
sb.pack(side=RIGHT,fill=Y)
sbb.pack(side=BOTTOM,fill=X)
#sbb.place(x=190,y=250)


q1=Label(window,text="Your Quote:")
q1.place(x=10,y=87)

q2=Label(window,text="Enter your word:")
q2.place(x=230,y=38)



l1=Listbox(window,height=20,width=150,yscrollcommand=sb.set,xscrollcommand=sbb.set,bg='black',fg='white')
l1.place(x=40,y=120)
sb.config(command=l1.yview)
sbb.config(command=l1.xview)



window=mainloop()

