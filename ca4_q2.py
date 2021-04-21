'''
nci programme: BSHDS 
program: searches among a given directory and its subdirectories recursively
author: Renato Gusani
studentID: x19411076
date: 08/05/2020

'''
import glob # glob  finds all pathnames matching a specified pattern

myPersonalDirectory = glob.glob("C:\\Users\\renat\\Documents\\BSc. (Honours) in Data Science\\Year 1\\Semester 2\\Programming I\\Python Programs")
for directory in myPersonalDirectory:
 print (directory)

