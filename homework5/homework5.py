# git is a command and github is a coding platform
# terminal is a program that gives you access to the command line and the command line is where you type. 
# a local repository is on your computer and a remote repository is on the internet
# version control manages changes made to files
# a staging area in Git is an intermediate area where commits can be made without completing the commit. 
# git add- adds work to staging area
# git commit- saves work locally
# git push- saves work remotely 
# git status- says the status of a repository (good for debugging)
# git pull- fetch from another repository or local branch
# pwd- print current working directory
# ls- list  and folders in current directory
# cd- change directories
# nano- open a text files editor
# touch- make a new file
# mv- move files
# rm- remove files
# cat- print all the contents of a file

#3.2
# 1. pwd
# 2. ls
# 3. cd .. then cd brianna_repo then git pull
# 4. git mv homework.py brianna_repo/homework.py homework/ then git commit -m
# 5. cd .. then cd judy_decal/ then cd homework/
# 6. nano homework.py
# 7. git add, git commit, git push
# 8. git pull (to get the file back to the staging area), git status (check for bugs), git push 
# 8. the error means she did not pull all the updates and therefore does not have everything locally.
# 9. cd ~/recents


# 4.1 Data types
x=4
print(4)
print(type(4))

#4.2 conditionals 
def even_or_odd(number):
    if number % 2==0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(2))

# 5 loops
numbers = [1,2,3,4,5]
sum = 0
for nums in numbers:
    sum += nums
print(sum)

#6 Homework4 Review
#6.1 lists
list=[1,2,3,4,5]
for nums in list:
    print(list *2)  #i dont know how to get the same numbers next to eachother

#6.2 debugging
num=2 
print (num ** 2)

def even_or_odd(number):
    if number % 2==0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(2))
