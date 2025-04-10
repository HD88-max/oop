class Employee:
    def __init__(self,name):
        self.name= name
        print("Employee constructer")
    def __del__(self):
        print("Employee destructed")
    
def createobject():
    obj = Employee("name")
    print("Created")
obj1 = createobject()