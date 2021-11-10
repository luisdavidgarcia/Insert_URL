#!/usr/bin/env python3

# Obtain User Inputs
from os import wait


URL = input("Enter Your URL Here: ")
HyperText = input("Enter the Name You Want for Your Link: ")

# Open the File
TestFile = open("TestFile.html","r+")

for line in TestFile:
    if line == "Line1\n":
        # Write the link to the HTML
        TestFile.write(line + "\n<a style = \"color: blue; display: flex; flex-direction:column;\" href= \"" + URL + "\">" + HyperText + "</a>\n")

TestFile.close()



