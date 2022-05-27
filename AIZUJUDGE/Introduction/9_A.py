W = input()
words = []

while words == [] or words[-1] != 'END_OF_TEXT':
  s = input().split()
  words.extend(s)

cnt = 0

for word in words:
  if word == W:
    cnt += 1

print(cnt)