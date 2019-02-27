# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:09:52 2019

@author: Jason
"""


# Add up all the frequency shifts
def get_freq():
    freq = 0
    with open("input.txt") as file:
        for line in file:
            freq = freq + int(line)
            print(line, ' ',  freq)


def loop_device(change_list):
    seen_freqs = []
    freq = 0
    seen_freqs.append(freq)

    while True:
        for change in change_list:
            current_frequency = freq
            resulting_frequency = current_frequency + int(change)

            if resulting_frequency not in seen_freqs:
                # print(f'Current frequency {current_frequency},'
                #       f'change of {int(change)};'
                #       f'resulting frequency {resulting_frequency}')
                seen_freqs.append(resulting_frequency)
            else:
                # print(f'Current frequency {current_frequency},'
                #       f'change of {int(change)};'
                #       f'resulting frequency {resulting_frequency},'
                #       f'which has already been seen.')
                return resulting_frequency

            # Reset for next time
            freq = resulting_frequency


def file_to_list(filename):
    changes = []
    with open(filename) as file:
        for line in file:
            changes.append(int(line))
    return changes


