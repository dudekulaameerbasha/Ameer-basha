'''
# Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.
'''
'''
length =int(input())
breadth =int(input())
if length ==breadth:
    print("its not square")
else:
        print ("its not square")

'''
'''
 python program to check whether the
 given integer is a multiple of both 5 and 7
'''
'''
n = int(input("enter the number:"))
if n%5==0 and  n%7==0:
     print("yes")
else:
         print ("no")

'''
'''
!Eg:5
Write a program to accept the cost price of a bike and display the
road tax to be paid
according to the following criteria :

    cost price (in Rs)
    > 100000
    >50000 and <= 100000
    >= 50000

    '''
'''
price = int(input("enter the price:"))
amount = 0
if price>=10000:
  discount = price*(6/100)
  value = price-discount
  amount=value*(15/100)
  total=value=amount
else:
     tax = price*(5/100)
     total = price=tax
print("the onroad cost of bike is: ",total)
'''
'''
#!-----> if elif else
'''
'''
Eg:1
a = 7
b = 9
c = 8
'''
'''
if a>b and a>c:
    print("A is greater")
    elif c>a and c>b:
        print ("C is greater")

A school has following rules for grading system:
    a.Below 25 - F
    b.25 to 45 - E
    c.45 to 50 - D
    d.50 to 60 - C
    e.60 to 80 - B
    f.Above 80 - A
    Ask user to enter marks and print the corresponding grade.
 mark = int(input("Enter mark:"))
 if mark >=80 and mark<= 100:
    print ("A")
elif marks > = 60 and mark < 80:
    print ("B")
elif marks > = 50 and mark < 60:
    print ("C")
elif marks > = 45 and mark <50:
    print ("D")
elif marks > = 25 and mark < 45:       
    print ("E")
else :
     print ("Fail")

   Enter marks 22
   Fail
'''
'''
 rules
1.)statement inside the if condition have to be present at first
2.)elif cannot be used in short hand if else
3.)always it have to end with else   
'''
'''
a=9
b=60
if a>b:
    print("A")
else:
    print("B")
'''
'''
#! code to check the given char is  vowel and consonent
'''
'''
#char = input("enter the char:")
if char=="a" or char=="e" or char=='i' or char =='o' or char =='u':
    #  print(is a vowel")
    #else:
    #  print("its consonent")
   '''
'''
str1 ="aeiouAEIOU"
if char in str1:
        print("vowel")
else:
         print("consonent")
    # ! shorthand if else
    char = input("enter the char:")
    str1 ="aeiouAEIOU"
    print("vowels") if char in str1 else print("consonent")

    # !---> elif ladder using short hand if else
    # eg:1
    # ? find greater among 3 variables using short hand if else
    a = 8
    b = 5
    c = 9

    #print("a is greater")if a>b and a>c else print("b is greater")
    # if b>a and b>c else print("c is greater")

'''
    # !---------> looping
'''
     # looping can be implimented using
     # for loop
     # while loop

     # ? for loop is used for iteration ,if we know the number of times  the loop have to run
'''      '''
# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
for val  in range (1,10+1,):
    print ('7','X',val,'=',val*7)
    
    '''
'''
# ! ------> while loop
#while is used when we do not kbnoe the number of times the loop have to run
#to iterate the non iterable elements while loop is used

# to do syntax
# initialisation
# while condition
#     statement
#     incre or decre

#Eg:1

#to iterate number from 1 to 10

#i=0
#while i<11:
#    print(i)

# for loop practice
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 abd 37c(including both numbers)

# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432


  
    

        

   
 



