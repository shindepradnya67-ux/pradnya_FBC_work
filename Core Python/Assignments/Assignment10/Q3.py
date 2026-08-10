# WAP to find second largest element in the list


li = [45, 34, 81, 77, 53, 26]

max = li[0]
second_max = li[0]

for i in range(1, len(li)):
    if li[i] > max:
        second_max = max
        max = li[i]

    elif li[i] > second_max and li[i] != max:
        second_max = li[i]

print("Maximum =", max)
print("Second largest =", second_max)