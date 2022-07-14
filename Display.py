# Importing user defined module.
import IndividualList

# Storing the return data from Splitted() in details.
details = IndividualList.Splitted()

# This function is called when administrator wants the program to display the books.
def getBook():
    # Opening file in read mode and storing it in books.
    books = open("Books.txt", "r")
    lines = books.readlines()
    # Displaying the details of book in a tabular format in the terminal.
    print("-----------------------------------------------------------------------")
    print("|                          Sorcerer's Library                         |")
    print("-----------------------------------------------------------------------")
    print(f"| {'Book name':<25} | {'Author':<18} | {'Amount':<8} | {'Price'}   |")
    print("-----------------------------------------------------------------------") 
    for i in range(10):
        print(f"| {details.book[i]:<25} | {details.author[i]:<18} | {str(details.amount[i]):<8} | ${str(details.price[i]):<7}|")
        print("-----------------------------------------------------------------------")
    books.close()