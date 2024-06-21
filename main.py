
# Installed Pillow to display image.
from PIL import Imagejos
# Intending to use Ex: os.system("pause")
import os
# This is a comment. In C++ comments are indicated as // or /**/

# In C++, cout << "" << is used in place of print().
# No semicolon ; after print() this is different than C++.
# input() is used to get user input.
# In C++ cin >> age; is used to get user input.
# Python uses colon : much more than semicolon ;.
print("Hello, World!", "\U0001F60A")
# A function to introduce the program
# Using unicode: 	U+1F600. To use emoji unicode replace + with 000, add \.
# Ex: U+1F606 to print("\U0001F606")
def intro1():
    print("IN THIS PROGRAM, YOU WILL LEARN ABOUT THE BOILING POINT OF WATER!", "\U0001F643")
intro1() # Function call
print("First Enter Your Name To Learn A Fun Fact About Python")
yourName = input("Enter Your Name: ")
print("Thank you " + yourName)
print("Did you know? Python gets its name "
      "from the 1970s British TV comedy series, Monty Python's Flying Circus?")
readerInput = input("Enter Yes/No")
if readerInput == "Yes":
    print("Perfect!")
else:
    print("Nothing to worry about.")
    print("Here is another fun fact -")
    print("In Python, To open() a file to read or text are default values. "
          "We don't have to specify these two file "
          "modes.")
    os.system("pause")
print("BOILING POINT OF WATER")
print("The boiling point of water,varies according to the surrounding atmospheric pressure. A liquid boils,"
      " when its internal vapor pressure equals the atmospheric pressure.")
# os.system("pause")
print(">>>>>>>>>>")
print("But pressure drops as you gain elevation.")
print("'-'")
print("Please review image - ")
# Load the image
img = Image.open('boiling-point.png')
# show the image
img.show()

print("In higher places, water boils at lower temperatures.")
print("The elevation of Mt.Everest is: 30K/ft")
print("The elevation of Denver is: 5K/ft")
print("Boiling point of water in Mt.Everest is: 162 Degrees Fahrenheit")
print("Boiling point of water in Denver is: 203 Degrees Fahrenheit")
# To receive int from user input using int(input())
# To make sure user gets another chance to enter answer
# used for loop in range().
# for in range() didn't work.
# Instead, used while loop. Loop ran forever.
# Used break stopped forever loop.
# Used if statement twice, worked.
# My intention was to use if elif and loop through, instead of using two if statements. Maybe next time.
# Using exceptions in-case user input is string.
# To throw (or raise) an exception, using the raise keyword.
# Ex: if..... raise Exception()
# New features to add - Learn to loop back to get the right answer.
# Right now program exits after Exception.

bpWaterDenver = int(input("Quiz: Please Enter Boiling Point of Water in Denver: "))
while bpWaterDenver != 203:
    print("Please Try Again!")
    break # when not using break while loop runs forever. It is scary!!
bpWaterDenver = int(input("Quiz: Please Enter Boiling Point of Water in Denver: "))
if bpWaterDenver > 203:
    raise Exception("It can't be more than 200 Degrees Fahrenheit.")
elif bpWaterDenver == 203:
    print("Thank you " + yourName)
else:
    print("Thank you for learning!")







