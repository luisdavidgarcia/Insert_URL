#!/usr/bin/env python3

# Obtain User Inputs
from os import wait

# Variables
filePath = input("Enter the File Path of the File you Wish to Edit: ")
URL = input("Enter Your URL Here: ")
HyperText = input("Enter the Name You Want for Your Link: ")
PlaceHolder = input("Enter the Placeholder Line Number for where all your new Links should Be Placed Below: ") 

# Open the File and Read Lines 
TestFile = open(filePath,"r")
lines = TestFile.readlines()
# User Enters the Line Number of placeHolder when counting from 1 to placeHolder, 
# but Computer counts from 0 to placeHolder, which is why there is a -1 
lines[int(PlaceHolder)-1] = "\n        <a style = \"color: blue; display: flex; flex-direction:column;\" href= \"" + URL + "\">" + HyperText + "</a>\n"
TestFile.close()

# Open File and Write Updated Lines 
TestFile = open(filePath,"w")
TestFile.writelines(lines)
TestFile.close()



