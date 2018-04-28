import random


# randomizes a list in O(n)
def fy_shuffle(arr):
    for i in range(len(arr) - 1, 1, -1):
        j = random.randrange(0, i)
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
    return arr

print fy_shuffle([1, 0, 3, 9, 2])
