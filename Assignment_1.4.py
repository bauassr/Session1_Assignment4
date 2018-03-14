# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:19:34 2018

@author: singh.shivam
"""
# Assignment 1.4 Calculate Volume of a sphere
import math
def Vol(diameter):
      Volume= 0
      radius = diameter/2
      Volume=4/3*(math.pi*math.pow(radius,3))
      
      return Volume

print("Calculate Volume of sphere")  
print("enter the diameter:")
v=Vol(int(input()))
print("Volume of sphare: ",v)


