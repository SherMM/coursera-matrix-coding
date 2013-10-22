from random import randint
from dictutil import *

## Task 1
def movie_review(name):
	review_options = ["See it!", "A gem!", "Ideological claptrap!"]
	return review_options[randint(0,2)]
## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    d = dict()
    words = [b for i in range(0,len(strlist)) for (a,b) in enumerate(strlist[i].split())]
    for word in words:
    	s = set()
    	for i in range(0,len(strlist)):
    		if word in strlist[i].split():
    			s.add(i)
    	d[word] = s
    return d
    
## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    s = set()
    for word in query:
    	if word in inverseIndex.keys():
    		s.update(inverseIndex[word])
    return s
    	

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """ 
    s = inverseIndex[query[0]]
    for word in query[1:]:
    	if word in inverseIndex.keys():
    		s.intersection_update(inverseIndex[word])
    return s
    		
