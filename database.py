'''This module is responsible for holding several functions that would be
frequently called from several different files to perform different tasks.
Being stored here: they can be called from anywhere and the programmer
doesn't have to constantly rewrite each function across different files.

Using these functions, bookcheckout.oy, bookreturn.py and booksearch.py can
interact withe the database.txt and logfile.txt files.'''

f = open("database.txt","r")

def prepareRow(currentRow):
    
    '''
    Splits a string (passed into the functionas a parameter) into a list
    seerated by the , character and returns the results.

    Parameters:

    currentRow (String) = The current line in the database.txt file stored as
                          a string
    '''
    
    currentRow = currentRow.strip()

    # Removes the leading and trailing whitespace from the current row,
    # ensuring that if any row is returned: it won't contain '\n' at the end
    
    bookDetails = currentRow.split(",")                   

    # Splits the contents of the current database row into its respective columns, using ',' as a seperator
    
    return bookDetails


def checkStock(ID):
    
    '''
    Starting on the first row, this function increments through each line in
    the database and searches for a book that has both a matching ID and is in
    stock.

    If these conditions are met: the funciton will return True, otherwise it
    will return False and show the user a relevant message saying the book isn't
    in stock

    Parameters:

    ID (Integer) = The unique ID of the specified book
    ''' 

    for currentRow in f:
        bookDetails = prepareRow(currentRow)
        if ID == bookDetails[0] and bookDetails[5] == "0" and ID != "ID":

    # Checks if the book is available and the ID is not equal to the title
    # If so, the function returns True
    
            print("This book is currently in stock")
            resetPointer()
            return True

    # Otherwise, the function returns Ffalse
    
    resetPointer()    
    print("This book is not currently in stock") 
    return False


def validCheck(ID):

    '''
    Checks if the book ID entered by the user matches any in the database.
    If it does: then it returns True, otherwise it shows the user a relevant
    message and returns False.

    Parameters:

    ID (Integer) = The unique ID of the specified book
    '''

    resetPointer()
    for currentRow in f:
    # iterates through each row, hoping to find the book with
    # the corresponding ID
        
        bookDetails = prepareRow(currentRow)
        if ID == bookDetails[0] and ID != "ID":
    # Checks if the ID is equal to the first column in the current row and if
    # it's different from the header row, if so: the function returns True
            
            print("This is a valid ID")
            resetPointer()
            return True

    # Otherwise it returns False
                
    print("Invalid ID, please try again.")
    resetPointer()
    return False


def getFile():

    '''Stores the contents of the database file as a list of strings and
    returns the result'''
  
    resetPointer()
    file = f.readlines()
    print("successfully retrieved database entries")
    resetPointer()

    # Resets the file pointer and transfers every line in database.txt into an
    # element of a list called 'file' which is then returned
    
    return file


def getLog():

    '''Stores the contents of logfile.txt as a list of strings and
    returns the result'''

    g = open("logfile.txt","r")
    
    g.seek(0,0)
    bookLogs = g.readlines()
    print("Successfully retrieved booklogs")

    # Resets the file pointer and transfers every line in logfile.txt into an
    # element of a list called 'file' which is then returned
    
    return bookLogs

        
def resetPointer():

    '''Resets the pointer for the database.txt file'''
    
    f.seek(0,0)
    test = f.readline()
    print(str(test)+" is the first row")
    f.seek(0,0)
    
    
def writeFile(file):

    '''Takes a string as a parameter and writes it to database.txt, erasing
    the origional contents'''
    
    f = open("database.txt","w")
    resetPointer()
    f.writelines(file)
    # Rewrites the contents of the file f with the list 'file'
    resetPointer()

def appendLogs(file):

    '''Takes a string as a parameter and appends it to the end of logfile.txt'''
    
    g= open("logfile.txt","a")
    g.seek(0,0)
    g.write(file)
    # Adds an extra line to the end of logfile.txt
    g.seek(0,0)

def writeLogs(file):

    '''Takes a string as a parameter and writes it to logfile.txt, erasing
    origional contents'''
    
    g= open("logfile.txt","w")
    g.seek(0,0)
    g.writelines(file)
    # Rewrites the contents of the file g with the list 'file'
    g.seek(0,0)

if __name__ == "__main__":
    
    print("Test 1")
    testOne =prepareRow("a,b,c,d,e,f,g")
    print(testOne)
    # Checks to see if the function does parse a string into several elements
    # in a list

    print("Test 2")
    testTwo =prepareRow("11,5,77,98,2313,646456,7686")
    print(testTwo)
    # Checks to see if the function does parse a string into several elements
    # in a list

    print("Test 3")
    testThree = checkStock("1")
    print(testThree)
    # Checks to see if the function correctly identifies the book is in stock
    
    print("Test 4")
    testFour = checkStock("2")
    print(testFour)
    # Checks to see if the function correctly identifies the book isn't in stock

    print("Test 5")
    testFive = validCheck("45")
    print(testFive)
    # Checks to see if the function correctly identifies that this is a valid
    # function

    print("Test 6")
    testSix = validCheck("450")
    print(testSix)
    # Checks to see if the function correctly identifies that this is not a
    # valid function

    print("Test 7")
    testSeven = getFile()
    print(testSeven)
    # Checks to see if the function is reading every line from the file and
    # storing them as elements of a list

    print("Test 8")
    testEight = getLog()
    print(testEight)
    # Checks to see if the function is reading every line from the file and
    # storing them as elements of a list
    
    print("Test 9")
    resetPointer()
    # Checks to see if the function resets the file pointer for database.txt
    
    print("Test 10")
    testTen = writeFile("hello")
    print(testTen)
    # Checks to see if the function rewrites the database file to say "hello"

    print("Test 11")
    testEleven = appendLogs("hello")
    print(testEleven)
    # Checks to see if the function appends "hello "to the end of the file
    
    print("Test 12")
    testTwelve = writeLogs("hello")
    print(testTwelve)
    # Checks to see if the function rewrites the logfile to say "hello"



    
