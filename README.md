# Homework 2 N-grams.
### Author  **Sree Teja Simha Gemaraju**
### Email    **Sreetejasimha.gemaraju@utdallas.edu**
#### THIS IS AN ACAD. SUBMISSION. DO NOT COPY/DERIVE FROM THIS.

### About
This is an implementation of NGrams with smoothing. More can be found here - 
https://en.wikipedia.org/wiki/Bigram

#### Files in this project
-------------------------------------------------------------------------------------------------------------------------
| File | Purpose |
|-----------------|----------------------------------------------------------------------------------------|
| Main.py | This is the actual application |
| NgramBuilderv2.py | This library builds uni/bigrams with/without smoothing |
| Tokenizer.py | This library applies a regular expression to breakdown corpus/test strings into tokens |12345

The details of the application are within the files as comments

### Execution
--------------------------------------------------------------------------------------------------------------------------

`python Main.py <CorpusFileAbsolutePath> <Sentence1> <Sentence2>`

Example: 
`python .\Main.py .\corpus.txt "Facebook announced plans to built a new datacenter in 2018" "Facebook is an American social networking service company in California"`
    
### Observations
---------------------------------------------------------------------------------------------------------------------------
Without smoothing the result for
`python Main.py corpus.txt "Facebook is good" "Facebook is an American online social media and social networking service company based in Menlo Park, California. "`

are...
Bigram probabilities without smoothing are: s1(0.00000000e+00f)    s2(8.18979388e-18f)
Bigram probabilities with smoothing are: s1(2.08183355e-06f)    s2(1.30979303e-46f)

Although sentence2 is same as a sentence in the corpus, this happens because adding 1 counts of most bigrams. Thus the zero occuring bigrams are now just as prevalent as 1time occuring bigrams.
