# -*- coding: utf-8 -*-
#started here: https://opendata.stackexchange.com/questions/7042/ascii-character-frequency-analysis
#frequency tables from here: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
#better tables here https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html

import string      # definitions of ascii printable chars
from collections import defaultdict     # fast counting
import codecs
import operator

d = defaultdict(int)    # define dictionary for counting frequencies

# define text - see below for how to download from a url
#text = '''Lorem ipsum dolor sit amet,\tconsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
f = open("encrypted.txt", "rb")
text = f.read()
#print(text)
f.close()
total = 0
for ch in text:       # loop over each character 
    #if ch in string.printable:     # is the character in the ascii/printable set?
	d[ch] += 1    #   if so, add 1 to that characters frequency counter
	total += 1

#print(d)     # print all frequencies


letterperc = defaultdict(int)

amountletters = 0
for i in d:
    
    perc = float(d[i]) / total
    perc *= 100

    letter = i
    #letter = letter[2:]
    #print(chr(letter) + ": " + str(perc))
    letterperc[letter] = float(perc)
    amountletters += 1

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sorted_x = sorted(letterperc.items(), key=lambda kv: kv[1])
sorted_x.reverse()


#get english frequencies || letter frequency dictonary
di = defaultdict(str)
orderedlist = [" "]

f = open("LetterFrequency.txt", "r")
for i in f:
	line = i.split("\t")
	di[str(line[0][:1])] = float(line[1])
	orderedlist.append(line[0][:1])

f.close()



#print final result
exchange = defaultdict(int)
for i in range(len(sorted_x)):
    try:
        print(chr(sorted_x[i][0]) + ": " + str(sorted_x[i][1]) + "(Orded Similar to {})".format(orderedlist[i]))
    except:
        print(chr(sorted_x[i][0]) + ": " + str(sorted_x[i][1]) + "(Orded Similar to ?)")
