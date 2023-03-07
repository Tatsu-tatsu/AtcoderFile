N = int(input())
X = list(map(int, input().split()))
X.sort()
nums = X[N:-N]
print(sum(nums) / len(nums))