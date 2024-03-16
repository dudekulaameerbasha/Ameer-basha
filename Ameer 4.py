
'''
# ----> while loop
#-----> break using while loop

# eg:1
# 1.) iterate from 20 to 30 and break the loop in 27
'''
'''
i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
 '''
'''
Eg.2
i = 20
while i<31:
  print(i)
  i+=1
  
  if i ==27:
     break
'''
'''
Eg:3
i = 20
while i<31:
    if i ==27:
     break 
print(i)  
i+=1
'''
'''
# !----> continue
# !---->Eg:1
i = 20
while i<31:
    if i==27:
        continue
    print(1)
    i=i+1

i = 20
while i<31:
    if i==27:
       i=i+1
       continue
    print(i)
'''
'''
# while to iterate  from 12 to 22
# find the sum of all numbers
i = 12
while i<22:
    if i ==22:
        break
    print(i)
    i+=1

i = 12
sum=0
while i<23:
 
    print =(sum)
    sum=sum=i
    i=1
'''
'''
# ! Eg:6
# Find the average of value from 20 to 30

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)

'''
'''

# ! -----> Nested for loop
# Eg:1

for i in range (1,3):
    for j in range(1,4):
        print(i,j)
for row in range(1, 3+2):
    for col in range(1, 4+1):
        print(row, col)
'''
'''
 # Eg:-2
 
#****
#****
#****
#****
for row in range(4):
    for col in range(4):
        print(row, col)
'''
'''
sum = 0
for row in range(5):
     for col in range(5):
         sum = sum+1
         print(sum,end="")
     print()  
'''
# !o print stars in right angled triangle


for row in range (0,6):
    for column in range(0,row+1):
                  print("*",end="")
                  print()
'''                  

# * * * * * *
# * * * * *
# * * *
# * *
# *
'''

for row in range (6,0, -1):
    (0,row) 
print("*", end= "")
print()

# * * * * *
# *       * 
# *       *
# *       *    
# *       * 
# * * * * *

'''
'''
''''
for row in range(5):
     for col in range(5):
         if col== Or col==5 or row ==0 or row==5-1:
              print("*", end= "")
         Else:
             print("*",end'')
                   
     print()
     '''

for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    

for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()





'''
# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous


# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

'''
'''
# ?---> positive indexing
lst1 = [1,4,1,7,89,7,7.5,"p","i"]
print(lst1[0])
print(lst1[4])
print(lst1[20])


# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

'''
# ? -----> Negative indexing
lst1 = [1, 4,7,89,7.5,"P","i"]
 print(lst1[-1])
 print(lst1[-5])

 # ? ----> slicing
# lst1[start_index:end_index:step]
lst1 = [1,2,3,4,56,34,"p","i",]
print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])













































     
























                   














        
        

















                  
























        



        





































    
    














          





















  





