# Importing datetime and date from datetime module.
from datetime import datetime,date

# Defining function that fetches today's date.
def getDate():
    return date.today()

# Defining function that fetches current time.
def getTime():
    return datetime.now().time()
