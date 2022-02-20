# TODO
# DONE account for words with repeated letters
# show as percentage
# format output
# more words
# score list of words
# guess the word
# 

def score(word, letter_counts):
  s = 0
  for i,c in enumerate(word):
    s=s+letter_counts[c][i+2]
  return s

file1 = open('words.txt', 'r')
Lines = file1.readlines()
words = [x.rstrip() for x in Lines]

# each count value will be an array
# 0 - number of words letter appears in (ie excluding duplicates)
# 1 - number of times letter appears (ie including duplicates)
# 2-6 - number of times letter is used in position i-1
count = {}
for line in words:
  word = line
  letters = set(word)
  for c in letters:
    if c in count:
      count[c][0] = count[c][0] + 1
    else:
      count[c] = [1,0,0,0,0,0,0]
  for i,c in enumerate(word):
    count[c][1] = count[c][1] + 1
    count[c][i+2] = count[c][i+2] + 1

marklist = sorted(count.items(), key=lambda x:x[1][0], reverse=True)
sortdict = dict(marklist)
for k in sortdict.keys():
  print(k,sortdict[k])

scored_words = [(w, score(w, count)) for w in words]
print(sorted(scored_words, key=lambda x:x[1], reverse=True))

# show guess
# get result of guess
# update list of correct letters, set of included letters
