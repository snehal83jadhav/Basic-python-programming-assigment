#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python program to check if a Number is Positive, Negative or Zero ?
n=int(input("Enter a number = "))
if(n>=0):
    print("number is positive")
else:
    print("Number is negative")


# In[2]:


#2.Write a Python program to check if a Number is Odd or Even ?
n=int(input("Enter a number = "))
if(n%2==0):
    print("number is even")
else:
    print("Number is odd")


# In[4]:


#3.Write a Python program to check Leap Year ?
year=int(input("Enter a year = "))
if (year%4 == 0 and year%100 != 0 or year%400 == 0):
    print(f'{year} is a Leap year')
else:
    print(f'{year} is not a Leap year')


# In[5]:


#4.Write a Python program to check Prime Number ?
def isPrime(num):
    flag = False
    for i in range(2,num):
        if num%i ==0:
            flag= True
            break
    if(not flag):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
        
number = int(input("Enter a number: "))
isPrime(number)


# In[6]:


#5.Write a Python program to print all Prime Numbers in an interval of 1-10000 ?
primeNumbersList = []

def generatePrimeNumbers():
    for x in range(1,10000):
        flag=False
        for y in range(2,x):
            if (x%y ==0):
                flag = True
                break
        if (not flag):
            primeNumbersList.append(x)
        
generatePrimeNumbers()
print(primeNumbersList)


# In[ ]:




