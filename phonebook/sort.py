keys = {
  'name': lambda e: e[0],
  'number': lambda e: e[1]
}

k = input().strip()
# print(key)
if k not in keys:
  print("You must choose to sort by either 'name' or 'number'.")
  exit(1)

k = keys[k]

import sys
entries = []
for line in sys.stdin:
  line = line.strip()
  if not line:
    continue
  name, number = line.split(',', 1)
  entries.append((name, number))

def merge(lst1, lst2):
  ans = []
  i,j = 0,0
  while i < len(lst1) and j < len(lst2):
    if k(lst1[i]) < k(lst2[j]):
      ans.append(lst1[i])
      i += 1
    else:
      ans.append(lst2[j])
      j += 1
  
  while i < len(lst1):
    ans.append(lst1[i])
    i += 1
  
  while j < len(lst2):
    ans.append(lst2[j])
    j += 1
  
  return ans

def sort(lst):
  if len(lst) == 1: return lst

  n = len(lst)
  lst1 = sort(lst[:n>>1])
  lst2 = sort(lst[n>>1:])
  return merge(lst1, lst2)

entries = sort(entries)
print('\n'.join(','.join(map(str, e)) for e in entries), end='')