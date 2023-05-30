import re

phone_numbers = []

with open('phone_numbers.txt', 'r') as f:
    for line in f:
        phone_numbers += re.findall(r'\+1\d{10}', line)

print(phone_numbers)
