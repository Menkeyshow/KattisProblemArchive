import sys

periods_of_constant_quality = int(input())
qaly = 0

for _ in range(periods_of_constant_quality):
    text = input()

    quality = float(text.split()[0])
    years = float(text.split()[1])

    qaly += quality * years
print(f"{qaly:.3f}")