import numpy as np

largest = None
smallest = None
count = 0
l = []

while 1:
    i = input()
    if i.isnumeric():
        i = int(i)
        l.append(i)
        if largest is None or i > largest:
            largest = i
        if smallest is None or i < smallest:
            smallest = i
    elif i == 'done':
        break
    count += 1

average = np.mean(l)
total = sum(l)

print(f"Count: {count} \n Total: {total} \n Average: {average} \n Largest: {largest} \n Smallest: {smallest}")
