# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString:
    def __init__(self):
        self.str1 = ""
    def getinput(self):
        self.str1 = input("Enter a string: ")
    def output(self):
        print("Result is: ",self.str1.upper())
ob = IOString()
ob.getinput()
ob.output()

    