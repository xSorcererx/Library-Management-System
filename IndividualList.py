# Making a class.
class Splitted:
    # Defining a constructor.
    def __init__(self):
        self.book, self.author, self.amount, self.price = self.splitted()   # Calling the splitted() function and initialising the variables.

    # Defining splitted() function.
    def splitted(self):
        # Making empty lists to store respective values.
        book = []
        author = []
        amount = []
        price = []

        # Opening Books.txt in read mode.
        file = open("Books.txt", "r")
        lines = file.readlines()
        list = []

        # For loop to store lines in a list.
        for i in lines:
            element = i.split(",")
            # Adding the values to the list.
            list.append(element)
        
        # For loop to store the individual values in the respective lists.
        for k in range(len(list)):
            book.append(list[k][0])
            author.append(list[k][1])
            amount.append(int(list[k][2]))
            price.append(float(list[k][3].strip('$ \n')))
        
        # Returning the lists.
        return book, author, amount, price
