#!/usr/bin/env python3

arr = [1, 1]  # Initital
print("{0}\n".format(arr[0]))

while True:
    print("{0}\n".format(arr[-1]))
    tmp = sum(arr)
    arr.append(tmp)
    del arr[0]
