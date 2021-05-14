def print_reverse(arr):
    for i in arr[::-1]:
        print(i, end=" ")

t = int(input())
i = 0
while i < t:
    n = int(input())
    arr = list(map(int, input().split(' ')[:n]))
    print_reverse(arr)
    print()
    i += 1
