#S. Intersection Operation
n = int(input())
n1 = set(map(int,input().split()))

b = int(input())
b1 = set(map(int,input().split()))

result = n1.intersection(b1)
count = 0
for i in result:
    count += 1
print(count)