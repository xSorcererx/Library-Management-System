# Importing modules to get date, time, individual lists containing details of book and to specify the path.
import IndividualList
import DateTime
import datetime
import os.path

# Storing the return data from Splitted() in bookDetails.
bookDetails = IndividualList.Splitted()

# Defining returnBooks() function.
def returnBooks():
    while(True):
        # Try block to check if the user with input first and last name has borrowed the book from library or not.
        try:
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

            # Assigning the name of the borrow file with user name to a variable.
            file_ = "Borrow details - " + fName + " " + lName + ".txt"

            # Specifying the path of Borrow files folder.
            path = os.path.join('Borrow files', file_)

            # Opening the file in read mode.
            borrow_file = open(path, "r")
            check_book = borrow_file.read()

            # Changing the cursor position to 0 again.
            borrow_file.seek(0)

            lines = borrow_file.readlines()
            break

        # Displaying message if the user with input name has not borrowed a book yet.
        except:
            print(fName + " has not borrowed any books from our library yet. Please make sure the name you've entered is correct.")

    # Assigning the name of the return file with user name to a variable.
    file_name = "Return details - " + fName + " " + lName + ".txt"

    # Specifying the path of Borrow files folder.
    path = os.path.join('Return files', file_name)

    # Creating and opening the return file in write mode.
    return_file = open(path, 'w')

    # Making a bill template.
    return_file.write("\t\t\t\t\t\tSorcerer's Library \n\n")
    return_file.write(
        f"{'Date: ' + str(DateTime.getDate()):<59} {'Time: ' + str(DateTime.getTime())} \n")
    return_file.write("Returned by: " + fName + " " + lName + "\n\n")
    return_file.write(
        f"\t{'S.N.':<5} {'Book-name':<27} {'Author name':<20} {'Price (per 10 days in $)':<4} \n")
    return_file.close()

    total = 0.0
    count = 1
    for i in range(10):
        # Checking which book(s) were borrowed by the user.
        if bookDetails.book[i] in check_book:
            # Opening the return file in append mode.
            return_file = open(path, "a")

            # Writing in the return file.
            return_file.write(
                f"\t{count:<5} {bookDetails.book[i]:<27} {bookDetails.author[i]:<20} {bookDetails.price[i]:<4} \n")
            count += 1
            total += bookDetails.price[i]
            return_file.close()

            # Updating the changes in the amount list.
            bookDetails.amount[i] = int(bookDetails.amount[i]) + 1
    print("")

    # Opening Books.txt in write mode to update it.
    books = open("Books.txt", "w")
    for i in range(10):
        books.write(bookDetails.book[i] + "," + bookDetails.author[i] + "," + 
        str(bookDetails.amount[i]) + ",$" + str(bookDetails.price[i]) + "\n")
    books.close()

    # Assigning the current date i.e., the date of return.
    return_date = datetime.datetime.now()

    # Getting the borrow date from the borrow file.
    borrow_date = datetime.datetime.strptime(lines[2].split(" ")[1], "%Y-%m-%d")

    # Subtracting the dates and getting the days to calculate the fine.
    borrow_days = return_date - borrow_date
    fine_days = borrow_days.days

    fine = 0
    # Checking if the books have expired or not.
    if fine_days <= 10:
        # Displaying the total without the fine.
        print("\nThank you for returning the book within 10 days. Your subtotal is $" +
              str(total) + ". Here's your receipt.\n")
    else:
        # Calculating the fine(per day).
        fine = (fine_days-10) * 0.4
        total = total + fine

        # Displaying the total with the fine.
        print("You are late to return the book by " + str(fine_days-10) +
              " days. So $0.4 will be charged per day and your subtotal is $" + str(total) + ". Here's your receipt.\n")

    # Opening the return file to write the fine money, and total price to pay.
    return_file = open(path, "a")
    return_file.write(
        "\t------------------------------------------------------------------------------\n")
    return_file.write(f"\t{'Fine:':<54} {'$' + str(fine)} \n")
    return_file.write(f"\t{'Total:':<54} {'$' + str(total)}")
    return_file.close()

    # Opening the return file to display the rececipt to the user.
    return_note = open(path, "r")
    lines = return_note.readlines()
    for line in lines:
        print(line)
    return_note.close()
    print("\t\t\tThank You. Visit Again.")
