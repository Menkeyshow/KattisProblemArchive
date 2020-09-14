#https://open.kattis.com/problems/pot

N = int(input())
sum = 0
for _ in range(N):
    numbers = input()
    power = int(numbers[-1])
    number = int(numbers[:-1])
    sum += number**power
print(sum)
