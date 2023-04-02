N = int(input())
A = input().split()
for i in range(N):
    if A[i] == "and" or A[i] == "not" or A[i] == "that" or A[i] == "the" or A[i] == "you":
        print("Yes")
        exit()
print("No")