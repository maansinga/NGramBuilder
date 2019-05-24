#!/usr/bin/env python
# coding: utf-8

# In[1]:
# @Author Sree Teja Simha G
# @email Sreetejasimha.Gemaraju@utdallas.edu
# @netid sxg177330

import os
import sys


# In[12]:
'''
buildUnigramDict builds a dictionary for unigrams with tokens as keys and counts as values
'''

def buildUnigramDict(tokens):
    unidict = {}
    for token in tokens:
        if unidict.get(token) is None:
            unidict[token] = 1
        else:
            unidict[token] += 1

    # unidict.pop('')

    return(unidict)


# In[13]:

'''
buildBigramDict builds a dictionary for bigrams with pairs of tokens combined as a single string - as keys and their counts as values
'''
def buildBigramDict(tokens):
    bidict = {}
    i = 0
    while i < len(tokens)-1:
        interp = "%s %s"%(tokens[i], tokens[i+1])
        if bidict.get(interp) is None:
            bidict[interp] = 1
        else:
            bidict[interp] += 1

        i+=1
    return(bidict)


# In[ ]:


if __name__ == "__main__":
    import Tokenizer
    f = open(sys.argv[1], encoding="utf-8")
    corpus = f.read()
    f.close()
    tokens = Tokenizer.corpusTokenizer(corpus)
    unidict = buildUnigramDict(tokens)
    print(unidict)
    bidict = buildBigramDict(tokens)
    print(bidict)

