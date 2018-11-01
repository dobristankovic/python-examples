# Example without stat packages
size = int(input())
numbers = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]

s = 0
w = 0
for i in range(size):
    w = w + numbers[i] * weights[i]
    s = s + weights[i]

print(round(w / s, 1))

'''
INPUT:
5
10 40 30 50 20
1 2 3 4 5

OUTPUT:
32.0


INPUT:
10
10 40 30 50 20 10 40 30 50 20
1 2 3 4 5 6 7 8 9 10

OUTPUT:
31.1
'''
