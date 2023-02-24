class Solution:
  def isPalindrome(self, s: str) -> bool:
    strings = ''.join(ch for ch in s if ch.isalnum())
    item = strings.lower()
    print(item)
    length = len(item)
    for i in range(length//2):
      if item[i] != item[length-i-1]:
        return False
    return True
