'''This module is responsible for updating the database.txt and logfile.txt
files when the user wants to return a book and it does this through the use
of its various functions.

Firstly, the checkoutCheck function is called to make sure that the entered
book ID is valid, once this is clarified: the checkoutBook function is called
and the database.txt and logfile.txt files are updated with the new information.'''

import database as DB
import datetime as DT

def checkoutCheck(ID,MembID):

    '''
    Checks if the book the user has selected is in the database by comparing
    it's ID and then checking if that book is in stock. If both procedures
    return true: the checkout process continues by calling the checkoutBook
    function.

    Parameters:

    ID (Integer) = The unique ID of the specified book

    MembID (Integer) = The unique ID of the member checking out the book
    '''

    isValid = DB.validCheck(ID)
    
    if isValid == True:
    # Checks if the entered book ID is valid, if so: the inStock variable is
    # updated
    
            inStock = DB.checkStock(ID)
            
    # Checks if the book associated with the entered ID is in stock, if so:
    # the program calls the checkoutBook function to update the database.txt
    # and logfile.txt files

            
            if inStock == True:
                print("ID is valid and the book is in stock")
                checkoutBook(ID,MembID)
            else:
                
    # Otherwise, the program will print an error message
    
                 print("ID is valid but the book is not in stock")

def checkoutBook(ID,MembID):

    '''
    Firstly, the function will retrieve the database row corresponding to the
    entered ID and alter the Member ID value. It will then overwrite the
    origional row in the database with the new information.

    Secondly, the funciton will also append a new row to logfile.txt with the
    respective ID, ISBN, checkout/returns dates and the Member ID.

    Parmeters:

    ID (Integer) = The unique ID of the specified book

    MembID (Integer) = The unique ID of the member checking out the book
    '''

    file = DB.getFile()
    bookRow = file[int(ID)]
    
    selectedBook = DB.prepareRow(bookRow)
    selectedBook[5] = MembID
    # splits the current file line into a list and sets the Member ID element
    # to be equal to the entered member ID
       
    newBookData = ",".join(selectedBook)
    newBookData = newBookData+"\n"

    # Joins it back together into 1 string and adds a newline character to the
    # end so each row is contained on one line in the file.
    
    file[int(ID)] = newBookData
    print("The new database row is "+str(file[int(ID)]))
    DB.writeFile(file)

    # overwrites the old row with the updated version and calls the function
    # writeFile to write the final list to database.txt
    
    
    newBookLog = ",".join([ID,selectedBook[1],str(DT.datetime.today().strftime('%d/%m/%Y')),"",MembID])
    newBookLog = newBookLog+"\n"
    print("The new logfile entry is "+str(newBookLog))
    DB.appendLogs(newBookLog)
    
    # Creates a new line in logfile.txt with today's date, indicating that there
    # is a new person checking out the book/that book's log has been updated


if __name__ == "__main__":

    print("Test 1")
    checkoutCheck("90","1111")
    # Checks to see if the function reacts to an invalid ID correctly.

    print("Test 2")
    checkoutCheck("9","1111")
    # Checks to see if the function reacts to a valid ID correctly.

    print("Test 3")
    checkoutCheck("24","1111")
    # Checks to see if the function reacts to try to check out a book that's
    # already out of stock correctly.

    print("Test 4")
    checkoutBook("27","2222")
    # checks to see if the function inserts the new rows in database.txt and
    # logfile.txt

    print("Test 5")
    checkoutBook("25","2222")
    # checks to see if the function inserts the new rows in database.txt and
    # logfile.txt with a different ID

    # Testing of checkoutBook is limited since all the error
    # checking is done in checkoutCheck, so we can only test if checkoutBook
    # performs its task successfully.













    
    
