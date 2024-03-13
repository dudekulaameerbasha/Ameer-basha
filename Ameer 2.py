'''
a, b=c=7,8
print(a)
print(b)
print(c)

a=b,c, = 4,2
print(a,b,c)

#--->swapping of variables
a=7
b=5
print(a,b)

# Eg:1
# temp=a #temp=7
#a=b   #a=5
#b=temp#b=7

##a=5,b=7
#print(a,b)

#Eg:2
#a=a+b #a=12
#b=a-b #b=12-7=5
#a=a-b #a=12-5=7

#print(a,b)

# a, b=b, a # only in python
# print(a,b)

a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))

# id()-->used to find the memory address of the variable
# a = 7
# b = 8
# print(id(a))
# print(id(b))

#--->keywords
# keywords are reserved words which provides special meaning to
# compiler or interpretor

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))


# To check if the string is keyword or not
print(keyword.iskeyword("isd")) # false

# if = 8
# print(if) # error coz if is a keyword

# !---> literals
# literal is the constant value assigned to a variable
# A variable is considers to be constant when it is defines
# in caps

#a= 78 # a is variable
# A=78 # A is constant

# hash()---> it creates a hash value for constant datatypes and
# provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))

f1 = [7,8,9]
print(hash(f1)) # error --> list is non-constant or mutable datatype


'''
'''

#!---> operators
#operators are symbols which are used to perform various operators  2 or more operators 
#arthimetic
#Assignment
#Logical
#Relational or comparison
#identify
#membership
'''
'''
#--->Arthimetic--->+,-,/,%,//,**
eg:1
a=8
b=6
c=5
print(a+b+c)

'''
'''

'''
'''
a=4
b=2
print(a/b)
print(a%b)
'''
'''
 #! **--> used for power of a number
 # print (2**40 #--> 16


#! Assignment --> +=,>,<, !=,<=,>=
   # a = 8
   # b = 7
   # print(a>b) # True
   
   # a = 9
   # b = 5
   # print(a==b)

    # ! Bitwise operator -->&,|,^, ~, <<,>>
    a = 7
    b = 4
    print(a&b)


  # 2^4 2^3 2^2 2^0
  # 8    4   2   1

  # 0     1   1
'''
n = int(input("enter the number:"))
if n %2==0:
    print(n,"is even")
else:
    print(n,"is odd")
    
...

n=int(str(name))
input(int(age))
input(str

  
   
   
   


















