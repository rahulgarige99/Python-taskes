class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b
    
my_cl = Calculator()
while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    ch = int(input("Select operation: "))
    if ch in (1, 2, 3, 4, 5):
        if(ch == 5):
            break     
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cl.divide(a, b))
    
    else:
        print("Invalid Input")




class Shiva():
    a=10 
    def show(self):
        print("this is class")
# obj name=class name()
kiran=Shiva()
print(kiran.a)
kiran.show()




class Mobiles():
    def __init__(self,Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price):
        self.a=Mobile_name
        self.c=Mobile_Ram
        self.d=Mobile_battery
        self.e=Mobile_Price

    def Mobile_Data(self):
        print("Mobile Name:",self.a)
        print("Mobile Ram:",self.c)
        print("Mobile Battery:",self.d)
        print("Mobile Price:",self.e)

while True:
    name=input("Enter the Mobile Name:")
    ram=input("Enter the Mobile Ram:")
    bat=input("Enter the Mobile Battery:")
    Price=float(input("Enter the Mobile Price:"))

    Mobile_obj=Mobiles(name,ram,bat,Price)
    Mobile_obj.Mobile_Data()























