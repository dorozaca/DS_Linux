#mutant - set/lis/dict
#Important Keywords: IN, CONTINUE, BRAKE, NOT, GLOBAL, RAISE
#Range (number generator), Slice (works with indexes), for i in list (i takes the value of each element temporarily)
# *args (unpacks positional arguments into a tuple), **kwargs (unpacks keyword arguments into a dictionary)
#Comprehension for TUPLES need keyword tuple at the start, otherwise they are GENERATORS 


#****************************************************************************************************************************************************************

#1. DATA TYPES

#Integers
-267236
76373

#Floats
2727.3
-9.7

#Strings, using single or double quotes is fine
'hello' 
"hello"
'4.6'
#if we want to embed a double quotation or single quotation mark in a string, we use the backslash or  we wrap the string in the other type of quotation marks
"'hello'"
'"hello"'

#Boolean 
True 1
False 0

#****************************************************************************************************************************************************************

#2. OUTPUT AND PRINTING

print('Hello World!')
print(4.5)
print("Hello",'end',87,False)
print('Hello','end',87,False,sep='|') #sep is the separator between the arguments
print('Hello','end',87,False,sep='|',end='\n') #end is the end of the line 

print('Hello','end',87,False,end='|') #end is the end of the line and it won't go to the next line, it will merge with the next print statement being the result: Hello end 87 False|Hello 
print('Hello')

#****************************************************************************************************************************************************************

#3. VARIABLES

hello = 'tim'
world = 'Mars'
world = 'hello'
print(hello,world)
#Variable convention is snake_case
hello_world = 'tim' #separate words with underscores, always lowercase

#****************************************************************************************************************************************************************

#4. INPUT

name = input('Tell your Name: ')
age = input('Tell your Age: ')
print('Hello',name,'you are',age,'years old')


def add(a,b):
    return a+b  #return is the output of the function   

print(add(5,6))


#Arithmetic Operators 12:40
x = 9
y = 3.5
result = x + y
result1 = x - y
result2 = x * y
result3 = x / y
print(result)
#we can convert the result to an integer
result4 = int(x / y)

#Exponentiation
result5 = x ** y #x to the power of y

#Integer result of division
result6 = x // y

#Remainder of division (modulo)
result7 = x % y

#Order of Operations
#BEDMAS: brackets, exponents, [division, multiplication], [addition, subtraction] those operations in the square brackets have the same precedence, so we evaluate them from left to right

#Using input to get numbers from the user
x = input('Enter a number: ')
print(x-1) #this will give an error because the input is a string

#we can convert the input to an integer
x = int(input('Enter a number: '))
print(x-1)

#we can convert the input to a float
x = float(input('Enter a number: '))
print(x-1)

#****************************************************************************************************************************************************************
#5. STRING METHODS

hello = 'hello'
print(type(hello)) #this will tell us that the hello is an instance of the string class

hello = 'hello'.upper() #this will convert the string to uppercase
print(hello.upper()) #this will convert the string to uppercase as well

hello = 'heLLO '
print(hello.lower()) #this will convert the string to lowercase
print(hello.capitalize()) #this will capitalize the first letter of the string
print(hello.count("l")) #this will count the number of times the letter l appears in the string
print(hello.find("l")) #this will find the index of the first letter l in the string
print(hello.replace("l","z")) #this will replace all the letter l in the string with the letter z
print(hello.lower().count("ll")) #this will convert the string to lowercase and count the number of times the letter ll appears in the string IMPORTANT!

#****************************************************************************************************************************************************************

#6. STRING CONCATENATION (ADDITION), MULTIPLICATION

x = 'hello'
y = 3
print(x * y) #this will print hello 3 times when the integer is on the right side
y = 'yes'
print(x + y) #this will print "helloyes" when the string is on the right side (concatenation)

#****************************************************************************************************************************************************************

#7. CONDITIONAL OPERATORS (>, <, ==, !=, <=, >=)

== #equal to
!= #not equal to
<=  #less than or equal to
>=  #greater than or equal to

#****************************************************************************************************************************************************************

#CONDITIONAL STRINGS (using ASCII values for strings) 

x = "hello"
y = 'hello'
print(x == y) #this will print True because the strings are equal
print(x != y) #this will print False because the strings are equal
print('a' > 'Z') #this will print True because the letter a is greater than the letter Z in ASCII
print(ord('a')) #this will print the ASCII value of the letter "a" IMPORTANT!
print('ab' > 'b') #It will start by comparing the characters at the same index (right to left) and if they are equal, it will move to the next index.

#Conditional Numbers 
print(7.0 == 7) #this will print True because the numbers are equal
print(7.0 != 7) #this will print False because the numbers are equal

result = 6 == 6
print(result) #this will print True because the numbers are equal

#****************************************************************************************************************************************************************

#8. CHAINED CONDITIONALS (AND, OR, NOT)

x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2 #It works as if x + 2 is in brackets
#IMPORTANT, all logical operators have lower precedence than arithmetic operators, # so in the following example, arithmetic operators will be evaluated first at each side of the logical operator
result4 = x + 2 > y - 1

#All previous results are boolean values, so we can use them with keywords like 
# AND, 
# OR, 
# NOT to chain them together

result5 = result1 and result2
print(result5) #this will print False because the first result is False

# "NOT" will reverse (flip) the boolean value that is on the right side of keyword "not"
result6 = result1 or not result2 or result
print(not True) #this will print False
print(not (False or True)) #this will print False because the result of the brackets is True (when we have "False OR True" because at least one of the operands is True) and the "not" will reverse it to False
print(not (False and True))#this will print True because the result of the brackets is False (when we have "False AND True" is False because we need both operands to be True in order to be True) and the "not" will reverse it to True

#When we have statements with multiple keywords, This is the order of precedence: NOT, AND, OR IMPORTANT!
print(not False and True or True) #this will print True because the "not" will reverse the False to True, then the "and" will evaluate the first operand AND second operand together to "TRUE", then the "or" will evaluate the second operand to True, so the final result is True

#****************************************************************************************************************************************************************

#9. IF/ELSE/ELIF Statements

x = input('Name: ')

if x == 'tim':
    print('Hello',x)

elif x == 'joe':          #We can add as many elifs as we want bur all elif must come after "IF" and before "ELSE" IMPORTANT!
    print('Hello',x)

else:
    print('Hello, stranger')

#we can also use the elif statement without the else statement, that is valid
if x == 'tim':
    print('Hello',x)

elif x == 'joe':        
    print('Hello',x)

elif x == 'Sarah':        
    print('Hello',x)

#Collections
    #Collections are data structures that can hold multiple values (ordered or unordered)


#****************************************************************************************************************************************************************

#10. LISTS (MUTABLE, Multiple data type, ordered) - append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy
#Lists are mutable, which means that we can change the values of the list. It keeps a reference to the same object in memory, but the values can change, not a copy of the object

x = [4,True,'hi']
y = 'hi'
print(len(x), len(y)) #this will print 3 and 2 because the length of the list is 3 and the length of the string is 2

x.append('bye') #this will add the string bye to the end of the list -> x = [4,True,'hi','bye']
print(x)

x.extend([4,5,5,5,5,5,5,5,5,8]) #this will add the list [4,5,5,5,5,5,5,5,5,8] to the end of the list -> x = [4,True,'hi','bye',4,5,5,5,5,5,5,5,5,5,8]
print(x)

x.pop()#this will remove the last element of the list -> x = [4,True,'hi','bye',4,5,5,5,5,5,5,5,5,5]
print(x)

x.pop(0)#this will remove the element at index 0 of the list which is for. Fist index in list is always 0 -> x = [True,'hi','bye',4,5,5,5,5,5,5,5,5,5]
print(x)
print(x[1]) #this will print the element at index 1 of the list which is 'hi'

x[0] = 'Toto'
print(x) #this will replace the element at index 0 of the list which is True with 'Toto' -> x = ['Toto','hi','bye',4,5,5,5,5,5,5,5,5,5]

#IMPORTANT Mutability and how to copy a list
x = [4,5,6,7,8,9,10]
y = x
x[0] = 'hello'
print(x) #this will print ['hello',5,6,7,8,9,10]
print(y) #this will print ['hello',5,6,7,8,9,10] because y is a reference (pointer) to x, so when we change x, y will change too

x = [4,5,6,7,8,9,10]
y = x[:] #this will create a copy of x and assign it to y, not a reference to x
x[0] = 'hello'
print(x) #this will print ['hello',5,6,7,8,9,10]
print(y) #this will print [4,5,6,7,8,9,10] because y is a copy of x, so when we change x, y will not change

#****************************************************************************************************************************************************************

#11. TUPLE (IMMUTABLE, Multiple data type, ordered) 2 Methods: count() and index()

#Tuples are immutable, can't be changed once we defined them. We can't append, remove, pop, extend, etc. We can only access the elements of the tuple
#It is an "immutable list"

# Create a tuple
t = (1, 2, 3, 2, 4, 5)

# Use the count() method to count the number of occurrences of the value 2
count = t.count(2)
print(count)  # Output: 2

# Use the index() method to find the index of the first occurrence of the value 4
index = t.index(4)
print(index)  # Output: 4

x = (0,0,2,2)
print(x[0]) #this will print 0
x[0] = 5 #this will give an error because we can't change the values of a tuple

y = x + (5,6,7) #this will create a new tuple and assign it to y
print(y) #this will print (0,0,2,2,5,6,7)

#****************************************************************************************************************************************************************

#12. FOR LOOPS - we use them to iterate over a collection (LIST, TUPLE, STRING, DICT, etc.) - 

#for i in dogs, here i will iterate whatever is dogs, let's assume is a list of dog's names, so i will temporarily take the name of each dog in the list during each cycle of the loop. 
# "range(len(x))"" and "enumerate(x)"" are very useful, 
# but remember that RANGE = NUMBER GENERATOR (DOESN'T INCLUDE THE STOP);  SLICE OPERATOR works with INDEXES (CONSIDERS SPACES into INDEX COUNT AND DOESN'T RETRIEVE THE VALUE AT THE STOP INDEX), <== IMPORTANT!
                  # FOR LOOP "i" takes the VALUE OF EACH ELEMENT in the list, tuple, string, etc. as in the example below:                                                               

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
for i in pairs:
    print(f"The number {i[0]} is spelled {i[1]}") #this will print The number 1 is spelled one, The number 2 is spelled two, The number 3 is spelled three



#Main difference with While loops is that while loops run an indefinite number of times based off on a condition, whereas for loops run a definite number of times

for i in range(10): #this will print the numbers from 0 to 9, not including 10, "i" is our counter
    print(i)

#Range(start, stop, step) - IMPORTANT SLICE vs RANGE!

#IMPORTANT, the range function is a GENERATOR, it generates the numbers from 0 to 9, not including 10, so it doesn't store them in memory, it generates them on the fly
#IMPORTANT, If we only provide one argument, it will be the stop, and the start will be 0, and the step will be 1
#IMPORTANT, If we provide two arguments, the first will be the start and the second will be the stop, and the step will be 1



for i in range(1,11):
    print(i) #this will print the numbers from 1 to 10, not including 11

for i in range(10,-1,-1): #this will print the numbers from 10 to 0, not including -1, with a step of -1
    print(i)

#THIS WHY AND HOW WE COMBINE RANGE and LEN - looping through a list
for i in [1,2,3,4,5,88,99,100]:
    print(i) #this will print all the elements of the list

#keeping track of the index
x = [3,42,12,19,30]

print(len(x)) #this will print the number 5 which is the length of the list x
print(range(len(x))) #this will print the range(0,5), which ara numbers from 0 to 4, not including 5

#this is how we loop through a list by keeping track of the index
for i in range(len(x)): 
    print(x[i]) #this will print all the elements of the list x

#Another way to loop through a list
for i, element in enumerate(x):#Enumerate is a function that takes a list and returns a tuple with the index and the element of the list
    print(i, element) #this will print the index and the element of the list x

#****************************************************************************************************************************************************************

#13. WHILE LOOPS (While TRUE, BREAK, CONTINUE)

i = 0
while i <10:
    print(i, 'run')
    i += 1 #this is the same as i = i + 1

#Using break and continue
i = 0
while True:
    print(i, 'run')
    i += 1
    if i == 10:
        break #this will stop the loop when i is equal to 10


# Using continue in a while loop
#The continue statement is used the skip even numbers and only print odd numbers.
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue # this will skip the rest of the loop and go back to the beginning, so it will skip the print statement
    print(i)


#****************************************************************************************************************************************************************

#14. SLICE OPERATOR

#Slice operator is used to get a subset of a list, tuple, string, etc anything that uses indexes (iterable)
#It considers spaces within index count. Doesn't include the value at the stop index
 
 x = [0,1,2,3,4,5,6,7,8,9]
 
 #sliced = x[start:stop:step] - IMPORTANT SLICE vs RANGE!
#Those numbers within the brackets are INDEXES, not numbers, so the first index is 0, the second is 1, etc.

sliced = x[0:4:2] #This will print 0 and 2, not including 4, with a step of 2
print(sliced)

sliced = x[:] #This will copy the whole list and assign it to sliced
sliced = x [2:] #This will copy the list from index 2 to the end and assign it to sliced
sliced = x[4:2:-1]#This will copy the list from index 4 to index 2, not including 2, with a step of -1
sliced = x[::-1]#This will reverse the list and assign it to sliced IMPORTANT!

mystring = 'hello world'
sliced = mystring[::2] #This will print 'hlowrd' because it will print every other character of the string, with a step of 2
sliced = mystring[2:] #This will print 'llo world' because it will print the string from index 2 to the end
sliced = mystring[2::2]#This will print 'lowrd' because it will print the string from index 2 to the end, with a step of 2
sliced = mystring[:3:]#This will print 'hel' because it will print the string from index 0 to index 3, not including 3


#****************************************************************************************************************************************************************
#15. SETS - MUTABLE unordered, unique elements, multi data type collection (add, remove, union, intersection, difference, etc.)

#Sets are unordered, so we can't access the elements by index, and they are mutable, so we can add and remove elements from them
#IN A SET WE ONLY CARE IF AN ELEMENT IS IN THE SET OR NOT, we don't care about the order of the elements
# Sets are extremely fast to do what's called lookups, additions, and removals.

x = set() #For empty sets we have to use the set function, we can't use the curly braces. It is a constructor
s = {4,32,2,2} #This is a SET LITERAL, it is the same as X = set([4,32,2,2])
#however:
print(type({})) #this will print <class 'dict'>, so we can't use the curly braces to create an empty set, we have to use the SET function
print(s) #this will print {32, 2, 4}, it will remove the duplicate 2 and sort the elements by default which is random every time we run the code

s.add(5) #this will add the number 5 to the set
s.remove(32) #this will remove the number 32 from the set
print(4 in s) #this will print True because 4 is in the set

#Testing speed between lists and sets
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = [1,2,3,4,5,6,7,8,9,10]
s3 = {20,30,40,50,60,70,80,90,100}

print(2 in s1) #this will print True, it is very fast
print(2 in s2) #this will print True, it is very slow, because it has to go through the whole list to find the number 2

print(s1.union(s3)) #this will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 70, 40, 80, 50, 20, 90, 60}, it will combine the two sets and remove the duplicates
print(s1.intersection(s3)) #this will print {80, 50, 20, 90, 60, 70, 40}, it will print the elements that are in both sets
print(s1.difference(s3)) #this will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, it will print the elements that are in s1 but not in s3

#****************************************************************************************************************************************************************

#16. DICTIONARIES - MUTABLE, unordered (however there is "ordered dicts" which are a subclass), key-value pairs, multi data type collection (add, remove, update, items(), keys(), values().)

x = {'key1': 'value1', 'key2': 'value2'} #This is a dictionary literal, it is the same as x = dict(key1='value1', key2='value2')
print(x['key1']) #this will print 'value1', we can access the value by using the key

x['key3'] = 'value3' #this will add a new key-value pair to the dictionary
x[2] = 8 #we can use numbers as keys, anything can be a key, but we can't use lists or dictionaries as keys. We can use tuples as keys.
print(x) #this will print {'key': 'value', 'key2': 'value2', 'key3': 'value3', 2: 8}

x[3] = [2,3,4] #we can use lists as values
print(x) #this will print {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 2: 8, 3: [2, 3, 4]}

print('key1' in x) #this will print True, it will check if the key is in the dictionary'
print(x.values()) #this will print dict_values(['value1', 'value2', 'value3', 8, [2, 3, 4]]), it will print all the values in the dictionary
print(list(x.values())) #this will print ['value1', 'value2', 'value3', 8, [2, 3, 4]]. It prints all the values in the dictionary as a list
print(list(x.keys())) #this will print ['key1', 'key2', 'key3', 2, 3], it will print all the keys in the dictionary as a list

del x['key1'] #this will delete the key-value pair from the dictionary

for key, value in x.items(): #this will print all the key-value pairs in the dictionary
    print(key, value)

for key in x:
    print(key, x[key]) #this will print all the key-value pairs in the dictionary as well. It is the same as the previous for loop

#****************************************************************************************************************************************************************

#17. COMPREHENSIONS - A way to create a list, set, or dictionary in a single line of code vs GENERATORS

#we define a for loop inside a list, whatever we have on the left of the "for" keyword is what we want to add to the list.
x = [x for x in range(5)] #this will create a list with the numbers from 0 to 4, not including 5
print(x) #this will print [0, 1, 2, 3, 4]

x = [x + 5  for x in range(5)] #this will create a list with the numbers from 5 to 9, not including 10
x = [x % 5 for x in range(5)] #this will create a list with the numbers from 0 to 4, not including 5
x = [0 for x in range(5)] #this will create a list with 5 zeros
x = [[0 for x in range(100)]for x in range(5)]#this will create a list with 100 zeros, 5 times
x = [i for i in range(100) if i % 5 == 0] #this will create a list with the numbers from 0 to 99, not including 100, but only the numbers that are divisible by 5

x = {i:0 for i in range(100) if i % 5 == 0} #this will create a DICTIONARY with the keys that would be numbers from 0 to 99, not including 100, but only the numbers that are divisible by 5, and the values will be 0

x  = {i for i in range(100) if i % 5 == 0} #this will create a SET with the numbers from 0 to 99, not including 100, but only the numbers that are divisible by 5

x = (i for i in range(100) if i % 5 == 0) #this will create a GENERATOR with the numbers from 0 to 99, not including 100, but only the numbers that are divisible by 5
print(x) #this will print <generator object <genexpr> at 0x0000020F4F6F4C80>, it is a generator object, so we can't print it, we have to iterate over it

x = tuple(i for i in range(100) if i % 5 == 0) #this will create a TUPLE with the numbers from 0 to 99, not including 100, but only the numbers that are divisible by 5

#*****************************************************************************************************************************************************************

#18. FUNCTIONS - def, return, arguments, parameters, default parameters, keyword arguments, unpacking arguments, scope, lambda functions, docstrings

def func(): #this is the function definition, it is not executed until we call it
    print('Hello World')

func() #this is the function call, it will execute the function


def func():
    print('Hello World')
    def func():#This is a nested function, it is not executed until we call it
        print('h')
    func() #this is the function call, it will execute the nested function

func() #this will print 'Hello World' and 'h'


def func(x,y):
    print('run', x, y)'
    
func(5,6)#this will print 'run 5 6'


def func(x,y):
    print('run', x, y)
    return x * y, x / y

print(func(5,6))#this will print 'run 5 6' and (30, 0.8333333333333334), it will return a tuple with the results of the multiplication and division
r1, r2 = func(5,6) #this will assign the results of the function to r1 and r2 
print(r1, r2) #this will print 30 0.8333333333333334 outside of the tuple


def func(x,y, z=None): #z is a default parameter, if we don't provide a value for z, it will be None
    print('run', x, y)
    return x * y, x / y

r1, r2 = func(5,6,7) #this will assign the results of the function to r1 and r2 and override the default value of z

#functions are objects, so we can pass them around. INVESTIGATE CLOSURE <=Only topic not covered in the course
def func(x):
    def func2():
        print(x)

    return func2

print(func(3))  #this will print <function func.<locals>.func2 at 0x0000020F4F6F4D08>, it is a function object, so we can't print it, we have to call it. It is saying that func2 is a local function inside func
print(func(3)()) #this will print 3 and None, because func2 doesn't return anything, so it returns None

x = func(3)
x() #this will print 3 because x is a function object, so we can call it.
#****************************************************************************************************************************************************************

#19. UNPACK OPERATOR - *args, **kwargs

#We use the unpack operator to unpack a list, tuple, set, dictionary, etc. into individual arguments
# One * is for a list or tuple, ** is for a dictionary


def func(*args **kwargs):
    pass

x = [1,23,236363, 2727]
print(*x) #this will print 1 23 236363 2727, it will unpack the list into individual arguments (separated by spaces as if we printed them individually)
print(x) #this will print [1, 23, 236363, 2727], it will print the list as it is


def func(x,y):
    print(x,y)   

pairs = [(1,2), (3,4), (5,6)]]

for pair in pairs:
    func(pair[0], pair[1]) #this will print 1 2, 3 4, 5 6 ; But this is not pythonic, we can do it better 

for pair in pairs:
    func(*pair) #this will print 1 2, 3 4, 5 6 ; This is pythonic, it is better

func(**{'x':2, 'y':5})#this will print 2 5, it will unpack the dictionary into individual arguments (separated by spaces as if we printed them individually)
func(**{'y':5, 'x':2})#this will print 2 5, it doesn't matter the order of the keys in the dictionary as long as keys match the parameter names of the function


def func(*args, **kwargs): #This is a function for which we don't know how many arguments (positional or keyword) we are going to pass to it
    print(args, kwargs)

func(1,2,3,4,5,one=1, two=2, three=3) #this will print (1, 2, 3, 4, 5) {'one': 1, 'two': 2, 'three': 3}, it will unpack the positional arguments into a tuple and keywords into a dictionary

#If we want to use the previous individually results we need to unpack them:
def func(*args, **kwargs):
    print(*args)

func(1,2,3,4,5,one=1, two=2, three=3)#This will print 1 2 3 4 5 because print(*args) will unpack positional arguments only.

def func(*args, **kwargs):
    print(**kwargs)

func(1,2,3,4,5,one=1, two=2, three=3)#This will give an error saying 'one' is an invalid keyword argument
#because when unpacking it will take the keywords to the print statement as arguments, so it will be like print(one=1, two=2, three=3), which is not valid.
#This would be valid print("one", 1, "two", 2, "three", 3), but it is not the case.

#How to unpack keywords only so the output is 1 2 3 in one line?
def func(*args, **kwargs):  
    print(*kwargs.values()) #this will print 1 2 3      

func(1,2,3,4,5,one=1, two=2, three=3) #this will print 1 2 3    

#****************************************************************************************************************************************************************

#20. SCOPE - global, local, nonlocal


x = 'tim' #This is a global variable, it is available everywhere in the code

def fun(name):
    x = name #this is a local variable, it is only available inside the function

print (x) #this will print 'tim'
func('Diego')
print(x) #this will print 'tim' because the variable x inside the function is local, so it is not available outside the function

#There is a workaround by using the keyword "global"
x = 'tim' #This is a global variable, it is available everywhere in the code

def func(name):
    global x #this will make the variable x global, so it will be available outside the function (not recommended)
    x = name #this is a local variable, it is only available inside the function    

print (x) #this will print 'tim'
func('Diego')
print (x) #this will print 'Diego' because the variable x inside the function is global, so it is available outside the function

#****************************************************************************************************************************************************************

#21. EXCEPTIONS 

raise Exception('This is an error') #this will raise an exception and stop the program. It will say "Exception: This is an error"


#****************************************************************************************************************************************************************

#22. HANDLING EXCEPTIONS - try, except, finally

try:
    x = 7/0
except Exception as e: #this will catch the exception and assign it to the variable e 
    print(e) #this will print "division by zero" and it won't stop the program

x =  7/0 #this will raise an exception and stop the program. It will say "ZeroDivisionError: division by zero"


try:
    x = 7/0
except Exception as e: #this will catch the exception and assign it to the variable e 
    print(e) #this will print "division by zero" and it won't stop the program
finally:
    print('finally') #this will print "finally" and it won't stop the program, it could  help us to close a file or a database connection, etc.

#****************************************************************************************************************************************************************

#23. LAMBDA FUNCTIONS.

#Lambda functions are anonymous functions, they don't have a name, they are used to create functions on the fly, they are used to pass functions as arguments to other functions

x = lambda x: x + 5 #this is a lambda function, it is the same as def x(x): return x + 5
print(x(2)) #this will print 7

x = lambda x, y: x + y #this is a lambda function, it is the same as def x(x, y): return x + y
print(x(2, 32)) #this will print 34

#****************************************************************************************************************************************************************

#24. MAP AND FILTER FUNCTIONS
x = [1, 21, 5, 63, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mp = map(lambda i: i + 5, x) #this will add 5 to each element of the list x
#map return an object of type map, we could iterate over it, but converting it to a list is more useful
print(list(mp)) #this will print [6, 26, 10, 68, 7, 8, 9, 10, 11, 12, 13, 14, 15]

mp = filter(lambda i: i % 2 == 0, x) #this will filter the even numbers of the list x. The lambda function will return True or False, so then FILTER can keep the elements that return True only
print(list(mp)) #this will print [2, 4, 6, 8, 10]

#Another way without using lambda functions
def my_function(i):
    return i % 2 == 0

mp = filter (my_function,x)
print(list(mp)) #this will print [2, 4, 6, 8, 10]

#****************************************************************************************************************************************************************

#25. F STRING - f"{}"

tim = 2000
x = f'hello {6 + 8} {tim} {67 +9}'
print(f'hello {tim}')



















