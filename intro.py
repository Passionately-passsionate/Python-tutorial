# Print welcome message

message = "Hello world!"

print(message)  # How to print a message
print(len(message))  # How to identify the number of characters in a string
print(message.lower())  # How to convert all the letters to lower case?
print(message.upper())  # How to convert all the letters to upper case?
print(message.count('l'))  # How to identify the number of time something is repeated in a string?
print(message.find("ld"))  # How to find the index of a character in a string?

new_message = message.replace("world", "universe")  # How to replace a word with another word in a string

# The 'new_message' string could have been simply 'message' again
# That would have changed the message(which is now new_message) string to "Hello universe" which
# was previously "Hello world"

print(new_message)

# Using variables to print a sentence

greeting = 'Hello'
name = 'Arvind'
message = greeting + ", " + name + ". Welcome!"
print(message)

# How to use formatting to get the same result as executing line 23?

formatted_message = "{}, {}. Welcome!".format(greeting, name)
print(formatted_message)  # Achieved the same result as line 23!

# How to use f-string method to get the same result as above.
# place an f before the start of the curly brackets, and fill in the format options in the curly brackets
# Te .format step can be completely omitted. see below

f_string_message = f'{greeting}, {name}. Welcome!'
print(f_string_message)   # Acheived the same result as above!

print(type(message))  # This is a string. Hence shows type 'str'

# Numbers and Data Type
num = 2  # This is an integer
print(type(num))  # so shows the result

numb = 2.15  # This has decimal values
print(type(numb))  # Hence the data type is Float


# Arithmetic Operators:
print(3 + 2)  # Addition
print(3 - 2)  # Subtraction
print(3 * 2)  # Multiplication
print(3 / 2)  # Division
print(3 // 2)  # Floor Division  - This gives us the result without decimal points
print(3 ** 2)  # Exponent  - ** indicates ^
print(3 % 2)  # Modulus  - This gives us the remainder after division


# How to increment(add) a given number by x number?
num = 1

# method 1
num = num + 1
print(num)

# method 2
num += 1
print(num)  # Gives the result 3 beacuse num was incremented by 1 and became num = 2 above(line 62)

# How to multiply a given number x times
numb = 4

numb *= 10     # 10 times numb(4) is 40
print(numb)

# Built in functions to work with numbers:
# 1. Absolute value

print(abs(-5))  # Abs removes the negative sign and renders the absolute value

# 2. Rounding off values
print(round(7.3652))  # round function rounds off the float value to its nearest whole number.
print(round(7.3652, 1))  # You may choose to round of the value to a certain number of decimal points too
print(round(7.3652, 2))  # Rounding off to 2 decimal points


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Example for comparisons

num1 = 3
num2 = 2
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)


# Casting of a string
num_1 = '100'
num_2 = '200'

print(num_1 + num_2)  # Since the above are strings which has '', the result is concatenation

# Casting the above strings will help us to execute addition instead of concatenation
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)


# Lists, Sets and Tuples

# Lists - enclosed in square brackets
subjects = ['Science', 'Math', 'CompSci', 'Physics']
print(len(subjects))  # How to find the length/ number of items in the list?
print(subjects[0])    # Indexing can be used to call the items in the list. Indexing starts from 0 not 1
print(subjects[-1])   # [-1] calls for the last item in the list
print(subjects[0:2])  # How to call a range of values? [2nd index number is not inclusive]


# Adding new items to the list or appending

subjects.append('English')  # .append takes only one argument
print(subjects)


# Adding new item to a particular index location or inserting an item

subjects.insert(3, 'AI')
print(subjects)

# Adding a new list inside an existing list
subjects_2 = ['ML', 'DL']          # creating a new list
subjects.insert(0, subjects_2)     # inserting new list at the begining[0] of existing list
print(subjects)                    # Printing the list

# Merging both lists instead of inserting a list inside a list
subjects = ['Science', 'Math', 'CompSci', 'Physics']
subjects.extend(subjects_2)
print(subjects)


# Removing a value from the list
subjects.remove('Math')
print(subjects)

subjects.pop()  # This removes the last item of the list
print(subjects)
popped = subjects.pop()
print(popped)  # gives the value that was popped

subjects.reverse()  # sorts the list in reverse order
print(subjects)

subjects.sort()  # This sorts the list in alphabetical order
print(subjects)  # A list containing numbers will be sorted in ascending order

nums = [1, 65, 4, 9, 34, 40]
print(nums)
nums.sort()
print(nums)

subjects.sort(reverse=True)
nums.sort(reverse=True)
print(subjects)
print(nums)

# creating a sorted list without altering the list itself

subjects = ['Science', 'Math', 'CompSci', 'Physics']

sorted_subjects = sorted(subjects)  # Assigning sorted(listname) to a variable gives sorted version of list
print(sorted_subjects)

# Min, max value and sum
print(nums)
print(min(nums))  # returns the least value
print(max(nums))  # returns the highest value
print(sum(nums))  # returns the sum value of all the items in the list


# Finding the index of a value
print(subjects.index('Math'))  # gives the index of the item 'Math'
print(subjects)

# How to check if a value is in the list

print('Art' in subjects)  # 'search word' in 'list name'
print('Math' in subjects)

for value in subjects:
    print(value)


for index, value in enumerate(subjects, start=1):
    print(index, value)

print(subjects)
print(type(subjects))
subjects_str = ', '.join(subjects)   # .join(listname) is used to convert a list to string
                                     # it works only when a separator is defined first in quotes
print(subjects_str)
print(type(subjects_str))


# TUPLES - It is similar to lists but round braces are used.

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'  # Changing the value of index[0]

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#  tuple_1[0] = 'Art'

#  print(tuple_1)
#  print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
print('Physics' in art_courses)
print(cs_courses.intersection(art_courses))  # A intersection B - set operation - Common values
print(cs_courses.difference(art_courses))    # .difference returns the values that are not common in 2nd set
print(cs_courses.union(art_courses))         # Union of two sets

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

print(empty_set)
print(type(empty_set))


# Dictionary
student = {'name': 'Arvind', 'age': '25', 'course': ['Math', 'Python']}
print(student)  # Prints the whole dictionary as it is
print(student['name'])  # returns the value of the key
print(student.get('random', 'Not found'))  # Use .get to search a key-value. if it doesn's exist
                                           # the second argument will be used to display the result.
                                           # If you dont specify 'Not found', it returns a key error.

# How to add or update a key value?

student['name'] = 'Albus'      # Updates the name key
print(student)

student['phone'] = '010-0000'  # Added a new key-value
print(student)


# How to update or/and add multiple key-values at a time?

student.update({'name': 'Arvind', 'phone': '55-5555'})
print(student)


################################################################
del student['age']  # Deletes the age key value

print(student)


student['age'] = '25'       # Adding back age again
age = student.pop('age')   # When you want to retain the deleted value, use .pop
print(student)
print(age)

student['age'] = '25'
print(type(student))
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

#  student = {'name': 'Arvind', 'age': '25', 'course': ['Math', 'Python']}
for key, value in student.items():
    print(key, value)

# If else statements
language = 'Python'
if language == 'Python':
    print('Language is Python'),
else:
    print('Language not found')


language = 'Java'
if language == 'Python':
    print('Language is Python'),
elif language == 'Java':
    print('Language is Java')
else:
    print('Language not found')


# Comparisons:
a = 2
b = 3

# Equal:            ==
if a == b:
    print('equals test is true'),
else:
    print('equals test is false')

# Not Equal:        !=

if a != b:
    print('a is not equal to b')
else:
    print('a is equal to b')

# Greater Than:     >
if a > b:
    print('a is greater than b')
else:
    print('a is not greater than b')
# Less Than:        <
if a < b:
    print('a is less than b')
else:
    print('a is not less than b')
# Greater or Equal: >=
if a >= b:
    print('a is greater than or equal to b')
else:
    print('a is not greater than or equal to b')
# Less or Equal:    <=
if a <= b:
    print('a is less than or equal to b')
else:
    print('a is not less than or equal to b')
# Object Identity:  is
if a is b:
    print('a is b')
else:
    print('a is not b because the id of a and b are different and so are a and b')

# and
user = 'admin'
logged_in = True
if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')

if user == 'admin' or logged_in:
    print('admin page')
else:
    print('bad creds')

# or
user = 'admin'
logged_in = False
if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')

if user == 'admin' or logged_in:
    print('admin page')
else:
    print('bad creds')

# not

if user == 'admin' and not logged_in:
    print('Please log in')
else:
    print('welcome!')

# Object identity explained:
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # contents are equal
print(a is b)  # is looks of id and ids are not equal

print(id(a))  # Ids are different. ID is the memory space where the items are stored
print(id(b))   # hence the object identity is false

c = [2, 3, 4]
d = c

print(c == d)
print(c is d)

print(id(c))  # when a variable is assigned to another variable, they both share the same space,
print(id(d))  # Hence they have same ids and return true for object identity test.

# False Values:
    #  False
    #  None
    #  Zero of any numeric type
    #  Any empty sequence. For example, '', (), [].
    #  Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0  # Any number besides 0 is true

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = {}  # The result is false for '', (), []. It helps to check if a set or list is empty

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# Nums


nums = [1, 2, 3, 4, 5, ]

for num in nums:
    if num == 3:
        print('Found!')
        break  # break stops the for loop
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue  # Continue keeps the loop going till the end, even after the condition
    print(num)


#  An example for a loop inside a loop
for num in nums:
    for letter in 'abc':         # 'abc' is a string
        print(num, letter)


#  How to loop through a range of values? WE use an inbuilt function range

for i in range(1, 11):  # printing values between 0 and 11.
    print(i)


#  While loops:

x = 0

while x <= 10:
    print(x)
    x += 1  # This increment iteration is required to prevent an infinite loop of x = 0

x = 0
while True:
    if x == 10:
        break
    print(x)
    x += 1

                        #  FUNCTION:
#  DRY -  Do not repeat yourself!


def hello_func():
    pass


print(hello_func())

#  print(type(hello_func))

hello_func()


def new_func():
    return 'Hi Arvind.'


print(new_func())


def Arvind():
    return print({'name': 'Arvind', 'age': 25, 'Phone': 9738134289})

Arvind()

def hello_func1(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func1('Hello', name = 'Arv'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['AI', 'ML', 'Math', 'Statistics']
info = {'name': 'Arvind', 'age': 25, 'phone': 9738124289}

student_info(*courses, **info)

#  Snippet from Corey's Github

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))

print(days_in_month(2020,4))


# Importing Modules:

import module as mod

courses = ['Math', 'Science', 'Social', 'ML']

index = mod.find_index(courses,'ML')
print(index)

courses.append('Biology')
print(courses)

index = mod.find_index(courses, 'Biology')
print(index)
