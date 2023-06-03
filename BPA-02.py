#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Write a Python program to convert Kilometers to Miles ?


# In[1]:


kiloMeters = float(input("Enter no of kilometers : "))
print("{} km is Equal to {} miles".format(kiloMeters,kiloMeters*0.621))


# In[2]:


#2.Write a Python program to convert Celsius to Farenheit ?
def celToFarh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
celToFarh()


# In[3]:


#3.Write a Python program to display calender ?
import calendar

year = int(input("Enter calender year: "))
print(calendar.calendar(year))


# In[5]:


#4.Write a Python program to solve quadartic equation ?
import cmath
import math

def quadarticEquationRoots(a,b,c):
    
    discriminant = b*b-4*a*c
    
    if discriminant == 0:
        r1 = -b/2*a
        r2 = -b/2*a
        print("Roots are Real",r1,r2)
    elif discriminant > 0:
        r1 = (-b-math.sqrt(discriminant))/(2 * a)
        r2 = (-b+math.sqrt(discriminant))/(2 * a)
        print("Roots are Real and different",r1,r2)
    else:
        r1 = (-b-cmath.sqrt(discriminant))/(2 * a)
        r2 = (-b+cmath.sqrt(discriminant))/(2 * a)
        print("Roots are Imaginary",r1,r2)


a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

quadarticEquationRoots(a,b,c)


# In[6]:


#5.Write a Python program to swap two variables without temp variable ?
a=10
b=8
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)


# In[ ]:




