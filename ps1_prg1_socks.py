n = int(input())
arr = list(map(int, input().split(' ')[:n]))

elem = {}
for i in arr:
    elem[i] = 0
for i in arr:
    elem[i] += 1
sum = 0
for value in elem.values():
    sum += int(value/2)

print(sum)