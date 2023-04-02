H, W = map(int, input().split())
check = [[[] for _ in range(W+1)] for _ in range(H+1)]
A = list(map(int, input().split()))
check[1][1].append({A[0]})
for i in range(1, W+1):
  for item in check[1][i]:
    if item == []:
      break
    if not A[i] in item:
      check[1][i+1].append({A[i]} | item)
    else:
      break
for i in range(1, H+1):
  B = list(map(int, input().split()))
  # 左端
  for item in check[1][i]:
    if item == []:
      continue
    if not B[0] in item:
      check[i+1][1].append({B[0]} | item)
    else:
      continue
  # 左端以降
  for j in range(1, W+1):
    # 横
    for item in check[i+1][j]:
      if item == []:
        continue
      if not B[j] in item:
        check[i+1][j+1].append({B[j]} | item)
      else:
        continue
    # 縦
    for item in check[i][j+1]:
      if item == []:
        continue
      if not B[j] in item:
        check[i+1][j+1].append({B[j]} | item)
      else:
        continue
print(len(check[H][W]))