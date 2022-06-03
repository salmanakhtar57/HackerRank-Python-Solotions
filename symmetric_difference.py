#symmetric difference
M, M1 = (int(input()), input().split())
N, N1 = (int(input()), input().split())

x = set(M1)
y = set(N1)

p = y.difference(x)
q = x.difference(y)

result = p.union(q)
print('\n'.join(sorted(result, key=int)))