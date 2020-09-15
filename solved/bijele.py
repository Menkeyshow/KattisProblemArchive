#  https://open.kattis.com/problems/bijele

set = {
    "kings": 1,
    "queens": 1,
    "rooks": 2,
    "bishops": 2,
    "knights": 2,
    "pawns": 8
}
txt = input()
txt = txt.split()

valid = [x-int(y) for x, y in zip(set.values(), txt)]
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
print(*valid, sep=" ")
