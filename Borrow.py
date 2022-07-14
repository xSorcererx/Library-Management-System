# Importing modules to get date, time and individual lists containing details of book.
import DateTime
import IndividualList
import os.path

# Storing the return data from Splitted() in bookDetails.
bookDetails = IndividualList.Splitted()

# Defining borrow() function.
def borrowBooks():
    # Accepting the user's first and last name and also checking for any false character in name like numbers & special characters.
    while(True):
        fName = input("Enter your first name: ")
        if fName.isalpha():
            break
        print("Please enter alphabet characters (A-Z/ a-z)")

    while(True):
        lName = input("Enter your last name: ")
        if lName.isalpha():
            break
        print("Please enter alphabet characters (A-Z/ a-z)")
    print("\n")

    # Assigning the name of the file with user name to a variable.
    file_name = "Borrow details - " + fName + " " + lName + ".txt"
    
    # Specifying the path of Borrow files folder.
    path = 'Borrow files'
    file = os.path.join(path, file_name)

    # Creating and opening the file in write mode.
    borrow_file = open(file, "w")

    # Creating a bill template.
    borrow_file.write("\t\t\t\t\t\tSorcerer's Library \n\n")
    borrow_file.write(
        f"{'Date: ' + str(DateTime.getDate()):<59} {'Time: ' + str(DateTime.getTime())} \n")
    borrow_file.write("Borrowed by: " + fName + " " + lName + "\n\n")
    borrow_file.write(
        f"\t{'S.N.':<5} {'Book-name':<27} {'Author name':<20} {'Price(per 10 days in $)':<4} \n")
    borrow_file.close()

    # Creating empty list to store the book codes of the books that have been borrowed by the user.
    book_list = []
    total = 0
    borrow = True
    while borrow == True:
        # Printing the book codes and names.
        for i in range(10):
            print("Enter code " + str(i) + " to borrow " + bookDetails.book[i])

        # Try block to validate the input from the user. The input value must be an integer.
        try:
            num = int(input("\nEnter code here: "))
            # Try block to check if the input integer is a code(0-9) or not.
            try:
                # If...else to check if the book is available or not.
                if bookDetails.amount[num] > 0:

                    # Adding the input value to list.
                    book_list.append(num)

                    # Writing the details in the Borrow file.
                    print("The book is available. You have borrowed " +
                          bookDetails.book[num] + " on " + str(DateTime.getDate()))
                    borrow_file = open(file, "a")
                    borrow_file.write(
                        f"\t{'1':<5} {bookDetails.book[num]:<27} {bookDetails.author[num]:<20} {bookDetails.price[num]:<4} \n")
                    total = bookDetails.price[num] + total
                    borrow_file.close()

                    # Subtractng the amount of chosen book in the list.
                    bookDetails.amount[num] = int(bookDetails.amount[num]) - 1

                    # Writing in the main Books.txt file.
                    books = open("Books.txt", "w")
                    for i in range(10):
                        books.write(bookDetails.book[i] + "," + bookDetails.author[i] + "," + str(bookDetails.amount[i]) +
                                    ",$" + str(bookDetails.price[i]) + "\n")
                    books.close()

                    # For borrowing multiple books.
                    count = 1
                    loop = True
                    while loop == True:
                        cont = input("\nDo you want to borrow more books? (Y/N)").upper()
                        if cont == "Y":
                            # Try block to validate the input value from the user.
                            try:
                                # Displaying book codes and names.
                                for i in range(10):
                                    print("Enter code " + str(i) +
                                          " to borrow " + bookDetails.book[i])

                                while(True):
                                    num = int(input("\nEnter code here to borrow different book: "))
                                    # Checking if the book has already been borrowed or not.
                                    if num in book_list:
                                        print("Sorry, you cannot borrow the same book twice.")

                                    else:
                                        # Try block to check if the input integer is a code(0-9) or not.
                                        try:
                                            amount = bookDetails.amount[num]
                                            break
                                        # Except block if the input integer is not a code assigned to the books.
                                        except IndexError:
                                            print("Please enter assigned codes!")

                                # Checking if the book chosen is available or not.
                                if amount > 0:
                                    # Adding the input code to the list again.
                                    book_list.append(num)
                                    print("The books is available. You have borrowed " +
                                          bookDetails.book[num] + " on " + str(DateTime.getDate()))

                                    # Opening the borrow file in append mode.
                                    borrow_file = open(file, "a")

                                    # Writing the details in the borrow file.
                                    borrow_file.write(
                                        f"\t{str(count + 1):<5} {bookDetails.book[num]:<27} {bookDetails.author[num]:<20} {bookDetails.price[num]:<4}\n")
                                    total = bookDetails.price[num] + total
                                    borrow_file.close()

                                    # Subtractng the amount of chosen book in the list.
                                    bookDetails.amount[num] = int(bookDetails.amount[num]) - 1

                                    # Writing the updated value in the main Books.txt file
                                    books = open("Books.txt", "w")
                                    for i in range(10):
                                        books.write(bookDetails.book[i] + "," + bookDetails.author[i] + "," + str(
                                            bookDetails.amount[i]) + ",$" + str(bookDetails.price[i]) + "\n")
                                    books.close()
                                    count += 1
                                    borrow = True
                                else:
                                    print("The book you want to borrow is currently unavailable. Sorry")
                                    break
                            
                            # Displaying message if the input value is not an integer.
                            except ValueError:
                                print("String an special characters is invalid. Please enter numerical value as assigned!")
                        
                        # Breaking the loop if the user decides not to borrow any more books.
                        elif cont == 'N':
                            print("\nPlease make sure to return the book(s) within 10 days. Thank you for borrowing. Happy reading!")
                            loop = False
                            borrow = False
                        
                        # Else block if the user inputs any other characters than Y/y or N/n.
                        else:
                            print("Please enter Y for yes and N for no. Any other input is considered invalid")

                # Informing the user about the unavailability of the book.
                else:
                    print("The book you want to borrow is currently unavailable. Sorry")

            # Displaying message if the input integer is not a code (0-9).
            except IndexError:
                print("Please enter assigned codes!")

        # Displaying message if the input value is not an integer.
        except ValueError:
            print("String and special characters are invalid. Please enter numerical value as assigned!")
    
    # Writing the total price of borrowing the the book(s).
    borrow_file = open(file, "a")
    borrow_file.write(
        "\t------------------------------------------------------------------------------\n")
    borrow_file.write(
        f"\t{'Total (if returned within 10 days):':<54} {'$' + str(total)}")
    borrow_file.close()

    # Displaying the borrow receipt to the user..
    print("\nHere is your borrow receipt. Please make sure to return the book before 10 days.\n")
    borrow_note = open(file, 'r')
    lines = borrow_note.readlines()
    for line in lines:
        print(line)
    borrow_note.close()
