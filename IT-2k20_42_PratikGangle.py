#qustion No 1
# print hello world

print("Hello world")


#qustion No 2
#how to define variable in the python
a ="pratik"
b = 345
c = 45.32
d = True
 #d = None


#  Printing the variables
print(a)
print(b)
print(c)
print(d)

# Printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#typecasting in python
a = "5"
a = int(a)
print(type(a))
print(a + 5)

#input function in python
a = input("Enter a number: ")
a = int(a) # Convert a to an Integer(if possible)
print(type(a))

#add two number in python
a = 30
b = 15
print("The sum of a and b is", a + b)


#remainder of two number
a = 458
b = 15

print("The remainder when a is divided by b is", a%b)

#average of two number
a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)
avg = (a + b)/2
print("The average of a and b is", avg)

#string in python
# b = "Pratik" # --> Use this if you have single quotes in your strings
# b = 'Pratik"s'
b = '''Pratik"s and 
       Pratik's '''
print(b)
# print(type(b))

#string slicing in python
name = "Pratik"
 #print(name[4])
# name[3] = "d" --> Does not work

 #print(name[1:4])
 #print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
 #c = name[-4:-1] # is same is name[1:4]
# print(c)

name = "Pratik"
# d = name[0::3]
d = name[:0:-1]
print(d)

#string functions
story = "once upon a time  "

# String Functions
# print(len(story))
# print(story.endswith("upon"))
# print(story.count("c"))
# print(story.capitalize())
# print(story.find("upon"))
print(story.replace("time", "times"))

#escape sequences
story = "Pratik is good.\nHe\tis ve\\ry good"
print(story)



# write a python program to display a user entered name followed by good aftermoon using input() function

name = input("Enter your name\n")
print("Good Afternoon, " + name)

# write a program to fill in a letter template given below with name and date
# letter = ''' dear </Name/>
# 		you are selected!
# 			<date>
letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

# write a program to deted double space in a string
st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)
# replace the double space from problem (upper question) with single space
st = "This is a string with double  spaces  ok"
st = st.replace("  ", " ")
print(st)

# write a program to format the following letter using escape sequence characters
# letter = "dear Pratik, how are you!"
letter = "Dear Pratik, how are you!"
print(letter)

formatted_letter = "Dear Pratik,\n\t how are you!\nThanks!"
print(formatted_letter)


# loops in python

# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

    # Write a Python program which iterates the integers from 1 to 50. For multiples of #three print "Fizz" instead of the number and for the multiples of five print #"Buzz". For numbers which are multiples of both three and five print "FizzBuzz
  
   for fizzbuzz in range(51):  
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

#Write a Python program to create the multiplication table (from 1 to 10) of a number.
n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)


#    while loops
#  Write a program to print the following using while loop
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

num = 2
while(num<=20):
   print(num)
   num = num + 2

# b)

num = 1
while(num<=20):
   print(num)
   num = num + 2

# c)

num = 1
while(num<=10):
   print(num)
   num = num + 1

# d)

num = 0
while(num<10):
   print(num)
   num = num + 1

# Write for loop statement to print the following series:
# 10, 20, 30 … … 300
num = 10
while (num <= 300) :
    print(num, end = " , ")
    num = num +10

    # Write a program to print first 10 natural number in reverse order using while loop.
    num = 10
while num >= 1:
     print(num)
     num= num - 1

    #  Write a program to print sum of first 10 Natural numbers.
    num = 10
sum = 0
while num >= 1:
   sum = sum + num
   num= num - 1
print(sum)

# Write a program to print sum of first 10 Even numbers.
num = 2
sum = 0
while num <= 20:
   sum = sum + num
   num= num + 2
print(sum)

# Write a program to print table of a number entered from the user.
i = 1
num = int(input("Enter any number  : "))
while i <= 10:
    print(num," * ",i," = ", num * i)
    i = i+1

#  Write a program to check whether a number is prime or not using while loop.
num1 = int(input("Enter any number : "))
k=0
if num1 == 0 or num1 == 1:
    print("Not a prime number ")
else:
   i = 2
   while(i<num1):
     if num1 % i == 0:
       k = k+1
     i = i+1
if k == 0 :
        print( num1,"is prime number")
else:
        print(num1, "is not prime number")

        # Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.
        n = int(input("How many terms you want in Fibonacci Series  : "))
if n==1:
      print("1")
elif n == 2:
      print("1, 1")
elif n <= 0:
      print("Please enter positive number greater than 0")
else:
      ft = 1
      st = 1
      print(ft,end=" ")
      print(st,end=" ")
      i = 2
      while(i<n):
           nt = ft + st
           print(nt,end = " ")
           ft = st
           st = nt
           i = i + 1

        #    Write a program to find the HCF of two numbers entered from the user.
        num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
rem = 1
if num1 > num2 :
   while rem!=0:
     rem = num1 % num2
     if rem == 0:
         hcf = num2
     else:
         num1 = num2
         num2 = rem
else :
   while rem!=0:
     rem = num2 % num1
     if rem == 0:
         hcf = num1
     else:
         num2 = num1
         num1 = rem
print("HCF of two numbers is  : ", hcf)





#    if else 
#. Write a program to check whether a number entered by user is even or odd.

num=int(input("Enter your age"))
if num%2==0:
   print("Number is Even")
else:
   print("Number is Odd")

#    Write a program to check whether a number is divisible by 7 or not.
num=int(input("Enter your age"))
if num%7==0:
   print("Number is divisible")
else:
   print("Number is not divisible")

#    Write a program to check whether an years is leap year or not.yr=int(input("Enter the year"))
if yr%100==0:
    if yr%400==0:
          print("Entered year is leap year")
    else:
          print("Entered year is not a leap year")
else:
    if yr%4==0:
         print("Entered year is leap year")  
    else:
        print("Entered year is not a leap year")


# Write a program to check whether a person is eligible for voting or not.(voting age >=18)
 age=int(input("Enter your age"))
if age >=18:
    print("Eligible for Voting")
else
    print("Not eligible for voting")


    # Write a program to check whether a person is senior citizen or not.
    age=int(input("Enter your age"))
if age >=60:
    print("Senior Citizen")
else
    print("Not a Senior Citizen")


    # Write a program to find the largest number out of two numbers excepted from user
    num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
if num1 > num2:
     print("greater number is :", num1)
else:
     print("greater number is :", num2)

    #  Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
    num1 = int(input("Enter first number"))
if num1%2==0 and num1%3==0:
      print("Number is divisible by 2 and 3 both")
else:
      print("Number is not divisible by both")


    #    Write a program to find the largest number out of three numbers excepted from user.
    num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
      print("Greatest number is ", num1)
if num2 > num1 and num2 > num3:
      print("Greatest number is ", num2)
if num3 > num2 and num3 > num1:
     print("Greatest number is ", num3)

#  Rock, Paper, Scissors game
     if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
   

   #Write a Python program to construct the following pattern, using a nested loop number
#    1                               
# 22
# 333
# 4444
# 55555  
# 666666 
# 7777777   
# 88888888
# 999999999 

   for i in range(10):
    print(str(i) * i)



# function
# Write a Python function to find the Max of three numbers.
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))


# Write a Python program to reverse a string
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

# Write a Python function that takes a number as a parameter and check the number is prime or not.
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))

# Write a Python function that checks whether a passed string is palindrome or not
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 


#list
# Create a list using []
a = [1, 2 , 4, 56, 6]

# Print the list using print() function
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])

# Change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Pratik", False, 6.9]
print(c)


#list slicing
friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:4])
print(friends[-4:])

#list mehods
l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# l1.sort() # sorts the list
# l1.reverse() # reverses the list
#l1.append(45) # adds 45 at the end of the list 
# l1.insert(2, 544) # inserts 544 at index 2
# l1.pop(2) # removes element at index 2
l1.remove(21) # removes 21 from the list
print(l1)

#tuples
# Creating a tuple using ()
t = (1, 2, 4, 5)

# t1 = () # Empty tuple
# t1 = (1) # Wrong way to declare a Tuple with Single element
t1 = (1,) # Tuple with Single element
print(t1)

# Printing the elements of a tuple
# print(t[0])

# Cannot update the values of a tuple
# t[0] = 34 # throws an error

#tuple methods
# Creating a tuple using ()
t = (1, 2, 4, 5, 4, 1, 2,1 ,1)

print(t.count(1))
print(t.index(5))

# #write a program to store seven fruits in a list entered by the user.
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)
# write a program to accept marks of 6 students and display them in a sorted manner
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)
# check that a tuplew cannot be changed in python
a = (2,4,5,3,2)
a[0] = 45

# wirte a prgram to sum a lilst with 4 number
a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))

#dictionary syntax
myDict = {
    "Fast": "In a Quick Manner",
    "Pratik": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'pratik': 'Player'}
}

# print(myDict['Fast'])
# print(myDict['Pratik'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['Pratik'])

#distionary method
myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'pratik': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "pratik": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("pratik")) # Prints value associated with key "pratik"
print(myDict["pratik"]) # Prints value associated with key "pratik"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("pratik2")) # Returns None as pratik2 is not present in the dictionary
print(myDict["pratik2"]) # throws an error as pratik2 is not present in the dictionary

#set in python
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)
#empty set
# Important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))


#set methods in python
# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)

#
# write a program to crete a distionary of hidi words with value as their english translation provide user with an option to look it up!
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))


# write a program to input eight number from the user and display all the unique numbers
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)
# can we have a set with 18 int and 18 str as a values in it?
s = {18, "18", 18.1}
print(s)
# what willk be the lengh of following set S 

# s= set()
# s.add(20)
# s.add(20.0)
# s.add("20")
s = {20, 20.0, "20"}
print(s)
print(len(s)) 



# create a empty dictinary allow 4 friends to enter their favourite language as values and use keys as their namesa assume that the namem are unique
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['mohit'] = b
favLang['ritik'] = c
favLang['avinash'] = d

print(favLang)

# class and object
# Write a Python program to create a class and display the namespace of the said class.

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
for name in py_solution.__dict__:
    print(name)


    # Write a Python class to reverse a string word by word.
    class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))


# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# file read write in python
# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes

file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print( "Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()



# Numpy in python

import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

# **************

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# 0-D Arrays
import numpy as np

arr = np.array(42)

print(arr)

# 1-D Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# 2-D Arrays

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# 3-D Arrays
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#  Array Indexing

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])


# ****** # ******# ******# ******

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

# ******

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# Slicing arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]

# scipy
from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21

# matplotlib


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()