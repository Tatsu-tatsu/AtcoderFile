N = int(input())
S = list(input())
now = S[0]
for i in range(1, N):
    if now == "M":
        if S[i] == "F":
            now = "F"
            continue
        print("No")
        exit()
    elif now == "F":
        if S[i] == "M":
            now = "M"
            continue
        print("No")
        exit()
print("Yes")