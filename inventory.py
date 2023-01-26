#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost

        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity

        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f'''A shoe object :
        Country : {self.country}
        Code : {self.code}
        Product : {self.product}
        Cost : {self.cost}
        Quantity : {self.quantity}
'''

        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            file.readline()
            # add an object in the list
            for s in file.readlines():
                shoe_pointer = list(s.split(','))
                shoe_pointer[3] = int(shoe_pointer[3])
                shoe_pointer[4] = int(shoe_pointer[4])
                shoe_list.append(
                    Shoe(shoe_pointer[0], shoe_pointer[1], shoe_pointer[2], shoe_pointer[3], shoe_pointer[4]))
    except FileNotFoundError as error_code:
        print('No file found.\n')
        print(error_code)

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

# I create this method in order to update the txt file.
def write_shoes_data():
    with open('inventory.txt', 'w', encoding='utf-8') as file:
        file.write('Country,Code,Product,Cost,Quantity\n')
        for i in shoe_list:
            file.write(f'{i.country},{i.code},{i.product},{i.cost},{i.quantity}\n')
    print('File updated.\n')

def capture_shoes():
    user_country = input('Country : ')
    user_code = input('Code : ')
    user_product = input('Product : ')
    user_cost = int(input('Cost : '))
    user_quantity = int(input('Quantity : '))
    shoe_list.append(Shoe(user_country, user_code, user_product, user_cost, user_quantity))
    write_shoes_data()
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    for i in shoe_list:
        print(i)
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    # set a temporary variable to store the slot number of shoe_list at lowest[0] and the lowest quantity number at lowest[1].
    # this loop is to find out the lowest quantity value in the shoe_list
    lowest = [0, 999999]
    for c, i in enumerate(shoe_list):
        if i.quantity < lowest[1]:
            lowest[1] = i.quantity
            lowest[0] = c

    # this loop find out all shoe with the lowest quantity in case there are multiple item with same lowest quantity.
    print('Below is the shoe with the lowest quantity')
    lowest_list = []
    for c, i in enumerate(shoe_list):
        if i.quantity == lowest[1]:
            lowest_list.append([c, i.quantity])
    # display all shoes with the lowest quantity
    for i in lowest_list:
        print(f'Shoe ID {i[0]+1}')
        print(shoe_list[i[0]])

    # re-stock selectively for a particular shoe
    action = input('Would you like to re-stock it ? (Y/N) ').lower()
    if action == 'y':
        if len(lowest_list) == 1:
            quantity = int(input('What is the max stock ? '))
            shoe_list[lowest[0]].quantity = quantity
            write_shoes_data()
        else:
            shoe_id = int(input('What shoe you would like to re-stock ? '))
            quantity = int(input('What is the max stock ? '))
            shoe_list[shoe_id-1].quantity = quantity
            write_shoes_data()
    elif action == 'n':
        pass
    else:
        print('Wrong input.\n')
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    search_found = False
    search_code = input('Please provide shoe code (exactly match) : ')
    for c, i in enumerate(shoe_list):
        if search_code.find(i.code) == -1:
            pass
        else:
            print(shoe_list[c])
            search_found = True
    if search_found == False:
        print('No match found.\n')

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for i in shoe_list:
        print(i)
        print(f'The total value of shoe : {i.cost * i.quantity}\n')
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    # set a temporary variable to store the slot number of shoe_list at highest[0] and the highest quantity number at highest[1].
    # this loop is to find out the highest quantity value in the shoe_list
    highest = [0, 0]
    for c, i in enumerate(shoe_list):
        if i.quantity > highest[1]:
            highest[1] = i.quantity
            highest[0] = c

    # this loop find out all shoe with the lowest quantity in case there are multiple item with same lowest quantity.
    print('Below is the shoe with the highest quantity')
    highest_list = []
    for c, i in enumerate(shoe_list):
        if i.quantity == highest[1]:
            highest_list.append([c, i.quantity])
    # display all shoes with the lowest quantity
    for i in highest_list:
        print(f'Shoe ID {i[0] + 1}')
        print(shoe_list[i[0]])

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
read_shoes_data()
while True:
    user_input = input('''Please select operator :
    1 - View all shoes
    2 - View all shoes' stock value
    3 - View sale suggestion with highest stock quantity
    4 - Search shoe by shoe code
    5 - Add new shoe
    6 - Re-stock shoe
    7 - Exit programme
    Operator : ''')
    print()
    if user_input == '1':
        view_all()
    elif user_input == '2':
        value_per_item()
    elif user_input == '3':
        highest_qty()
    elif user_input == '4':
        seach_shoe()
    elif user_input == '5':
        capture_shoes()
    elif user_input == '6':
        re_stock()
    elif user_input == '7':
        exit()
    else:
        print('Wrong input\n')

'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''