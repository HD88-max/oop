# Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max=max_speed
        self.mileage=mileage

ob = Vehicle(120,200)
print("The maximum speed of the model is {0}".format(ob.max))
print("The mileage of the model is {0}".format(ob.mileage))