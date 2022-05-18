A = list(map(int, input().split()))

taka = A[0] * A[1] + A[2]
aoki = A[3] * A[4] + A[5]

taka_1 = A[6] // (A[0] + A[2])
aoki_1 = A[6] // (A[3] + A[5])

taka_2 = A[6] % (A[0] + A[2])
aoki_2 = A[6] % (A[3] + A[5])

if taka_2 <= A[0]:
  taka_3 = taka_2 
  taka_3
elif taka_2 > A[0]:
  taka_3 = A[0]
  taka_3

if aoki_2 <= A[0]:
  aoki_3 = aoki_2 
  aoki_3
elif aoki_2 > A[0]:
  aoki_3 = A[0]
  aoki_3

 

taka_long = taka_1 * A[0] * A[1] + taka_3 * A[1]
aoki_long = aoki_1 * A[3] * A[4] + aoki_3 * A[4]
if taka_long == aoki_long:
  print("Draw")
elif taka_long > aoki_long:
  print("Takahashi")
elif taka_long < aoki_long:
  print("Aoki")

