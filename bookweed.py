'''This module is responsible for finding the number of days since each book was
returned or purchased and then sorting each book by the number of days in a
descending order. The final result is then returned.

This will be used by librarians to evaluate which books are not being checked
out that often or even at all, this helps them decide which books to remove to
make way more other books which might be more popular.

I does this by first calling the getHistory() function which compares every row
in database.txt with every row in logfile.txt (starting for the bottom) and then
passing the relevant information into the getDate() function.

getDate() then finds the number of days since the book was returned or purchased
and passes than information into sortLogs(). This rearranges every row into
descending order, so the librarians can easily idenify which books are not
popular'''

import database as DB
import datetime as DT


loanHistory = []

    
def getHistory():

    '''This function checks every row of the log file (starting at the last one) to
    see if it has a book ID which is identical to the one passed into the function
    by the user.

    If it does, the program checks if the book is currently checked out and generates
    a new row which is appended to the loanHistory list which will be returned.'''


    data = DB.getFile()
    logs = DB.getLog()


    global loanHistory
    loanHistory = []
    PurchaseList = []
    
    for currentRow in data:

        bookDetails = DB.prepareRow(currentRow)
        
        if bookDetails[1] != "ISBN":

            for currentLog in reversed(logs):

                logDetails = DB.prepareRow(currentLog)

                if bookDetails[1] == logDetails[1]:

                    newID = int(logDetails[0])
                    newBookDetails = DB.prepareRow(data[newID])
                    
                    if newBookDetails[5] != "0":
                        loanHistory.append(bookDetails[1]+",0")
                        break
                    else:
                        print(logDetails)
                        getDate(logDetails)
                        break

            purchaseList = ["",bookDetails[1],"",bookDetails[4],""]
            getDate(purchaseList)

    print(loanHistory)
    return loanHistory


def getDate(logDetails):

    '''
    The funciton finds the amount of days between the current date, and the date
    the book was last returned (or purchased if the book has not been checked out
    before).

    Finaly, the function appends both the book ID and the number of days since it was
    last returned/purchased, it then calls the function sortLogs to organize the
    results.

    Parameters:

    logDetails (List) = Contains each column value of the specified row of
                        logfile.txt as elements of a list
    '''

    global loanHistory

    today = DT.datetime.today().strftime('%d/%m/%Y')
    todaysDate = DT.datetime.strptime(today, '%d/%m/%Y').date()
    returnDate = DT.datetime.strptime(logDetails[3], '%d/%m/%Y').date()
               
    daysSinceCheckout = (todaysDate - returnDate).days
    print("There have been "+str(daysSinceCheckout)+" days since checkout")
        
    loanHistory.append(logDetails[1]+","+str(daysSinceCheckout))

    
    sortLogs()


def sortLogs():

    '''This function uses a simple bubble sort to organize each book by the number of
    days since it was last returned/purchased into a descending order'''
     
    for i in range(len(loanHistory)):
        
        for j in range(len(loanHistory)-1):

            currentLoanRow = DB.prepareRow(loanHistory[j])
            comparedLoanRow = DB.prepareRow(loanHistory[j+1])

            if int(currentLoanRow[1]) < int(comparedLoanRow[1]):

                temp = loanHistory[j]
                loanHistory[j] = loanHistory[j+1]
                loanHistory[j+1] = temp
        
    
          
if __name__ == "__main__":

    print("Test 1")
    testHistory = getHistory()
    print(testHistory)
    # Checks to see if the function finds the latest checkout associated with a
    # book ID, finds the date since their last return and returns a list of
    # all books which are sorted by their unpopularity.

    print("Test 2")
    purchaseList = DB.prepareRow("43,796582284,16/02/2014,18/04/2014,9919")
    testDate = getDate(purchaseList)
    print(testDate)
    # Checks to see if the function finds the difference in days between now and
    # the last time the book was returned to the library.

    print("Test 3")
    purchaseList2 = DB.prepareRow("36,748953403,20/07/2008,29/12/2008,3434")
    testDate2 = getDate(purchaseList2)
    print(testDate2)
    # Checks to see if the function finds the difference in days between now and
    # the last time the book was returned to the library.

    print("Test 4")
    loanHistory = ["1,174","2,298","3,1788","4,19","5,6743","6,992","7,365","8,4355","9,2050","10,1400"]
    testLogs = sortLogs()
    print(loanHistory)
    # Checks to se if the function rearranges the list elements so they are
    # sorted by the number of days since they were last returned to the
    # library, in descending order.
   
    print("Test 5")
    loanHistory = ["1,5699","2,1646","3,378","4,2881","5,1229","6,5208","7,2308","8,1217","9,5729","10,2481"]
    testLogs = sortLogs()
    print(loanHistory)
    # Checks to se if the function rearranges the list elements so they are
    # sorted by the number of days since they were last returned to the
    # library, in descending order.



