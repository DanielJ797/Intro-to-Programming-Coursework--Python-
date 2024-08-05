# This is week 10 lab session 1
# Topic: Application Development File Operation with GUI Menu V3 + Matplotlib
# Date 10/12/2020
# By Firat Batmaz

from fileoperations import *
from tkinter import *
import matplotlib.pyplot as plt # new
testmarks=[]

def say_hello():
    print ("hello")
def say_bye():
    print ("bye")
    window.destroy()

def list_student_marks():
    i=0
    lstMarks.delete(0,END)
    for student_mark in testmarks:
        lstMarks.insert(i,student_mark[0]+":"+str(student_mark[1]))
        i+=1  
        

def update_student_mark(name,mark):

    for student_mark in testmarks:
        if student_mark[0]==name:
            student_mark[1]=mark       
    print ("the student mark has been updated successfully.")

def updateMark():
    studentMark=int(txtMark.get())
    studentName=txtName.get()
    update_student_mark(studentName,studentMark)    

def add_student_mark(name,mark):
    student_mark=[name,mark]
    testmarks.append(student_mark)
    print ("New student mark has been added successfully.")

def getMark():
    studentMark=int(txtMark.get())
    studentName=txtName.get()
    add_student_mark(studentName,studentMark)


def readMarks():
    global testmarks
    testmarks=read_student_marks()

def showGraph(): #new
    #prepare data    
    names=[]
    marks=[]
    for student_mark in testmarks:
        sname=student_mark[0]
        smark=int(student_mark[1])
        names.append(sname)
        marks.append(smark)
    print(names) #temp testing 
    print(marks) #temp testing 

    plt.bar(names,marks)
    plt.show()


#################################################
#------------------Main-------------------------#
#################################################
window=Tk()
window.title("Test Marks")
window.geometry("500x400")#updated

# Create all GUI components 
btnHello=Button(window,text="Hello",command=say_hello)
btnReadMarks=Button(window,text="Read Marks",command=readMarks)
btnListMarks=Button(window,text="Display Marks",
                    command=list_student_marks)
btnAddMark=Button(window,text="Add Mark",
                  command=getMark)
btnUpdateMark=Button(window,text="Update Mark",
                  command=updateMark)
btnSaveMarks=Button(window,text="Save Marks",
                    command=lambda:saveStudentMarksIntoFile(testmarks))
btnBye=Button(window,text="Exit",command=say_bye)
btnGraph=Button(window,text="Show Graph",command=showGraph) #new
lblName=Label(window,text="Name:")
txtName=Entry(window,width=10)
lblMark=Label(window,text="Mark:")
txtMark=Entry(window,width=10)
lstMarks=Listbox(window)



# Define locations of the components 
btnHello.grid(column=0,row=0)
btnReadMarks.grid(column=0,row=1)
btnListMarks.grid(column=0,row=2)
lblName.grid(column=0,row=3)
txtName.grid(column=1,row=3)
lblMark.grid(column=2,row=3)
txtMark.grid(column=3,row=3)
lstMarks.grid(column=4,row=0,rowspan=10)
btnAddMark.grid(column=0,row=4)
btnUpdateMark.grid(column=0,row=5)
btnSaveMarks.grid(column=0,row=6)
btnGraph.grid(column=0,row=7)  #new


btnBye.grid(column=0,row=9)

window.mainloop()
