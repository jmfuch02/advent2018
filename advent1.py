# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:09:52 2019

@author: Jason
"""

freq = 0
i = 0
input = []

# Add up all the frequency shifts
with open("input.txt") as file:
    for line in file:
        freq = freq + int(line)
    print (line, ' ',  freq)

'''        
with open("input.txt") as file:
    for line in file:
        print (i)
        input.append(tuple((freq, int(line), freq + int(line))))
        freq = freq + int(line)
        print (line, ' ',  freq)
        i = i + 1

'''
        
        

