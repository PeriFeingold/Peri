# file: homework1.py
#--- Variables and Data Types ---
a=10
print(a)
print(type(a)) #a in an integer, a whole number with no decimals
b=1.5
print(b)
print(type(b)) #b is a float, a number with a decimal place
c=3j
print(c)
print(type(c)) #c is a complex number, specifically the imaginary part
d="hello"
print(d) 
print(type(d)) #d is a string 
e=[1,2,3] 
print(e)
print(type(e)) #e is a list of integers
f={"peri", "mango"}
print(f)
print(type(f)) #f is a dictionary
g=(1,2) 
print(g)
print(type(g)) #g is a tuple
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list
i=True
print(i) 
print(type(i)) #i is a boolean
j=None
print(j)
print(type(j)) #j is a NoneType
k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, mixed types
l=str(14)
print(l)
print(type(l)) #l is a string
m=1e4
print(m)
print(type(m)) #m is a float
print(10>9) #true
print(10==9) #false
print(10<=9) #false
print(bool("abc")) #true
print(bool(123)) #true
print(bool(["apple","cherry","banana"])) #true
print(bool(True)) #true
print(bool(False)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool(" ")) #true
print(bool(())) #false
print(bool([])) #false
print(bool({})) #false
print(bool(True and False)) #false
print(bool(True and True)) #true
print(bool(False and False)) #false
print(bool(True or False)) #true
print(bool(True or True)) #true
print(bool(False or False)) #false
print(bool(not(False))) #true
print(bool(not(True))) #false
print(bool([{}])) #true
print(bool('')) #false

print(10+5) #15
print(10-5) #5
print(2*4) #8
print(6/3) #2.0
print(5%2) #1
print(3 ** 2) #9
print(15//2) #7
print(5==2) #false
print(10 != 10) #fale
print(2<5) #true
print(12>5) #true
print(5<=6) #true
print(1>=10) #false
x=5
x+=5
print(x) #10
x-=4
print(x) #6
x*=3
print(x) #18

my_string="hello"
print(my_string) #prints: hello
print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) #prints: el
print(my_string[0:5:2]) #prints: hlo
print(len(my_string)) #prints: 5
print(my_string+"goodbye") #prints: hellogoodbye
print(my_string*7) #hellohellohellohellohellohellohello
name="Oski" 
print("Hello, my name is", "Oski")
name = "Oski"
print(f"Hello, my name is {name}")

#cd: 
#changes directories: use it to move from one folder to another
#example: cd desktop
#ls
#list: list everything in the current directory
#example: ls
#ls -a
#list all files
#example: ls-a
#mkdir
#make a new directory
#example: mkdir hw_1
#cat
#cat shows the contents of a file
#example: cat_file(filename)
#pwd
#print current working directory
#example: pwd
#cd ..
#moves up one folder
#example: cd ..
#cd .
#stay in the current directory
#example: cd.
#cd ~
#moves to home directory
#example: cd ~
#cp
#copies files/directories
#example: cp file.txt
#mv
#moves/renames files and directories
#example: mv old.txt new.txt
#rm
#deltes files
#example: rm old_file.txt
#clear
#clears the terminal screen
#example: clear
#grep
#searches for text patters
#example: grep "apple" random.txt



# 1 Create a Folder
# Windows Users: Please make sure you are using Git Bash and NOT PowerShell.
# In class, you created a folder structure that looks like:
# python_decal_fa25/yourname/
# In the yourname/ directory, please make a new folder called homework1/. Type the following on
# the command line:
# mkdir homework1
# This is the folder where you will store the Python script you will work on throughout this assign-
# ment and the screenshots you take along the way. Move into the new homework1/ directory and
# the call pwd to show your entire file path.
# Take a screenshot of you making this directory on the command line. Name it hw1 folder.
# Store it in your homework1/ directory.




# 2 Make a New File in VS Code
# 1. Open VS Code.
# 2. Navigate to your homework1/ folder.
# 3. Create a new file called homework1.py.



# 3 Write a Python Script
# At the top of your file, add the following line:
# File: homework1. py
# It’s good coding practice to add a line at the top of your file stating its name. It will help keep you
# more organized.
# Section Headers
# At the top of each of the follow sections, please add a header like the following:
# # --- Variables and Data Types ---
# 3.1 Variables and Data Types
# In class we covered three data types: strings, integers and floats. Now you will work through several
# more. For each variable given below:
# 1. Print the variable.
# 2. Print the data type of the variable.
# 3. Leave a comment describing what kind of data it is.
# Hint: Use the internet.
# Example:
# a = 10
# print(a)
# print(type(a)) # a is an integer, a whole number with no decimals
# Variables:
# • a = 10
# • b = 1.5
# • c = 3j
# • d = "hello"
# • e = [1, 2, 3]
# • f = {"name": "Ellen", "favorite fruit": "strawberry"}
# • g = (1, 2)
# • h = ["apple", "banana", "strawberry"]
# 2
# • i = True
# • j = None
# • k = [True, "blue", 12]
# • l = str(14)
# • m = 1e4
# Questions:
# Answer the following questions as comments below your variables.
# 1. How many different data types did you find? 10
# 2. List all the data types you found.
# Integer, float, complex number, string, dictionary, tuple, list, boolean, NoneType, 
# 3. What variables have the same data types?
# d & l, b & m, k & h & e
# 4. What was the data type of l? Why is it not an integer? What does str() do?
# l is a string. It is not an integer because it has str() before the whole number which converts a value to a string
# 5. Look up one more data type not given above. Repeat the same procedure.
# Sets. turns multiple items into one variable
# 3.2 Booleans
# A boolean is a data type in Python which returns True or False depending on your code. Run
# each line given below. Next to the line, write a comment if it was True or False. Describe the result.
# Example:
# print(10 > 9) # True, 10 is greater than 9
# Expressions:
# • 10 > 9
# • 10 == 9
# • 10 <= 9
# • bool("abc")
# • bool(123)
# • bool([‘‘apple", ‘‘cherry", ‘‘banana"])
# • bool(True)
# • bool(False)
# • bool(0)
# • bool("")
# • bool(" ")
# • bool(())
# • bool([])
# • bool({})
# 3
# • bool(True and False)
# • bool(True and True)
# • bool(False and False)
# • bool(True or False)
# • bool(True or True)
# • bool(False or False)
# • bool(not(False))
# • bool(not(True))
# Questions:
# • What pattern do you notice about expressions returning True or False?
# When true was put first, the output was true and vice visa. 
# • Which expression surprised you about its result?
# All the brackets coming out as false surprised me.
# • Create an expression, not given above, that will return True. Why is it True?
# bool([{}]) this returns true because its not an empty container. If it were to be just bool([]) it would return false
# • Create an expression, not given above, that will return False. Why is it False?
# bool(‘’) this returns false because there is nothing between the ‘’. 
# 3.3 Operators
# An operator is a special symbol or keyword that performs operations. We will explore the following
# types of operators:
# • Arithmetic
# • Comparison
# • Assignment
# • Logical
# Run each line below, leave a comment next to it with the result and a description.
# Example:
# print(10 + 5) # 15, + performs addition
# 3.3.1 Arithmetic Operators
# • 10 + 5
# • 10 - 5
# • 2 * 4
# • 6 / 3
# • 5 % 2
# • 3 ** 2
# • 15 // 2
# 4
# 3.3.2 Comparison Operators
# • 5 == 2
# • 10 != 10
# • 2 < 5
# • 12 > 5
# • 5 <= 6
# • 1 >= 10
# 3.3.3 Assignments Operators
# Create a variable: x = 5. Perform the following operations on it.
# • x += 5
# • x -= 4
# • x *= 3
# 3.3.4 Logical Operators
# Answer the following questions as comments:
# 1. What does the operator and do? Write an expression that results in True. Write an expression
# that results in False.
# # operator and returns true when both operands are also true and false when operands are either. True: 2<5, False: 5>2
# 2. What does the operator or do? Write an expression that results in True. Write an expression
# that results in False.
# # operator or returns true if either operands are true and false when both operands are false. True: 3<5, False: 5>10
# 3. What does the operator not do? Write an expression that results in True. Write an expression
# that results in False.
# # operator not reverses the boolean expression. True: not(7>10), False: not (5<10)
# More Questions:
# 1. What is the difference between / and //?
# / returns a floating-point number and keeps the decimal point; // returns the biggest integer less than or equal to the quotient. 
# 2. What is the difference between % and //?
# % returns the remainder, // returns the quotient 
# 3. What operator would you use to calculate the remainder when dividing two numbers? Give
# an example.
# %, 10%3	
# 4. How do assignment operators work?
# They assign values to variables.
# 5
# 3.4 Strings
# Start with the string my string = "hello". Perform the following mutations and describe the
# results with a comment.
# Example:
# my_string = "hello"
# print(my_string) # Prints: hello
# Mutations:
# 1. Print my string.
# 2. Print my string[0].
# 3. Print my string[1].
# 4. Print my string[2].
# 5. Print my string[3].
# 6. Print my string[4].
# 7. Print my string[-1].
# 8. Print my string[1:3].
# 9. Print my string[0:5:2].
# 10. Print the length of the string: len(my string).
# 11. Print the result of adding my string with ”goodbye”.
# 12. Print the result of multiplying 7 times my string.
# 3.4.1 Questions:
# 1. Define the term slicing. For which of the manipulations did you slice your string?
# Slicing is a term used to describe extracting a piece from a sequence of date. We sliced for 2-9.
# 2. Call the following, describe the result: the result is: Hello, my name is Oski
# name = "Oski"
# print("Hello, my name is", name)
# 3. Call the following, describe the result: the result is Hello, my name is Oski
# name = "Oski" 
# print(f"Hello, my name is {name}")
# 4. What is the difference between the two last print statements?
# The difference between them is how you input them. The second way is used if you don’t want to write out the name everytime. 
# Hint: Look up f-strings.
# 6
# 3.5 Terminal Commands
# For each command listed below, do the following:
# 1. Define the command as a comment.
# 2. Explain how to use it.
# 3. Give an example of how to use it.
# 4. Try out the command on your terminal.
# Hint: If you don’t know one, feel free to look it up!
# Example:
# # cd
# # Changes directories. Use it to move from one folder to another
# # Example: cd Desktop
# Commands:
# 1. cd
# 2. ls
# 3. ls -a
# 4. mkdir
# 5. cat
# 6. pwd
# 7. cd ..
# 8. cd .
# 9. cd ∼
# 10. cp
# 11. mv
# 12. rm (be careful with this one)
# 13. clear
# 14. grep
# Questions:
# 1. Look up 3 other commands not present. Define and explain how to use them on the command line.
# len(): says the length on an object
# input(): enter a value to convert it into a string
# center(): align the string in the center.
# 2. What is the difference between ls and ls -a?
# ls lists only visible files whereas ls -a lists all files including hidden ones
# 3. What is a hidden file?
# Files that start with a dot
# 4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
# use them on the command line.
# -l: shows details of files; ls -l
# -d: lists directories
# -S: sorts files and directories by size
# 7
# 4 Running Your Script
# Please complete all the parts above before continuing.
# 4.1 In Your VS Code Terminal:
# 1. Open VS Code.
# 2. Run your completed script with the arrow button.
# 3. Take a screenshot of your code and the output on the VS Code terminal.
# 4. Name the screenshot: hw1 vscode
# 5. Save the screenshot in your homework1/ folder.
# 4.2 On Your Terminal Application:
# 1. Open the terminal (Mac) or Git Bash (Windows).
# 2. Navigate to the directory that holds your homework1.py script.
# Hint: It should be located in python decal fa25/yourname/homework1/.
# 3. Call pwd and ls, to show your current working directory and to list all the files and folders
# inside.
# 4. Take a screenshot of your pwd and ls commands on the terminal.
# 5. Name the screenshot: hw1 pwd and ls
# 6. Save the screenshot in your homework1/ folder.
# 7. Run your completed homework1.py script by calling:
# python3 homework1.py
# 8. Take a screenshot of your entire script output.
# 9. Name the screenshot: hw1 commandline
# 10. Save the screenshot in your homework1/ folder.
# 5 Submitting Your Homework
# Before submitting this assignment to Gradescope, make sure your homework1/ folder looks like
# this. You should have one homework1.py file and four screenshots:
# homework1/
# |--- homework1.py
# |--- hw1_folder.png
# |--- hw1_vscode.png
# |--- hw1_pwd_and_ls.png
# |--- hw1_commandline.png
# Please make sure your screenshots are named as shown. This will make it easier for the graders.
# Upload your entire homework1/ folder to Gradescope. Great job!
