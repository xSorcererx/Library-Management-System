#importing user defined modules.
import Display
import Borrow
import Returns

# Welcoming the user.
print("<------------ Sorcerer's Library ------------->")

print("Hello! Welcome to Sorcerer's Library where all kinds of books are available. Let's dive into the world of books.")
while(True):
    # Providing options to the user.
    print("\nEnter 1 to display the books.")
    print("Enter 2 to borrow your favourite book(s).")
    print("Enter 3 to return the book(s).")
    print("Enter 4 to exit.")

    #Try block to make sure the user inputs integer value.
    try:
        # Accepting users' choice as input.
        option = int(input("Enter code here: "))

        if option == 1:   #if input is 1, the program displays the information about all the books in the library.
            print("\nHere are all the books we have in our Library along with authors name, quantity of the available books and their price for 10 days period.\n")
            Display.getBook()   #calling getbooks() from display module.

        elif option == 2:   #if input is 2, the program helps the user to borrow the book(s) from the library.
            Borrow.borrowBooks()    #calling borrowBooks() from borrow module.

        elif option == 3:   #if input is 3, the program helps the user to return the  book(s) to the library.
            Returns.returnBooks()   #calling returnBooks() from returns module.

        elif option == 4:   #if input is 4, the program exits.
            print("\nThank you for visiting Sorcerer's Library. Visit Again and till then happy reading.")
            exit()
        else:   #displaying message if user enters numbers other than 1-4.
            print("\nPlease enter options from 1-4 as provided.")
    
    #displaying exception message if user enters Strings or special characters.
    except ValueError:
        print("\n\nString and special characters are considered invalid. Please enter integer value.")
    
    

        
