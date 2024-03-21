

#) Tasks
#Write the code for the belwo tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'
#2.) Find then 67, is strong number or not
#3.) 11 [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]


'''
# Task 1
def find_min_max_price(products):
    min_price = min(products.values())
    max_price = max(products.values())
    return min_price, max_price

def find_products_starting_with_s(products):
    s_products = [product for product in products.keys() if product.lower().startswith('s')]
    return s_products

# Task 2
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def is_strong_number(n):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(n))
    return sum_of_factorials == n

# Task 3
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Example usage
d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
print("Min and Max priced product:", find_min_max_price(d1))
print("Products starting with 's' or 'S':", find_products_starting_with_s(d1))

n = 67
print(n, "is a strong number:", is_strong_number(n))

l1 = [1, 2, 3, 4, 5, 6]
n_values = [2, 3]
for n in n_values:
    print("Rotated list for n =", n, ":", rotate_list(l1, n))



# ! Method Riding
# * Polymorphism in classes

class bank:
    def ratio(self):
        print("All banks has repo rate")


class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()
        
s = SBI()
s.ratio()


# ? Eg:2
class USA:
    def language(self):
        print("English")
    def capital(self):
        print("Washing DC")
class India(USA):
    def language(self):
        print("None")
    def capital(self):
        print(New dalhi")

I = India()
I = language()
I = capital()


# Eg:3
# polymorphism using objects

# c1,c2---> c1 = print(c1),print(c2)
# f1,f2

# Eg:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj2 = c1()

#* changing the functionality of builtin functions
class shooping:
    def__init__(self, l1):
        self.items = len(l1)

    def__len__(self):
        length = len(self.items)
        return length
s = shoping([1,2,3,4,5])
print(len(s))
# print(len(s))


# ! ---> Method overloading
# ! Eg:1
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
# s.add(4,3) # ! ---> error
s.add(455,575,441)


# * changing the functionally of builtin functions
class shopping:
   def __init__(self,l1):
       self.items = l1
       
   def __len__(self):
       length = len(self.items)
       return length
s = shopping([1,2,3,4,5])

print(len(s))

# ! --------> Abstraction
# The procss of hiding the implimentation details is abstraction

# ? Eg:1
class shapes(ABC):
    def sides(self):
        print('All shapes have sides except circle')

class triangle:
    def triangle_sides(self):
        print("3 sides")

class square:
    def square(self):
        print("4 sides")


 from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()

# To write the capital letters

def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'   

  


# ! Rules to define abstract class 1
1.) Abstract class cannot be instantiated
2.) From abc import ABC, abstractmethod
3.) subclass the normal class with ABC
4.) Convert the normal method inside the abstract class to abstract method
5.) All the child classes have to be subclassed with abstract class
6.) The abstract method should be present in the child classes


# ! Eg:2
# super()
from abc import ABC, Abstractmethod 
class c1(ABC):
    @Abstractmethod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
    
class2 = c2()
class2.m2()
# ! --------> Abstraction
# The procss of hiding the implimentation details is abstraction

# ? Eg:1
class shapes:
    def sides(self):
        print('All shapes have sides except circle')

class triangle:
    def triangle_sides(self):
        print("3 sides")

class square:
    def square(self):
        print("4 sides")
        pass 

s = shapes()
s.sides()

tr = triangle()
tr.triangle_sides()

# Rules to define abstract class1
#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the # child classes


#! Eg:2
#super() ---> used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")
    def m1(self):
        pass
class2=c2()
class2.m2()
#Eg:3
from abc import ABC, abstractmethod
class password (ABC):
   @abstractmethod
   def pwd(self):
       pswd "Ameer2003$"
class login (password):
    def validate(self, name, passwrd):
        print(name, passwrd)
Login login()
Login.validate()



# * ----> Eg:-2
# ? accessing privet date out side the class
'''
'''
class c1:
      _phone = '8532247773'

      def display(self):
          print(self._phone)

# * -----> Eg:3
# ? declare privet method
'''
'''
class class1:
    def m1(self):
       print ("i am private method")

    def __init__(self):
            self.m1()
c = class1()
# ? nested class
'''
class class1:
    class class2:
        name = "Ameer"

        def display(self):
            print(self.name)
    obj1 = class2()
obj = class1()
obj.obj1.display()





















       


















        



















              










              


















    
