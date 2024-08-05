'''This module is responsible for updating the database.txt and logfile.txt
files when the user wants to return a book and it does this through the use
of its various functions.

Firstly, the returnCheck function is called to make sure that the entered
book ID is valid, once this is clarified: the returnBook function is called
and the database.txt and logfile.txt files are updated with the new information.
'''

import database as DB
import datetime as DT



def returnCheck(ID,MembID):

    '''
    Checks if the Book ID is valid/is held in the database and returns
    True if it is, and does nothing if it isn't.

    Parameters:

    ID (Integer) = The unique ID of the specified book

    MembID (Integer) = The unique ID of the member returning the book
    '''

    isValid = DB.validCheck(ID)

    if isValid == True:
        print("function has completed its task (successfully checked if valid)")
        returnBook(ID,MembID)
    else:
        print("function has completed its task (invalid ID or member ID)")    

def returnBook(ID,MembID):

    '''
    Retrieves book data from the database and compares it against the entered ID
    and Member ID. If the correspoding row shows that the book has been taken
    out, then it overwrites the databse row with a new version showing that it
    is available. It also updates the logfile with the new information, if the
    member ID does not match the corresponding Member iD in the database: it will
    print an error message.

    Parameters:

    ID (Integer) = The unique ID of the specified book

    MembID (Integer) = The unique ID of the member returning the book   
    '''

    file = DB.getFile()
    bookRow = file[int(ID)]
    
    selectedBook = DB.prepareRow(bookRow)
        
    if MembID == selectedBook[5]:
        selectedBook[5] = "0"

 # Checks if the member ID that's been entered matches the one assigned to the
 # borrowed book, if it is: the Member ID is set to "0"

            
        newBookData = ",".join(selectedBook)
        newBookData = newBookData+"\n"
        file[int(ID)] = newBookData
        DB.writeFile(file)


 # The row list is joined into 1 string and the row is replaced. Finally,
 # the file is updated.

        retrieveLogs(ID,MembID)
        
    else:
        print("You don't own this book")



def retrieveLogs(ID,MembID):

    '''
    Starting at the last row, the function decrements through each line until
    it finds one with an ID matching that of the entered user ID. When the ID
    is found: it overwrites the orgional row with an updated version showing a
    new return date.

    Parameters:

    ID (Integer) = The unique ID of the specified book

    MembID (Integer) = The unique ID of the member returning the book   
    '''

    currentRow = ""
        
    bookLogs = DB.getLog()
        
    for logRow in reversed(bookLogs):
    # Loops through the logfile in reverse order

        logDetails = DB.prepareRow(logRow)
   
        if logDetails[0] == ID:
    # until it finds a row where the first element in the list is the matching
    # ID to the relevant book

            logDetails[4] = MembID+"\n"
            selectedRow = bookLogs.index(logRow)
            print("logfile row "+str(selectedRow)+" has been found") 
            updateLogs(logDetails,bookLogs,selectedRow)
    # Member ID is updated and the updatedLogs function is called to update the date





def updateLogs(logDetails,bookLogs,selectedRow):   

    '''
    Opens the file, sets the value of the date column to the new date in the
    selected row. The function then joins these columns together into 1 array,
    representing the row and overwrites the row in the file.

    Parameters:

    logDetails (List) = Contains each column value of the specified row of
                        logfile.txt as elements of a list 

    bookLogs (List) = Contains every line/row in logfile.txt stored as
                      elements in a list

    selectedRow (Integer) = The line/index number of the specified row in
                            logfile.txt
    '''

        
    logDetails[3] = str(DT.datetime.today().strftime('%d/%m/%Y'))
    # Sets the return date lement equal to the current date

    newLog = ",".join(logDetails)
    bookLogs[selectedRow] = newLog
    print(bookLogs[selectedRow]+" has overwritten the old row")
    # joins the list together into a single string which is used overwrite the
    # row that was previosuly there.
    

    DB.writeLogs(bookLogs)

    # Finally, the updated lines are written back to logfile.txt


if __name__ == "__main__":

    print("Test 1")
    returnCheck("400","6049")
    # Checks if it will accept an ID that isn't in the database

    print("Test 2")
    returnCheck("40","6049")
    # Checks if it will return a book with ID 40, borrowed by Member ID 6049

    print("Test 3")
    returnCheck("40","6049")
    # Checks if you can repeat the process, even if 6049 doesn't have the book

    print("Test 4")
    retrieveLogs("33","9329")
    #Checks if it will retrieve the correct row from the database

    print("Test 5")
    logDetails = DB.prepareRow("4,129051572,24/12/2019,17/01/2020,1111")
    bookLogs = DB.getLog()
    updateLogs(logDetails,bookLogs,5)
    # Checks if the logfile is being updated when a row, the file contents and
    # the index position are passed into the updateLogs function.
    

    # Testing of retrieveLogs and updateLogs is limited since all the error
    # checking is done in returnCheck, so we can only test if they perform
    # their task successfully.


    







    
