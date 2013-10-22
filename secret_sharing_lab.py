# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
	u_found = False
	while not u_found:
		u = list2vec([randGF2() for i in range(6)])
		if a0*u == s and b0*u == t:
			u_found = True
			return u 
		



## Problem 2
# Give each vector as a Vec instance

secret_a0 = list2vec([one, one, 0, one, 0, one])
secret_b0 = list2vec([one, one, 0, 0, 0, one])
secret_a1 = list2vec([0, one, 0, 0, one, 0])
secret_b1 = list2vec([one, 0, one, 0, one, 0])
secret_a2 = list2vec([one, one, one, one, one, one])
secret_b2 = list2vec([0, one, one, 0, 0, one])
secret_a3 = list2vec([0, 0, 0, one, one, 0])
secret_b3 = list2vec([one, 0, one, one, one, one])
secret_a4 = list2vec([one, one, one, 0, one, 0])
secret_b4 = list2vec([0, 0, one, 0, 0, 0])


def growSec():
	from independence import is_independent
	from itertools import combinations
	proven = [(a0,b0)]
	found = False
	while not found:
		t = [(list2vec([randGF2() for i in range(6)]),list2vec([randGF2() for i in range(6)])) for j in range(2)]
		vecs = proven + t
		if all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
			found = True
			proven += t
	
	found1 = False
	while not found1:
		t1 = [(list2vec([randGF2() for i in range(6)]),list2vec([randGF2() for i in range(6)])) for j in range(2)]
		vecs1 = proven + t1
		if all(is_independent(list(sum(x,()))) for x in combinations(vecs1,3)): 
			found1 = True
			proven += t1
	
	return proven		
	
			
	
			
	
		
	
		
	
		