#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1.Write a Python Program to find the factorial of a number ?
num = int(input("Enter a number: "))
factorial =1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
        factorial=factorial*i
   print("The factorial of",num,"is",factorial)


# In[22]:


#2.Write a Python Program to display the multiplication table ?


num = int(input('Enter a number: '))
for x in range(1,11):
        print(f'{num} X {x} = {num*x}')


# In[23]:


#3.Write a Python Program to print the fibonacci sequence ?
s_count = int(input('Enter the no of fibonacci sequences you want? '))
initial_list = [0,1]
if s_count < 0:
    print('Fibonacci Numbers are not available for Negative Numbers')
elif s_count <= 2 and s_count >= 0:
    print(initial_list)
else:
    for ins in range(s_count):
        if ins >= 2:
            initial_list.append(initial_list[ins-1]+initial_list[ins-2])
    print(f'The First {s_count} fibonacci series are: ',initial_list)


# In[24]:


#4.Write a Python Program to check Armstrong number ?
def checkArmstrongNumber():
    in_num = input('Enter a number: ')
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        print(f'{in_num} is a Armstrong Number')
    else:
        print(f'{in_num} is a Not Armstrong Number')

for x in range(2):
    checkArmstrongNumber()


# In[26]:


#6.Write a Python Program to sum of natural numbers ?
def sumOfNaturalNumbers(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural numbers is {sum}')
    
num = int(input('Enter a number: '))
sumOfNaturalNumbers(num)


# In[ ]:




