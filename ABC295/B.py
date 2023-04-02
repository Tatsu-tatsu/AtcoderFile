R, C = map(int, input().split())
maps = []
nums = {}
for i in range(R):
    item = list(input())
    maps.append(item)
    for j in range(C):
        if item[j] != "." and item[j] != "#":
            nums[(i, j)] = item[j]
for i in range(R):
    for j in range(C):
        for k, v in nums.items():
            if abs(i-k[0]) + abs(j-k[1]) <= int(v):
                maps[i][j] = "."
for i in range(R):
    print("".join(maps[i]))