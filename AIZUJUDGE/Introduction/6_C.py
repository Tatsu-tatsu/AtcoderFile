n = int(input())

data = [[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10],[[0]*10,[0]*10,[0]*10]]

for i in range(n):
  b, f, r, v = map(int, input().split())
  data[b-1][f-1][r-1] = v

for bu in data:
  if data[0] != bu :
    print("####################")
  for fl in bu:
    for ro in fl:
      print(str(ro)+" ", end="")
    print()

# 3次元配列の問題。丁寧に配列を攻略していけば可能。