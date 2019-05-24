#!/usr/bin/env python
# coding: utf-8

# In[17]:
# @Author Sree Teja Simha G
# @email Sreetejasimha.Gemaraju@utdallas.edu
# @netid sxg177330

import re
import sys
import os


# In[18]:

'''
This function takes contents of a corpus file and applies regular expressions to extract tokens. The regular expression tries its best to split
the lines into proper words and sentences. The line terminator is represented by a null string "". The line terminator has also been used in the
statistical evaluation of bigrams. Every sentence must begin with a line terminator and must end with a line terminator. With the addition of line
terminators, there was significant improvement in the difference between probabilities of candidate test sentences.

The same tokenization function shall also be applied on the input sentences. The same rules for breaking down corporal sentences into tokens applies
to them too.
'''
def corpusTokenizer(corpus):
    rx = re.compile("[\s\(\"\-]*([a-zA-Z]+\.com|(?:[\(\"]*)[a-zA-Z+\'\’]+|Inc\.|\$?[0-9]+(?:[\,\.][0-9]+)?\%?|[a-zA-Z]+[\.\n\r\t])?[\s\,\;\"\)\-]*")
    alltokens = rx.findall(corpus)

    finalpass = []
    spacehit = False
    for k in alltokens:
        # k.replace('’',"'")
        # if not spacehit:
        #     finalpass.append(k.lower())
        #     if k == '':
        #         spacehit = True
        # else:
        #     if k != '':
        #         spacehit = False
        #         finalpass.append(k.lower())
        k.replace('’',"'")
        if k != '':
            finalpass.append(k.lower())

    return(finalpass)


# In[19]:


if __name__=="__main__":
    f = open(sys.argv[1], encoding='utf-8')
    fall = f.read()
    f.close()

    finalpass = corpusTokenizer(fall)
    print(finalpass)


# In[ ]:




