'''
# ! Eg:3
def profile(name,age,place):
    txt ="My name is{}.Iam{}years old. Iam from{}."
    print(txt.format(name,age,place))
profile("Ameer basha", "21", "tadipatri")

You, Now
# ! Eg:4
# ? Function with return statement

def f1():
    z = 8
    f1()
    print(Z) #error----->cannot use outside the function

 def f1(a,b):
     c = a*b
     return c
   print (f1(6,8))
   obj = f1(6,8)
   obj1 = f1(4,6)



def gracemark(object):
       print(object+4)
       gracemark(obj)
       gracemark(obj+1)
'''       
       
def palindrome(n):
       print(n)


a = int(input("Enter the value:"))
palindrome(a)

# ? Problem:1
def palindrome(n)
string = srt(n)
    rev = str(n)
    if string==rev:
         print(n, "palindrome")
    else:
         print("not palindrome")
         a  =  int(input("Enter the vslue:"))
         palindrome(a)

# ? based on the declaration of parameter and args
# ? function are divide in to 5 catagories

#posible args
#key words args
# default args
#varible lenth args
#key words avriable lenth args

# * Positional args
#? The position of parameter ahve to be same as position as arguments
#! Eg:1
def profile (name,phone,mark):
    txt = "My name is {}.My phone number is{}.I got {} marks."
    print(txt.format(name,phone,mark))

    profile(9573558615,"ameer",95)# unexpected output

# * Keyword args
#!Eg:1
To overcome the disadvantage of position args ,we keyboard args
It is the process of intialising the paremeter with the args while calling the
Functon
def profile (name,phone,mark):
    txt = "My name is{}.my phone number is{}.I got{} marks."
    print(txt.format(name ,phone,mark))

    profile (name"ameer",123456789,marks=95) # error
    profile(123456789,name="ameer",mark95)
  profile (name"ameer",123456789,marks=95) # error--> positional args follow keyboard   
   profile(123456789,name="ameer",mark95) #! error--> name has multiple values
   profile("ameer",mark=95,phone 123456789)


# ! Eg:2
def profile(name,phone,place="kadapa"):
    txt = "My name is {}.my phone nu,mber is {}.I am from{}."
    print(txt.format(name,phone,place))

Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("ameer",9876543210)


# * Variable length params
#! Eg:1

def profile(*name):
    print("My name is",name)
    profile("mk", "name2","name3")

    def profile(*name):
        for val in name:
            print("My name is val)
                  profile("ameer", "name2" "name3")
    
# ! Eg:2
   def profile(*name,age):
     for val in name:
       print("my name is","my age is",age)
       profile("ameer,""name2" "name3",)
       
                 
# * Keyword variable length args
# kwargs-->which is used to provide the args in the form of key value pair.
# ! Eg:1
# def price(price_list):
# print(price_list)

# price(shirt=1000,iphone=80000)

# n = 5
# {1:1, 2:4, 3:9,4:16,5:25}
n = int(input_'Enter the number:"))
def dict(n):
   d1 = {} for val in range(1.n+1):
          d1[val] = val**2
     print (d1)
# dict(5)


# d1 = {"a":100, "b":200,"c":300}
# d1 = dict(a=100,b=200,c=300)
# print (d1)

#----> object oriented programming
# The paradigams of objects oriented programming are

# class
# object
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object

l1 = [1,2,3,4,5,6]

# ? Eg:1
class c1:
    name1 = "ameer"
    print(name1)

# ? Eg:2
class person:
    name = "ameer"

c = person() # c os object
The process of creation of an object is called an Instantiation 
print(c.name)

# ? Eg:3
create of a method
When the function is created with a class is called as method


class person:
       def display():
              print("Hellow welcome to classes")

p = person()
p.display()


# ? Eg:4
#Method with parameter
class person:
    def display(person,name,age):
        print(name,age)


p = person()
p.display("ameer",21)

#print("Hello welcome to classes")

#! Eg:5
class person1:
       fname = "ameer"# attribute or static variable
       I name = "T"

       def first_name(self):
              print(self.fname)

              
              def full _name(self)
                  print(self.fname+" "+self.1name)
  p = person()
  p.first_name()
  p.full_name()

# constructors ---> __init__()
# This is a special method which has the ability to execute itself without
# calling it manually through the process of instatiation

class profile:    
    def __init__(self):
        print("hey")

p = profile() # execution through this process
p.__init__()






















             































       

            
