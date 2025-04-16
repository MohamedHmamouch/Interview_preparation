n = int(input())

events = []

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))   # arrival: +1
    events.append((b, -1))  # leaving: -1

# Sort by time — if times are equal, departure (-1) before arrival (+1)
events.sort()

current = 0
maximum = 0

for time, delta in events:
    current += delta
    maximum = max(maximum, current)

print(maximum)
