# Example with statistics and built-in packages
import numpy
import statistics

size = int(input())
numbers = sorted(int(val) for val in input().split())

print(numpy.mean(numbers))
print(numpy.median(numbers))
print(statistics.mode(numbers))


'''
INPUT:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

OUTPUT:
43900.6
44627.5
4978
'''
