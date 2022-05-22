S = int(input())

a = S // 3600
a2 = S % 3600
b = a2 // 60
c = a2 % 60
# str()で文字列に変換。
print(str(a)+':'+str(b)+':'+str(c))

# f-stringを使う別解
print(f"{a}:{b}:{c}")