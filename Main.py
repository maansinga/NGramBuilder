#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[76]:
# @Author Sree Teja Simha G
# @email Sreetejasimha.Gemaraju@utdallas.edu
# @netid sxg177330

import sys
from functools import reduce


import Tokenizer
import NgramBuilderv2


# In[116]:

'''
Computes unigram counts for tokens
'''
def unigramCounts(tokens, unigramDict):
    unigram_counts = {}
    for token in tokens:
        g = unigramDict.get(token)
        if g == None:
            unigram_counts[token] = 0
        else:
            unigram_counts[token] = g
            
    return unigram_counts

'''
Computes bigram counts for adjacent token pairs
'''
def bigramCounts(tokens, bigramDict):
    unique_tokens = []
    #for tok in tokens:
    #   if tok not in unique_tokens:
    #       unique_tokens.append(tok)
            
    unique_tokens = tokens
    bigram_counts = []
    for k in unique_tokens:
        bigram_counter = []
        for j in unique_tokens:
            interp = "%s %s"%(k, j)
            g = bigramDict.get(interp)
            
            if g==None:
                bigram_counter.append(0)
            else:
                bigram_counter.append(g)
        bigram_counts.append(bigram_counter)
        
    return((unique_tokens, bigram_counts))

'''
Displays bigram counts without add one smoothing
'''
def displayBigramCounts(bcounts):
    (unique_tokens, matrix) = bcounts
    len_tok = len(unique_tokens)
    pattern = "%-16s "+"%4s "*len_tok
    print("V -------------------------------------------------------------------->")
    for i in range(len_tok):
        pattern_fill = tuple([unique_tokens[i],]+matrix[i])
        print(pattern%pattern_fill)
    print()

'''
Computes bigram probabilities without add one smoothing
'''
def bigramProbabilities(bcounts, unigramDict):
    (unique_tokens, matrix) = bcounts
    new_matrix = []
    i = 0
    
    for each_row in matrix:
        prior = unigramDict.get(unique_tokens[i])
        new_matrix.append([(float(count)/float(prior) if prior is not None else 0) for count in each_row])
        i += 1
        
    return(unique_tokens, new_matrix)

'''
Displays bigram probabilities without add one smoothing
'''
def displayBigramProbabilities(bprobs):
    (unique_tokens, matrix) = bprobs
    len_tok = len(unique_tokens)
    pattern = "%-16s "+"%1.4f "*len_tok
    print("V -------------------------------------------------------------------------------------->")
    for i in range(len_tok):
        pattern_fill = tuple([unique_tokens[i],]+matrix[i])
        print(pattern%pattern_fill)
    print()

'''
Computes bigram counts with add one smoothing
'''    
def bigramAddOneCounts(tokens, bigramDict):
    unique_tokens = []
    #for tok in tokens:
    #   if tok not in unique_tokens:
    #       unique_tokens.append(tok)
            
    unique_tokens = ['',]+tokens
    bigram_counts = []
    for k in unique_tokens:
        bigram_counter = []
        for j in unique_tokens:
            interp = "%s %s"%(k, j)
            g = bigramDict.get(interp)
            
            if g==None:
                bigram_counter.append(1)
            else:
                bigram_counter.append(g+1)
        bigram_counts.append(bigram_counter)
        
    return((unique_tokens, bigram_counts))

'''
Computes bigram probabilities with add one smoothing
'''    
def bigramAddOneProbabilities(bcounts, unigramDict):
    V = len(unigramDict.keys())
    N = reduce(lambda a,b: a+b, unigramDict.values())
    
    (unique_tokens, matrix) = bcounts
    new_matrix = []
    i = 0
    
    for each_row in matrix:
        prior = unigramDict.get(unique_tokens[i])
        prior = prior if prior is not None else 0;
        new_matrix.append([float(count+1)/float(prior+V) for count in each_row])
        i += 1
        
    return(unique_tokens, new_matrix)

'''
Computes sentence probability using bigram sparse matrices
'''    
def getBigramProbability(token_probs):
    (unique_tokens, matrix) = token_probs
    len_tok = len(matrix)
    accum = 1
    for i in range(len_tok-1):
        accum *= matrix[i][i+1]
        
    return(accum)


# In[137]:


if __name__ == "__main__":
    unigramDict = None
    bigramDict = None

    if(len(sys.argv)<4):
        print("Usage: Main.py <CorpusFilePath> \"<Sentence1>\" \"<Sentence2>\"")
        exit(0)
        
    corpus_file = sys.argv[1]
    S1 = sys.argv[2]
    S2 = sys.argv[3]
    with open(corpus_file, encoding="utf-8") as corpus_file_handle:
        corpus = corpus_file_handle.read()
        tokens = Tokenizer.corpusTokenizer(corpus)
        unigramDict = NgramBuilderv2.buildUnigramDict(tokens)
        bigramDict = NgramBuilderv2.buildBigramDict(tokens)


    # Sentence1 tokens
    s1_tokens = Tokenizer.corpusTokenizer(S1)
    # s1_tokens

    # Sentence2 tokens
    s2_tokens = Tokenizer.corpusTokenizer(S2)
    # s2_tokens

    # Sentence1 unigram counts
    unigramCounts(s1_tokens, unigramDict)
    # Sentence2 unigram counts
    unigramCounts(s2_tokens, unigramDict)

    # Sentence1 bigram counts
    s1_bcount = bigramCounts(s1_tokens, bigramDict)
    # Sentence2 bigram counts
    s2_bcount = bigramCounts(s2_tokens, bigramDict)

    # Displaying bigram counts
    print("Bigram counts for s1 without smoothing")
    displayBigramCounts(s1_bcount)
    print("Bigram counts for s1 without smoothing")
    displayBigramCounts(s2_bcount)

    # Computing bigram probabilities sparse matrices without smoothing for sentences 1 and 2
    s1_probs = bigramProbabilities(s1_bcount, unigramDict)
    s2_probs = bigramProbabilities(s2_bcount, unigramDict)

    # Displaying bigram probabilities sparse matrices wihout smoothing for sentences 1 and 2
    print("Bigram probabilities for s1 without smoothing")
    displayBigramProbabilities(s1_probs)
    print("Bigram probabilities for s2 without smoothing")
    displayBigramProbabilities(s2_probs)

    #Computing bigram probabilities of sentences 1 and 2 without smoothing
    ps1_nosmooth = getBigramProbability(s1_probs)
    ps2_nosmooth = getBigramProbability(s2_probs)

    print("Bigram probabilities without smoothing are: s1(%10.8ef)\ts2(%10.8ef)"%(ps1_nosmooth, ps2_nosmooth))

    # Computing AddOne smoothed bigram counts
    s1_aocounts = bigramAddOneCounts(s1_tokens, bigramDict)
    s2_aocounts = bigramAddOneCounts(s2_tokens, bigramDict)

    # Computing AddOne bigram probabilities sparse matrices for sentences 1 and 2
    s1_aoprobs = bigramAddOneProbabilities(s1_bcount, unigramDict)
    s2_aoprobs = bigramAddOneProbabilities(s2_bcount, unigramDict)

    # Displaying bigram counts with smoothing for sentences 1 and 2
    print("Bigram counts for s1 with smoothing")
    displayBigramCounts(s1_aocounts)
    print("Bigram counts for s2 with smoothing")
    displayBigramCounts(s2_aocounts)

    # Displaying bigram probabilities with smoothing for sentences 1 and 2
    print("Bigram probabilities for s1 with smoothing")
    displayBigramProbabilities(s1_aoprobs)
    print("Bigram probabilities for s2 with smoothing")
    displayBigramProbabilities(s2_aoprobs)

    #Computing bigram probabilities of sentences 1 and 2 without smoothing
    ps1_smooth = getBigramProbability(s1_aoprobs)
    ps2_smooth = getBigramProbability(s2_aoprobs)
    print("Bigram probabilities with smoothing are: s1(%10.8ef)\ts2(%10.8ef)"%(ps1_smooth, ps2_smooth))


# In[ ]:




