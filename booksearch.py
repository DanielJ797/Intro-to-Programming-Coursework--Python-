'''This module is responsible for searching through eveery row in the database and
returning any with a book title matching that of the user's input. It contains the
TitleSearch() function which does exactly that and is called from a function in
the menu file.'''

import database as DB


def TitleSearch(Title):
    
    '''
    This function is used to search through every row in the database, split
    them into their respective columns and compare the contents of the title
    column with the 'Title' string entered as the argument of the function.

    If there is a book in the library database with the same title as the search
    criteria, then all information about it will be returned to the user

    Parameters:

    Title (String) = The title of the book the user is searching for
    '''
    
    f = DB.getFile()
    
    allResults = []                                           
        
    for currentRow in f:

        ''' Starting at line 0, the program will loop through every line in the
        file until it reaches the end and will store the contents of each
        line in 'currentRow' '''

        bookDetails = DB.prepareRow(currentRow)
        if Title == bookDetails[2] and Title != "Title":      
            allResults.append(bookDetails)

        # Compares the user search with the string contained in the Title column
        # of the database. It also denies any search if it matches the column
        # header. If the user search does match one of the book titles, all
        # information about that book will be added to the list 'allResults'

    return allResults

    ''' Returns a list containing all database entries with book titles matching
    that of the user search '''


if __name__ == "__main__":

    print("Test 1") 
    testResults = TitleSearch("Nineteen Eighty-Four")
    print(testResults)
    # Testing the title search function
    
    print("Test 2") 
    testResults = TitleSearch("Lord of the Flies")
    print(testResults)
    # Testing the title search function

    print("Test 3") 
    testResults = TitleSearch("The Lord of the Rings")
    print(testResults)
    # Testing the title search function
    
