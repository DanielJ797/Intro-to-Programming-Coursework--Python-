'''This module is responsible for displaying a graphical user interface which
the user can interact with to perform tasks like search for books, check out
books, return books and weed books.

It also contains several functions related to the interactive buttons available
for the user to press. When one of the buttons is pressed, the relevant function
is called and the corresponding task is performed.

This module also contains a listbox which is used to show information in a list
format'''




'''This program was written by Daniel Jennings and this was written on
17/12/2020

This program is designed to be used with the graphical user interface,
the user will enter any relevant info through the text boxes and then press
the corresponding buttons to confirm an action. Pressing these buttons will
update'''


import sys
import booksearch as BS
import database as DB
from tkinter import *

sys.path.apend('')

MemberID = ""
#initialises a global variable that stores the current Member ID
searchResults = []
FillListB = []
WeedBool = False
x = []
y = []


window = Tk()

def clicked1():

    '''This function checks if the Member ID entered in the corresponding text
    box is valid, to be invalid an ID must either be outside the possible integer
    range or be of a different data type.

    If the Member ID is invalid, a relevant message is displayed for the user to see.
    If it's valid: The global Member ID variable will be updated for the rest of the
    program to access'''
    
    global MemberID
    MemberID = MemID.get()

    try:
        if int(MemberID) < 1000 or int(MemberID) > 9999:
            lbl6.configure(text="Invalid Member ID",fg="red")
            MemberID = ""
    # Checks to see if the entered Member ID is within the expeceted range,
    # if it isn't: the variable is reset and a relevant message is shown
        else:
           lbl6.configure(text="Member ID has been confirmed",fg="green")

    except ValueError:
        lbl6.configure(text="Invalid Member ID",fg="red")
        MemberID = ""
    # Using the try and except blocks, we can detect if there's a value error
    # (a value of the wrong data type has been entered) and reset the variale
    #while displaying a relevan message

def clicked2():

    '''This function retrieves the contents of the Book Search text box and passes it
    as a parameter into the TitleSearch function (which is held in the booksearch module).

    Finally, it calls the function ListB with the result of the previous function call
    being passed into it as an argument.'''

    Title = BSBox.get()
    global FillListB
    lbl5.configure(text="ID | ISBN | Author | Purchase Date | Member ID                                         (If the Member ID is 0, the book is available)")
    FillListB = BS.TitleSearch(Title)
    # Calls the TitleSearch function with the user's title query, the function will
    # return a list of all books witha matching title
    
    ListB()





def clicked3():

    '''Stores the contents of the Book Checkout textbox in the variable "ID" and
    calls the memberCheck function to verify if the MemberID is valid. If it is,
    the function calls the relevant function to check the ID's and updates the
    database. Eventually a message confirming the book checkout is shown to the
    user.'''
    
    import bookcheckout as BC
    ID = BCBox.get()
    if memberCheck() == True:
        BC.checkoutCheck(ID,MemberID)
        lbl6.configure(text="Successfully checked out book",fg="green")


        
def clicked4():

    '''Stores the contents of the Book Checkout textbox in the variable "ID" and
    calls the memberCheck function to verify if the MemberID is valid. If it is,
    it calls the function needed to update the database and the user is shown a
    message confirming the book return.'''
    
    import bookreturn as BR
    ID = BRBox.get()
    if memberCheck() == True:
    # Stores the contents of the book return text box in ID and checks that the
    # member ID variable isn't empty by calling memberCheck(), if not: the
    # program calls returnCheck with the ID and Member ID
        BR.returnCheck(ID,MemberID)
        lbl6.configure(text="Successfully returned book",fg="green")



def clicked5():

    '''Retrieves the sorted log history of all books in the database and passes
    that into the ListB function as an argument to be printed.'''
    
    import bookweed as BW
    global FillListB
    global WeedBool

    lbl5.configure(text="ISBN | Days since last returned (or purchased)")
    FillListB = BW.getHistory()
    WeedBool = True
    # Updates the listbox label and retrieves the ordered list of books to be
    # printed by the ListB function  
    ListB()
    
    
def memberCheck():

    '''If there is no value stored in the MemberID variable, this function shows
    the user a relevant message about how it is empty.'''
    
    if MemberID == "":
        lbl6.configure(text="Please enter something into the\nMember ID field.",fg="red")
        return False
    else:
        return True



def ListB():

    '''
    Clears the current contents of the listbox and fills it with either results
    of a book search or the number of days since each book was
    returned/purchased.
    '''

    global WeedBool
    global x
    global y
    ListB1.delete(0,END)
    x = []
    y = []
        
    for currentRow in FillListB:

        if WeedBool == True:
    # Checks if we are listing the result of book weeding by evaluating the
    # state of the WeedBool variable
    
            currentRow = DB.prepareRow(currentRow)
            x.append(currentRow[0])
            y.append(currentRow[1])
                        
        newRow = " | ".join(currentRow)
        ListB1.insert(END,newRow)
    # Adds a seperator | for each column of the row and inserts it at the end
    # of the listbox

    plotGraph()
    WeedBool = False



def plotGraph():

    global x
    global y
    

#=============================================================== 

window.title("Library System")
window.geometry("900x540")

lbl1 = Label(window,text="Member ID")
lbl1.place(x=20,y=20)
# Initialises lbl1 as a label and sets its position in the window

MemID = Entry(window, width=50)
MemID.place(x=180,y=20)
# Initialises the member ID text box and sets its position in the window

btn1 = Button(window, text="Confirm",command=clicked1)
btn1.place(x=500,y=20)

description1 = Label(window,text="This box must be filled to withdraw a book.")
description1.place(x=580,y=20)

#===============================================================

lbl2 = Label(window,text="Search for a book")
lbl2.place(x=20,y=60)
# Initialises lbl2 as a label and sets its position in the window

BSBox = Entry(window, width=50)
BSBox.place(x=180,y=60)
# Initialises the Book Search text box and sets its position in the window

btn2 = Button(window, text=" Search  ",command=clicked2)
btn2.place(x=500,y=60)

description2 = Label(window,text="Please enter the title of the book you are looking for.")
description2.place(x=580,y=60)

#===============================================================

lbl3 = Label(window,text="Check out a book")
lbl3.place(x=20,y=100)
# Initialises lbl3 as a label and sets its position in the window

BCBox = Entry(window, width=50)
BCBox.place(x=180,y=100)
# Initialises the Book Checkout text box and sets its position in the window

btn3 = Button(window, text="Confirm",command=clicked3)
btn3.place(x=500,y=100)

description3 = Label(window,text="Please enter the ID of the book you are checking out.")
description3.place(x=580,y=100)

#===============================================================

lbl4 = Label(window,text="Return a book")
lbl4.place(x=20,y=140)
# Initialises lbl4 as a label and sets its position in the window

BRBox = Entry(window, width=50)
BRBox.place(x=180,y=140)
# Initialises the Book Return text box and sets its position in the window

btn4 = Button(window, text="Confirm",command=clicked4)
btn4.place(x=500,y=140)

description4 = Label(window,text="Please enter the ID of the book you are returning.")
description4.place(x=580,y=140)

#===============================================================

lbl5 = Label(window,text="ID | ISBN | Author | Purchase Date | Member ID                                         (If the Member ID is 0, the book is available)")
lbl5.place(x=20,y=200)

# Initialises lbl5 as a label and sets its position in the window

ListB1 = Listbox(window,height="10",width="100")
ListB1.place(x=20,y=230)
# Initialises the List Box and sets its position in the window

lbl6 = Label(window,text="",fg="red")
lbl6.place(x=650,y=230)

#===============================================================

btn5 = Button(window, text="Weed Books",command=clicked5)
btn5.place(x=20,y=420)

description5 = Label(window,text="Evaluates which books are most suitable for weeding")
description5.place(x=120,y=420)

window.mainloop()
# Event listener that constantly checks for user input








    
    
