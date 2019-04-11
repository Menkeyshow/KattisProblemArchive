#%%
import sys
# f = open('1.txt', 'r')
# AllLines = f.read()
AllLines = sys.stdin.readlines()

#cast all strings to int while splitting didnt work :c
Lines = AllLines.split('\n')#[int(line) for line in AllLines.split('\n')]
#print(Lines)

X = int(Lines[0])
Y = int(Lines[1])
if(X>0 and Y>0):
    print(1)
if(X<0 and Y>0):
    print(2)
if(X<0 and Y<0):
    print(3)
if(X>0 and Y<0):
    print(4)
