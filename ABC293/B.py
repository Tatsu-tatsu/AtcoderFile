N = int(input())
A = list(map(int, input().split()))
items = set()
for i in range(len(A)):
  if not i+1 in items:
    items.add(A[i])
count = 0
ans = []
for i in range(1, N+1):
  if i not in items:
    count += 1
    ans.append(i)
print(count)
for item in ans:
  print(item, end=' ')
