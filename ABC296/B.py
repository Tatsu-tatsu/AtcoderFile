alpha = ["a","b","c","d","e","f","g","h"]
for i in range(8):
  item = list(input())
  for j in range(len(item)):
    if item[j] == "*":
      print(alpha[j]+str(8 - i))
      exit()