# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:09:52 2019

@author: Jason
"""

freq = 0
input = []
freqs = []

# Add up all the frequency shifts
with open("input.txt") as file:
    for line in file:
        input.append(tuple((freq, int(line), freq + int(line))))
        freq = freq + int(line)
    print (line, ' ',  freq)


def find_repeat(input_list, freqs):
    for tuple_item in input_list:
        if tuple_item[2] in freqs:
            return tuple_item[2]
        else:
            freqs.append(tuple_item[2])
    return "None"

answer = "None"
while answer == "None":
    answer = find_repeat(input, freqs)
    print (answer)



    
        

