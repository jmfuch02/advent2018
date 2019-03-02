
def compute_checksum(input: list):

    two_times: int = 0
    three_times: int = 0

    for item in input:
        counter = {}
        for letter in item:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        if 2 in counter.values():
            two_times += 1
        if 3 in counter.values():
            three_times += 1

    checksum: int = two_times * three_times
    return checksum


checklist = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]
assert compute_checksum(checklist) == 12

boxes = []
with open('input2.txt') as f:
    for line in f:
        boxes.append(line)

print(compute_checksum(boxes))

