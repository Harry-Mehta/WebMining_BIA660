#!/usr/bin/env python
# coding: utf-8

# In[44]:


import logging
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


id2word = gensim.corpora.Dictionary.load_from_text('Result_wordids (2).txt.bz2')
# load corpus iterator

mm = gensim.corpora.MmCorpus('Result_tfidf.mm.index')

print(mm)
# extract 20 LDA topics, using 1 pass and updating once every 1 chunk (10,000 documents)
lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=20, update_every=1, passes=1)
lda.print_topics(20)


# In[45]:


#Random wiki pages text files converted into corpus format

with open('doc1.txt', 'r') as file:
    doc1 = file.read().replace('\n', '')
input_corpus_1 = [word for word in doc1.lower().split()]
        
with open('doc2.txt', 'r') as file:
     doc2 = file.read().replace('\n', '')
input_corpus_2 = [word for word in doc2.lower().split()]

with open('doc3.txt', 'r') as file:
     doc3 = file.read().replace('\n', '')
input_corpus_3 = [word for word in doc3.lower().split()]


# In[ ]:


#created lda model ran on each document to check it's topic probability
#get topic probability distribution for a document
doc = id2word.doc2bow(input_corpus_1)
vector = lda[doc]  

print(vector)

doc = id2word.doc2bow(input_corpus_2)
vector = lda[doc]  
print(vector)

doc = id2word.doc2bow(input_corpus_3)
vector = lda[doc]  
print(vector)

