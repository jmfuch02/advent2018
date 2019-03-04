import re
import numpy as np

elf_claims = []
with open('input3.txt') as f:
    for line in f:
        elf_claims.append(line)


def place_items(items):
    big_fabric = np.zeros((10000, 10000))
    for item in items:
        x = int(item[1])
        y = int(item[2])
        width = int(item[3])
        height = int(item[4])

        big_fabric[x : x + width, y : y + height] += 1
    area_covered = len(big_fabric[np.where(big_fabric > 1)])

    return area_covered


def parse_claims(claims):
    claims_parsed = []
    for claim in claims:
        claims_parsed.append(re.split(' @ |,|: |x', claim.replace('#', '')))
    return claims_parsed


test_claims = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]

assert (place_items(parse_claims(test_claims))) == 4

print(place_items(parse_claims(elf_claims)))





