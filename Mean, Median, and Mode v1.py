# Example without stat packages
size = int(input())
numbers = sorted(int(val) for val in input().split())


def mean(lst):
    return float(sum(lst)) / max(len(lst), 1)


def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    else:
        return sum(sorted(lst)[n // 2 - 1:n // 2 + 1]) / 2.0


def get_small_mode(lst):
    counts = {k: lst.count(k) for k in set(lst)}
    modes = sorted(dict(filter(lambda x: x[1] == max(counts.values()), counts.items())).keys())
    return modes[0]


print(mean(numbers))
print(median(numbers))
print(get_small_mode(numbers))


'''
INPUT:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

OUTPUT:
43900.6
44627.5
4978
'''

