# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:31:21 2020

@author: Bony Mondal
"""
l=[1,3,5,7]
lower=0
num=int(input('enter number '))
upper=len(l)-1
mid=lower+upper//2
if l[mid]<num:
    lower=mid+1
    mid=lower+upper//2
else:
    mid=lower+upper//2
    upper=mid
    
print('position',mid)
