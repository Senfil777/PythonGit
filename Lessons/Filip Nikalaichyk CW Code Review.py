li = [3, 5, 2, 0]  # 0, 2, 3, 5
swapped = True
print(li)

while swapped:
    swapped = False

    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            swapped = True

print(li)