'''
nci programme: BSHDS 
program: quotes
author: Renato Gusani
studentID: x19411076
date: 08/05/2020

'''
import random # this package will select a random quote to output

# prompts user for 7 quotes
Quote1 = input('Enter Quote1:')
Quote2 = input('Enter Quote2:')
Quote3 = input('Enter Quote3:')
Quote4 = input('Enter Quote4:')
Quote5 = input('Enter Quote5:')
Quote6 = input('Enter Quote6:')
Quote7 = input('Enter Quote7:')

# Creates a file with the above input into it
with open('Renato_Quotes.txt','w+') as f:
    f.writelines(Quote1+'\n')
    f.writelines('\n')
    f.writelines(Quote2+'\n')
    f.writelines('\n')
    f.writelines(Quote3+'\n')
    f.writelines('\n')
    f.writelines(Quote4+'\n')
    f.writelines('\n')
    f.writelines(Quote5+'\n')
    f.writelines('\n')
    f.writelines(Quote6+'\n')
    f.writelines('\n')
    f.writelines(Quote7+'\n')

# closes the file after input
f.close()

# opens the file again and generates a random line for output
s=open("Renato_Quotes.txt","r")
m=s.readlines()
l=[]
for i in range(0,len(m)-1):
    mystring=m[i]
    myint=len(mystring)
    a=mystring[:myint-1]
    l.append(a)
l.append(m[i+1])
Quote=random.choice(l)
print(Quote)
s.close()