
 # 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

'''
s1 = "hellow world"
fst = s1 [0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

'''
'''
n = 128
while n!=0:
    rem = n%10
    print(rem)
    n = n/10
'''
'''
n = 128678
temp = n
str1 = ""
while n!=0:
    rem = n%10
    check= temp %rem
    n = n//10

if f1==0
    print("Yes")
    else:
        print("No")
'''
'''
l1 = [8,9,0,7]
l2 = [7,6,5,4]
l3=[]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)

# ! -----> set
# characteristics of set
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable

# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 3
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)

# eg
# ? to add element inside list
'''
'''

s1 = {8, 78, 67, 'u'}
s1.add(43)
print(s1)
'''
'''

# update()
s1 = {8,6,7,3,546,'u'}
s1.update([45,'i'])
print(s1)

# clear()
# ? to delete element inside set
s1 = {8, 78, 67, 'u'}


# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove()
s1.remove(78)
print(s1)

# discard()
s1.discard(8967)
print(s1)


# clear()
l1 = {}
print(type(l1)) ---- datatype is dict

s1 = set() # to creat empty set
print(type(s1))
'''
'''
l1 = {}
print(type(l1)) 
'''

'''
s1 = set() # --> to create empty set
print(type(s1))
'''

'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''
'''


s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

# n1 = {1,2,3} --->

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)

# !----> dictionary
# Eg:1
d1 = {1:100,'a':200, 4.5:"hellow"}
print(d1)
print(len(d1))

mech_name = ["name1","name2","name3"]
mech_age = [23,22,24]
mech_mark = [89,78,60]
mech_email = ("name2@gmail.com", "name3@gmail.com")
'''
'''

# ? char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key,value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed,
# 5.) Duplicate values are allowed
# 6.) It is unidexed
# 7.) It is ordered
# 8.) Key does nat allow mutable datatypes
# 9.) Values allow mutable datatypes


d1={1:100,2:200,3:300,-4:400}
#to access elements in dictionary
print(d1)
#or
#to access the values
print(d1[-4])#---->o/p is 100

#some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

#to find min,max based on values
print(min(d1.values())


d1 = {1:100, 2:200, 3:300, 4:400}
# to access element in dictionary

print(d1)
#or
# To access the values
print(d1[1]) #o/p --->100

# ? some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

# ? To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

# ? dictionary based functions
# to add elements(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

# ? To replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)

# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
#popitem ---> to delete last key value pair in dict
d1.popitem()
print(d1)
print(d1.popitem())

#pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

#clear(), del
#update()
#join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

#get() ---> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[3])
#print(d1[90])
print(d1.get(90))


#to print all the keys
print(d1.keys())
print(type(d1.keys()))
d1 = {1:100, 2:200, 3:300, 4:400}
# to access element in dictionary

print(d1)
#or
# To access the values
print(d1[1]) #o/p --->100

# ? some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

# ? To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

# ? dictionary based functions
# to add elements(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

# ? To replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)

# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
#popitem ---> to delete last key value pair in dict
d1.popitem()
print(d1)
print(d1.popitem())

#pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

#clear(), del
#update()
#join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

#get() ---> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[3])
#print(d1[90])
print(d1.get(90))


#to print all the keys
print(d1.keys())
print(type(d1.keys()))

# ! problem:1
#Iterating dictionary
for val in d1: # to iterate keys alone
    print(val)

# for val in d1.values(): # to iterate values alone
#   print(val)

# to get both key and values
for  key, val in d1.items():
    print(key,val)
'''
# ! Problem:1
#n = input()

#1.) Swap elements in string list
# The original list is : ['Gfg', 'is', 'bGst', 'for', 'eGGks']
#List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']




n = int (input(" Enter num of times:"))
integer=[]
float_value =[]
string=[]

for val in range(n):
    value = eval(input("Enter the values:"))
    if type(value)==int:
                inter.appened(value)
            elif type(value)== float:
                float_ value.appened(value)
            elif type(value)== str:   
                sring.appened(value)
                      else:
        print("p1s provide data in int, float, string")      
print(integer)        
print(float_value)        
print(string)

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

# ! problem:2
# return a set elements present in set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)

print(set3)


# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']




#! ---> problem 3
l1=[1,2,3,4] # key
l2=["a","b","c","d"]  # value
l3=(l1[0],l2[0]or l1[1],l2[1] or l1[2],l2[2]or l1[3],l2[3])
print(l3)
LE-318 DUDEKULA USMAN
4:08 PM
#!------> problem 3
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)

# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']





















































