from curses.ascii import islower, isupper

S = input()

if S.islower()==False and S.isupper() ==False:
  li = list(S)
  if len(set(li)) == len(li):
    print("Yes")
  else:
    print("No")
else:
  print("No")