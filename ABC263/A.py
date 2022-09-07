A = list(map(int, input().split()))
A_num = list(set(A))
for i in A_num:
  if A.count(i) == 2 or A.count(i) == 3:
    continue
  elif A.count(i) == 4 or A.count(i) ==1 or A.count(i) == 5:
    print("No")
    exit()

print("Yes")

## 解答
## 13桁しかないので、ある桁をカウントしていって、ソートして上位2つが3個、2個であれば正解