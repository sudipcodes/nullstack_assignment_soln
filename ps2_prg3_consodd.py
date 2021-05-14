def print_output(inp):
    if inp == 1:
        print("yes")
    else:
        print("no")

t = int(input())
for y in range(t):
    nk = list(map(int, input().split(' ')[:2]))
    n = nk[0]
    k = nk[1]
    arr = list(map(int, input().split(' ')[:n]))
    non_dec = False
    a = arr[0]
    for i in arr[1:]:
        if i > a:
            non_dec = True
            break
        else:
            a = i
    if not non_dec:
        print_output(0)
        continue
    num_odd = 1
    max_odd = 1
    for i in range(n-1):
        if arr[i]%2==1 and arr[i+1]%2==1:
            num_odd += 1
            if num_odd > max_odd:
                max_odd = num_odd
        else:
            num_odd = 1
    if max_odd >= k:
        print_output(1)
    else:
        print_output(0)