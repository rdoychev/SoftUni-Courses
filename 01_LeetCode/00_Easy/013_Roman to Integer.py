s = "MCMXCIV"

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
previous = 0
number = 0

for i in range(len(s) - 1, -1, -1):
    current = roman[s[i]]
    if current < previous:
        number -= current
    else:
        number += current
    print(current, previous, number)
    previous = current

print(number)
