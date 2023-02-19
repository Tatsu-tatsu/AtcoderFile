# 実行時errorが一つ
H, M = input().split()
while True:
  if len(H) == 1:
    H = '0' + H
  if len(M) == 1:
    M = '0' + M
  h = H[0] + M[0]
  m = H[1] + M[1]
  if int(h) < 24 and int(m) < 60:
    print(H, M)
    exit()
  else:
    if int(M)<59:
      M = str(int(M)+1)
    elif int(H) == 23:
      H = '00'
      M = '00'
    else:
      H = str(int(H)+1)
      M = '00'
