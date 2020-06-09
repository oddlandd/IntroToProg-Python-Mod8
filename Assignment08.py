# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KOdland,6.7.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KOdland,6.7.2020,Modified code to complete assignment 8
    """

    # ----Constructor---
    def __init__(self, prod="", price=0.0):
        # ----Attributes----
        self.__product_name = prod
        self.__product_price = price

    # ----Properties-----
    # getter for product name, changes to title case
    @property
    def product_name(self):
        return str(self.__product_name).title()

    # setter for product name
    @product_name.setter
    def product_name(self, value: str):
        self.__product_name = value

    # getter for product price, changes to float
    @property
    def product_price(self):
        return float(self.__product_price)

    # setter for product price
    @product_price.setter
    def product_price(self, value: float):
        self.__product_price = value
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KOdland,6.7.2020,Added code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes a list of object instances into a text file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want written into file:
        :return:
        """
        f = open(file_name, "w")
        # write product & price of each object to file
        for row in list_of_product_objects:
            f.write(row.product_name + "," + str(row.product_price) + "\n")
        f.close()

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_product_objects = []
        f = open(file_name, "r")
        # get the data from each line of file, use it to initialize object
        for line in f:
            prod, price = line.split(",")
            obj = Product(prod, price)
            list_of_product_objects.append(obj)  # reads a row of data
        f.close()
        return list_of_product_objects
# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Presents options to user, gets user input:

    methods:
        print_menu_tasks():
        input_menu_choice(): -> (string of user choice)
        print_products_in_list(list_of_product_objects):
        input_new_product(): -> (a product object)

    changelog: (When,Who,What)
        KOdland,6.7.2020,Created Class
    """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Existing List of Products    
        2) Add New Product to List
        3) Save to File and Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        # raise exception if user chooses a number outside of the range
        if int(choice) > 3 or int(choice) < 1:
            raise Exception
        return choice

    @staticmethod
    def print_products_in_list(list_of_product_objects):
        """ Shows the current products in the list

        :param list_of_product_objects: (list) of products you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_product_objects:
            print(row.product_name + " ($%.2f)" % row.product_price)
        print("*******************************************")

    @staticmethod
    def input_new_product():
        """ Asks user for a new task and priority to add

        :return: (object) of Product
        """
        prod = input("Enter a new product: ")
        price = float(input("Enter the price of this product: "))
        obj = Product(prod, price)
        return obj
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# If file does not exist, create it
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
except FileNotFoundError:
    print("File does not exist yet")
    print("Created new file")
    f = open(strFileName, "a")
    f.close()

while True:
    # Show user a menu of options
    IO.print_menu_tasks()

    # Get user's menu option choice
    # if user enters a number not in the menu, ask for new choice
    try:
        strChoice = IO.input_menu_choice()  # get menu option
    except:
        print("Please make a choice from 1 to 3")
        continue

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':  # print the list of products
        IO.print_products_in_list(lstOfProductObjects)  # print the list of products\
    elif strChoice == '2':  # add a new product
        # if user enters non-numeric value for price, ask for new input
        try:
            lstOfProductObjects.append(IO.input_new_product())
        except ValueError:
            print("Price should be a number")
            continue
    # let user save current data to file and exit program
    elif strChoice == '3':  # Save and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)  # write to file
        print("Data Saved")
        break  # exit
# Main Body of Script  ---------------------------------------------------- #

