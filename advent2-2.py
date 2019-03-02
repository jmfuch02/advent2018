

def find_similar(inboxes: list):
    for i in range(len(inboxes)):
        for j in range(i, len(inboxes)):
            bad_counter = 0
            idx = 0
            for a in range(len(inboxes[i])):
                if inboxes[i][a] != inboxes[j][a]:
                    if bad_counter == 0:
                        bad_counter = 1
                        idx = a
                    elif bad_counter == 1:
                        bad_counter = 2
                        break
            if bad_counter == 1:
                return inboxes[i], inboxes[j], idx

testlist = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
]

x, y, z = find_similar(testlist)
assert x == 'fghij'
assert y == 'fguij'
assert z == 2

boxes = []
with open('input2.txt') as f:
    for line in f:
        boxes.append(line)

word1, word2, letter_id = find_similar(boxes)
print(f'Word1: {word1}')
print(f'Word2: {word2}')
print(f'Index: {letter_id}')
print(f'Answer: {word1[:letter_id] + word1[letter_id+1:]}')