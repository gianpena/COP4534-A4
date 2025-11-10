words = []

def ending(n):
  ones = n%10
  tens = (n//10)%10

  if ones == 0 or ones > 3: return 'th'
  if ones == 3:
    return 'rd' if tens != 1 else 'th'
  if ones == 2:
    return 'nd' if tens != 1 else 'th'
  return 'st' if tens != 1 else 'st'

with open("dictionary.txt", "r") as file:
  for line in file:
    word = line.strip()
    if word:
      words.append(word)

  def lookup(word):

    def search(i,j):
      if i == j:
        if words[i] == word: return i
        return -1
      
      m = i + ((j-i) >> 1)
      if word < words[m]:
        return search(i, m-1)
      elif word > words[m]:
        return search(m+1, j)
      else:
        return m
    
    return search(0, len(words)-1)
  
  wordToLookUp = input().lower()
  position = lookup(wordToLookUp)
  if position == -1:
    print("Your word could not be found in the dictionary.", end='')
    exit(1)
  else:
    print(f'{wordToLookUp} is the {position+1}{ending(position+1)} word in the dictionary.', end='')
