n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

tickets.sort()
result = []

for price in customers:
    l, r = 0, len(tickets) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        if tickets[mid] <= price:
            ans = mid  
            l = mid + 1
        else:
            r = mid - 1

    if ans == -1:
        result.append(-1)
    else:
        result.append(tickets[ans])
        tickets.pop(ans) 

for val in result:
    print(val)
