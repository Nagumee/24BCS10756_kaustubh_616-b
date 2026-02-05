import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    
    if n <= 4:
        results.append('-1')
        continue
    
    if n == 5:
        p = [1, 3, 5, 4, 2]
    else:
        
        odds = []
        for i in range(1, n + 1, 2):
            if i != 5:
                odds.append(i)
        evens = []
        for i in range(2, n + 1, 2):
            if i != 4:
                evens.append(i)
        p = odds + [5, 4] + evens
    
    valid = True
    for i in range(n - 1):
        if is_prime(p[i] + p[i + 1]):
            valid = False
            break
    
    if valid:
        results.append(' '.join(map(str, p)))
    else:
        results.append('-1')

print('\n'.join(results))
