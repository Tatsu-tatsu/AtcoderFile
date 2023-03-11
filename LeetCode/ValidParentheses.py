from collections import defaultdict
class Solution:
  def isValid(self, s: str) -> bool:
    checkMap = defaultdict(int)
    for item in s:
      if item == '(':
        checkMap['('] += 1
      elif item == '{':
        checkMap['{'] += 1
      elif item == '[':
        checkMap['['] += 1
      elif item == ')':
        if checkMap['('] > 0:
          checkMap['('] -= 1
        else:
          return False
      elif item == '}':
        if checkMap['{'] > 0:
          checkMap['{'] -= 1
        else:
          return False
      elif item == ']':
        if checkMap['['] > 0:
          checkMap['['] -= 1
        else:
          return False
    if checkMap['('] == 0 and checkMap['{'] == 0 and checkMap['['] == 0:
      return True
    else:
      return False

# 簡潔な解法
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    table = {
      '(': ')',
      '{': '}',
      '[': ']',
    }
    for char in s:
      if char not in table:
        if not stack or table[stack.pop()] != char:
          return False
      else:
        stack.append(char)
    if stack:
      return False
    else:
      return True