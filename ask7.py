print "dwste tis lexeis xwrismenes me keno"

# oles oi lexeis mazi
words = raw_input()
seperated = words.split(" ") # array kai se ka8e cell mia lexh ths eisodou

maxLen = len(seperated[0]) # max len to mhkos ths prwths lexhs
longestWord = ""

for i in range (len(seperated)):
	if maxLen <= len(seperated[i]): # an einai to maxlen <= ths current lexis
		longestWord = seperated[i]
		maxLen = len(longestWord)

print longestWord
