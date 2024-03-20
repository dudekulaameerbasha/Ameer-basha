
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print("8th Fibonacci number:", fibonacci(8))

s1 = "Hellow how are you"
s2 = "Hellow how is"


s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
    
for val in s2:
    if val not in s1:
        print(val)

# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)

# ! Constructors
# ! Eg:2

# * unparametarised constructor
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()


# ? Eg:3
# * Parametarised constructor
class profile:
    def__init__(self,id,name,age:
        print(id,name,age)

obj = profile(1,"ameer"21)

#? Eg:4
class c1:
    email = "ameer@gmail.com"

    def m1(self):
        name = "ameer"
        place="gooty"
        print(name,place)
        print(self,email)

object = c1()
object.m1()

# ? Eg:5
class c1:
    def m1(self):
        name = "ameer"
        age = 21
        return name,age
        def diplay(self):
            print(name,age)
            print(self.name,self.age)
            print (self.m1())
 object = c1()
 object.display()

# ? Eg:6
class class1:
    def__init__(self):
        email = "ameer@gmail.com"         # static variable
        self.name = "ameer"               # instance variable
        self.email = "ameer@gmail.com"
        # return name, email # error --->cannot use return with constructor
        
        def display(self): # instance method
            print(self.name,self.email)

 c1 = class()
 c1.display()


# ! -------> Inheritance
The process of utilising the methods and attributes of parent class
Throught the object of child class it is called as inheritance

# 5 types of Inheritance
Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hybrid Inheritance
heirarichal Inheritance

# * Single Inheritance
# ? It has only one parent class and only one child class
# ! Eg:1
class parent:
    def m1(self):
        print("Iam parent class")

class child(parent):
    def m2(self):
        print("Iam child class")
p = parent()
p.m2()
 obj = child()
 obj.m1()
 # !Eg:2
 class c1:
     def __init__(self):
         print("i am constructor from parent class")
 
 class child(c1):
      pass
    
obj = child()

# ! Eg:3
class parent:
    name = "ameer"
class child(parent):
    name = "name1"
    def display(self):
        print(self.name)

d = child()
d.display()

# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
                print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(voice):
    def cat_voice(self):
        print("meow")

class parrot(voice):
    def parrot_voice(self):
        print("speak")

# ? Eg:2
class honda_city:
    def honda_city_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)


class honda (civic):
    pass

honda = honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white,2000,5.5,8,"hatchback")



















        























 

















            
















Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -



































        
