## Built in functions

# In Python we have lots of built-in functions. Built-in functions are globally available for
# your use that mean you can make use of the built-in functions without importing or configuring. 
# Some of the most commonly used Python built-in functions are the following:
# _print()_, _len()_, _type()_,_int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_,
# _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()

## Variables

# Variables store data in a computer memory.Mnemonic variables are recommended to use in many programming languages. 
# A mnemonic variable is a variable name that can be easily remembered and associated.
# A variable refers to a memory address in which data is stored.
# Number at the beginning, special character, hyphen are not allowed when naming a variable.
# A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

# Python Variable Name Rules

# - A variable name must start with a letter or the underscore character
# - A variable name cannot start with a number
# - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
# - Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# Here are some example of valid variable names:
"""firstname
lastname
age
country
city"""

#Invalid variables names

"""first-name
first@name
first$name"""

# Variables in Python
first_name = 'Asa'
last_name = 'Yet'
country = 'Fin'
city = 'Hels'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'Python']
person_info = {
   'firstname':'Asa',
   'lastname':'Yet',
   'country':'Fin',
   'city':'Hel'
   }


# Let us use the _print()_ and _len()_ built-in functions. Print function takes unlimited number of arguments.
# An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

#**Example:**


print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument


#Let us print and also find the length of the variables declared at the top:

#**Example:**

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


### Declaring Multiple Variable in a Line

#Multiple variables can also be declared in one line:

#**Example:**


first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#Getting user input using the _input()_ built-in function. Let us assign the data we get from a user into first_name and age variables.
# **Example:**

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)


## Data Types

#There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

## Checking Data types and Casting

#Check Data types: To check the data type of certain data/variable we use the _type_
#**Examples:**


# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

# - Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_, _set_
#   When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

#**Examples:**

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asa'
print(first_name)               # 'Asa'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a']


## Numbers

#Number data types in Python:

"""1. Integers: Integer(negative, zero and positive) numbers
   Example:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. Floating Point Numbers(Decimal numbers)
   Example:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Complex Numbers
   Example:
   1 + j, 2 + 4j, 1 - 1j
"""