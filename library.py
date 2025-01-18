# Context:
# The entire system works on a dictionary consisting of a key and a value attached to it.
# The key is a user-inputted string based on their desired "username".
# Attached to the key is a list (the value) to hold multiple data values of strings.
# The value is a list that hold multiple user-inputted strings based on the "books" that the user wants to "borrow".

def borrowing(users_dict, username, borrow_book): # Function to add values to the list.
    """
    Purpose: 
        Adds to value of key: adds the user input of books to their list found in the main dictionary and creates a list for the user if list not already created in the dictionary (basically adds values from user inputs to a list attached to a key also provided from a userinput and creates a key for the user's books if not already created).
        Limitation:
        Prevents user-list from having more than 3 books at a time.
    Arguments: 
        Dictionary (including key and value): takes the "users_dict, username, and borrow_book" variables which are the main dictionary that holds each user and thier list of books, the username of the user (the key in the dictionary), and the book that they want to add to their borrow list (the value attached to the key in the dictionary).
    Return: 
        None: the function prints directly and doesn't return any value
    """
    if username not in users_dict: # Detects if user is in dictionary keys.
        users_dict[username] = [] # Adds key (username) and value (list) into dictionary (username based on user input).
        users_dict[username].append(borrow_book) # Adds book to user list in the case that user wasn't previously detected.
        print(f'{username} has successfully borrowed "{borrow_book}"!') # Tells user that book has been added to user's borrow-list. 
        return # Prevents further processing (especially lines 18-20).
    elif len(users_dict[username]) >= 3: # Detects if user's list has more than 3 values (limitation).
        print("Sorry, you can only borrow upto 3 books at a time.") # Tells user about the limitation.
        return # Prevents further processing (especially lines 18-20).
    users_dict[username].append(borrow_book) # If no other condition is met, the book is added to the list automatically.
    print(f'{username} has successfully borrowed "{borrow_book}"!') # Tells user that book has been added to user's borrow-list.
    return # Prevents further processing.
    
def returning(users_dict, username, return_book): # Function to remove values from the list.
    """
    Purpose:
        Removes value from list (which is a value for the key): removes the user-inputted value from the list attached to a key in the main dictionary and creates a key and value for user if not created previously.
    Arguments:
        Dictionary (including key and the value): takes the "users_dict, username, and borrow_book" variables which are the main dictionary, the key in the dictionary, the value (list) attached to the key in the dictionary.
    Returns:
        None: the function prints directly and doesn't return any value.
    """
    if username in users_dict.keys(): # Detects if the user-inputted key exists in the dictionary and runs the following program if detected.
        if return_book not in users_dict[username]: # Detects if the book doesn't exist in the user's list.
            print("This book has not been borrowed by the user.") # If not detected, tells the user the book hasn't been added to the list in the first place.
        elif return_book in users_dict[username]: # Detects if the book exists in the user's list.
            users_dict[username].remove(return_book) # If detected, removes the user-inputted book from their list.
            print(f'{username} has successfully returned "{return_book}"!') # Tells user that book has been removed from their list.
    else: # If not detected in the dictionary, the following will run.
        users_dict[username] = [] # Adds a key and value (list) in the dictionary for the user.
        print("No account was found in the system. Your account is now registered.") # Tells user that no key was found in dictionary previously and one was created for user.

def viewing(users_dict, username): # Function to view the user's list.
    """
    Purpose:
        Prints data values found inside the user's list.
    Arguments:
        Dictionary (including key): takes the "users_dict and username" variables which are the main dictionary that stores all keys and lists as values, and the key to find that specific list of the user.
    Returns:
        None: the function prints directly and doesn't return a value.
    """
    if username in users_dict.keys(): # Detects if user exists in the keys of the dictionary.
        print(f'Books currently borrowed by {username}: {users_dict[username]}') # Shows user what data values are found in their list. 
    else: # If user not detected as key in the dictionary, the following will run.
        print("No account found.") # Tells user no key is found in the dictionary that was inputted by them.

def viewing_all(users_dict): # Funciton to view the entire system's data.
    """
    Purpose:
        Prints the entire dictionary (whatever data values are in it at the time).
    Arguments:
        Dictionary: takes the "users_dict" variable which is the main dictionary containing all keys and values.
    Returns:
        None: the function prints directly and doesn't return any value.
    """
    print("All borrowed books in the library:")
    if users_dict: # Detects if the dictionary has keys inside it.
        for user in users_dict: # Loops through every key in the dictionary.
            print(f'- {user} has borrowed: {users_dict[user]}') # For every key, it will print the key and value (list of books).
    else: # Detects if the dictionary is empty.
        print("No users are borrowing currently.") # Tells user that the dictionary is empty with no keys
        
def library_system():
    """
    Purpose:
        To act as a UI (user interface) for the user allowing them to see what's possible in the system and to run other functions depending on user preference.
    Arguments:
        None: only defined for the sake of simplicity and easier readability. 
    Returns:
        None: the function prints directly and doesn't return any value (only acts as a user interface to run other functions).
    """
    users_dict = {} # Creats an empty dictionary to handle all data of the library. 
    while True: # Continuously runs the followign program while the program is True (that it exists and has a boolean value of True). Useful so that the program doesn't end after an execution, so that the dictionary can retain information after every user input and every time it is used.
        try: # This is a try and catch system. It tries a certain program, but if a specific error is detected, then it runs another thing depending on what the error is. Therefore, it is a conditional statement that works with cases (telling the program to run this, but if the program gives something else instead (for example the error), run this).
            user_input = int(input("\nWelcome to the Library System! What would you like to do?\n1. Borrow a book\n2. Return a book\n3. View borrowed books\n4. View all borrowed books in the library\n5. Exit\nEnter your choice (1-5): ")) # A user interface (UI) that tells the user what options are possible to do in the Library System and specifies to enter a number depending on what the user wants to do.
            if user_input < 1: # Detects if the input is smaller than 1 for bad user input handling.
                print("Error, you have entered an invalid number. Try again!") # Tells user that only options 1-5 will allow them to use the Library System.
            elif user_input == 1: # Detects if user input is 1: if the user wants to borrow books based on the option given to "1".
                username = input("Enter your username: ") # Asks user for their username so that the system can use it as a key to store values of books.
                borrow_book = input("Enter the title of the book to be borrowed: ") # Asks user for the book to be added to their list.
                borrowing(users_dict, username, borrow_book) # Calls and runs the function that adds values to the user's list.
            elif user_input == 2: # Detects if user input is 2: if the user wants to return books based on the option given to "2".
                username = input("Enter your username: ") # Asks user for their username so that the system can use it as a key to store values of books.
                return_book = input("Enter the title of the book to be returned: ") # Asks user for the book to be removed from their list.
                returning(users_dict, username, return_book) # Calls and runs the function that removes values from the user's list.
            elif user_input == 3: # Detects if user input is 3: if the user wants to view their currently borrowed books based on the option given to "3".
                username = input("Enter your username: ") # Asks user for their username so that the system can use it as a key to store values of books.
                viewing(users_dict, username) # Calls and runs the function that prints all values from the user's list.
            elif user_input == 4: # Detects if user input is 4: if the user wants to view all borrowed books in the library based on the option given to "4".
                viewing_all(users_dict) # Calls and runs the function that prints the entire dictionary.
            elif user_input == 5: # Detects if user input is 5: if the user wants to exit the system based on the option given to "5".
                print("You have exited the Library System. Please visit again!") # Tells user they have exited the system.
            elif user_input > 5: # Detects if the input is larger than 5 for bad user input handling.
                print("Error, you have entered an invalid number. Try again!") # Tells user that only options 1-5 will allow them to use the Library System.
        except ValueError: # Tells the program to run the following if the user inputted text or a decimal (when inputting anything other than integers into a int() (integer conversion), it will give a ValueError, hence the function detects ValueError and not any other kind of errors.   )
            print("Error, you have entered incorrectly. Try again with the requested numbers!") # Tells the user that they have inputted incorrectly and must try again with the correct integers that were specified in the UI.

# Runs the program only if the program is run directly (prevents automatic execution if imported).
if __name__ == "__main__":
    library_system()