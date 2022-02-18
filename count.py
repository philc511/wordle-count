# TODO
# account for words with repeated letters
# show as percentage
# format output
# more words
# score list of words
# guess the word
# 
file1 = open('words.txt', 'r')
Lines = file1.readlines()

# each count value will be an array
# 0 - number of times letter appears (ie including duplicates)
# 1 - number of words letter appears in (ie excluding duplicates)
# 2-6 - number of times letter is used in position i-1
count = {}
for line in Lines:
  for i,c in enumerate(line.rstrip()):
    if c in count:
      count[c][0] = count[c][0] + 1
      count[c][i+1] = count[c][i+1] + 1
    else:
      count[c] = [1,0,0,0,0,0]
      count[c][i+1] = 1

marklist = sorted(count.items(), key=lambda x:x[1][1], reverse=True)
sortdict = dict(marklist)
for k in sortdict.keys():
  print(k,sortdict[k])
