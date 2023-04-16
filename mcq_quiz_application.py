from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import*
from PIL import Image, ImageTk
top=Tk()
top.title("Quiz World")
top.geometry("1050x800")
top.configure(background="light yellow")
lbltitle=Label(top,text="Welcome to Quiz World",bg="light yellow",fg="Red",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
lbltitle.pack(side=TOP,fill=X)


DataFrameLeft=LabelFrame(top,text="Student's Details",bg="light yellow",fg="green",bd=20,relief=RIDGE,font=("times new roman",30,"bold"))
DataFrameLeft.place(x=220,y=140,width=650,height=300)


member2=Label(DataFrameLeft,text="Student's Name ",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6)
member2.grid(row=1,column=0,sticky=W)
member2=Entry(DataFrameLeft,font=("times new roman",20,""))
member2.grid(row=1,column=3 )

member3=Label(DataFrameLeft,text="Roll Number  ",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6)
member3.grid(row=2,column=0,sticky=W)
member3=Entry(DataFrameLeft,font=("times new roman",20,""))
member3.grid(row=2,column=3)

member4=Label(DataFrameLeft,text="Mobile Number ",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6)
member4.grid(row=3,column=0,sticky=W)
member4=Entry(DataFrameLeft,font=("times new roman",20,""))
member4.grid(row=3,column=3)


def Qu():
    from tkinter import messagebox as mb
    import json
    class Quiz:
        def __init__(self): 
            self.q_no=0
            self.display_title()
            self.display_question()
            self.opt_selected=IntVar()
            self.opts=self.radio_buttons()
            self.display_options()
            self.buttons()
            self.data_size=len(question)
            self.correct=0

        def display_result(self):
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"
            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

        def check_ans(self, q_no):
            if self.opt_selected.get() == answer[q_no]:
                return True
 
        def next_btn(self):
            if self.check_ans(self.q_no):
                self.correct += 1
            self.q_no += 1
            if self.q_no==self.data_size:
                self.display_result()
                gui.destroy()
            else:
                self.display_question()
                self.display_options()

        def buttons(self):
            next_button = Button(gui, text="Next",command=self.next_btn,
            width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
            next_button.place(x=350,y=380)
            quit_button = Button(gui, text="Quit", command=gui.destroy,
            width=5,bg="black", fg="white",font=("ariel",16," bold"))
            quit_button.place(x=700,y=50)
 
        def display_options(self):
            val=0
            self.opt_selected.set(0)
         
            for option in options[self.q_no]:
                self.opts[val]['text']=option
                val+=1

        def display_question(self):
            q_no = Label(gui, text=question[self.q_no], width=60,
            font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
            q_no.place(x=70, y=100)

        def display_title(self):
            title = Label(gui, text="Welcome "+s,
            width=50, bg="yellow",fg="red", font=("ariel", 20, "bold"))
            title.place(x=0, y=2)

        def radio_buttons(self):
            q_list = []
            y_pos = 150
         
            while len(q_list) < 4:
                radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
                value = len(q_list)+1,font = ("ariel",14))
                q_list.append(radio_btn)
                radio_btn.place(x = 100, y = y_pos)
                y_pos += 40
            return q_list
 
# Create a GUI Window
    gui=Toplevel(top)
    gui.geometry("800x450")
    gui.title("Quiz?")
    with open("data.json") as f:
        data=json.load(f)
    s=member2.get()
# set the question, options, and answer
    question = (data['question'])
    options = (data['options'])
    answer = (data[ 'answer'])
    quiz=Quiz()
    top.gestroy()
    gui.mainloop()



member5=Button(DataFrameLeft,text="Submit ",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6,command=Qu)
member5.grid(row=7,column=2) 

DataFrameLeft=LabelFrame(top,text="Guided By :",bg="light yellow",fg="green",bd=20,relief=RIDGE,font=("times new roman",30,"bold"))
DataFrameLeft.place(x=10,y=460,width=500,height=300)
guid1=Label(DataFrameLeft,text="",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6)
guid1.grid(row=3,column=0,sticky=W)

name3=Label(DataFrameLeft,text="Surbhi Upadhyay \n Assistant Professor ",bg="light yellow",font=("times new roman",25,"bold"),padx=2,pady=6)
name3.grid(row=1,column=1,sticky=W)


DataFrameLeft=LabelFrame(top,text="Guided To :",bg="light yellow",fg="green",bd=20,relief=RIDGE,font=("times new roman",30,"bold"))
DataFrameLeft.place(x=530,y=460,width=500,height=300)

name2=Label(DataFrameLeft,text="Aman Sharma \nRoll no- T21EJICS015 \nBranch - CSE ",bg="light yellow",font=("times new roman",20,"bold"),padx=2,pady=6)
name2.grid(row=20,column=4,sticky=W)


load= Image.open("JGI.png")
render = ImageTk.PhotoImage(load)
img = Label(top, image=render)
img.place(x=50, y=20)
top.mainloop()