# num = list(map(int, input().split()))
# table = [[0,0,0] for _ in range(3)]
# print(num)
# print(table)
# i = 0
# while table[0][0]+table[0][1]+table[0][2] != num[0]:


# 違う方法
num = list(map(int, input().split()))
ans = {"h1":[], "h2":[], "h3":[], "w1":[], "w2":[], "w3":[]}
for k in range(6):
  for i in range(1, num[k]+1):
    for j in range(1, num[k]+1):
      if num[0]-i-j>0:
        if k<=2:
          ans["h"+str(k+1)].append([i, j, num[k]-i-j])
        else:
          ans["w"+str(k-2)].append([i, j, num[k]-i-j])

print(ans)