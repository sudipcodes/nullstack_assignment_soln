inp = list(map(int, input().split(' ')))
n = inp[0]
arr = inp[1:]

for i in range(n):
    if arr[i] < 38:
        pass
    else:
        if arr[i]%5 >= 3:
            arr[i] = arr[i] + (5-(arr[i]%5))
for i in arr:
    print(i, end=" ")
print()

