#Given two integers A and B (A <= B). Print all numbers from A to B inclusively.

A = int(input('введите значение A: '))
B = int(input('введите значение B: '))
print(list(range(A,B+1)))