# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:09:52 2019

@author: Jason
"""

# Add up all the frequency shifts
def get_freq_1():
    freq = 0
    with open("input.txt") as file:
        for line in file:
            freq = freq + int(line)
            print(line, ' ',  freq)


def find_repeat_2(changes: list):
    found: bool = False

    changes = file_to_list()

    while found is False:
        print('Round #', count)
        for change in changes:
            if found is False:
                freq = freq + int(change)
                # print(line, ' ', freq)
                if freq not in freqs:
                    print(f'Found a new frequency: {freq}')
                    freqs.append(int(freq))
                else:
                    found = True
                    print('First repeated frequency is', freq)
                    return freq
        print(f'Freq at end of round {count} is {freq}')
        count += 1


def apply_changes(changes, starting_freq=0,  frequency_list=[0]):
    freqs = frequency_list
    freq = starting_freq

    for change in changes:
        freq = freq + int(change)
        if freq not in freqs:
            freqs.append(freq)
        else:
            print(f'Frequency {freq} is a repeat')
            return freq, freqs
    return freq, freqs


def file_to_list():
    changes = []
    with open("input.txt") as file:
        for line in file:
            changes.append(int(line))
    return changes


