def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    from orthogonalization import orthogonalize
    oVecs = orthogonalize(L)
    return [v/(v*v)**(1/2) for v in oVecs]
    	
    	


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    from orthogonalization import aug_orthogonalize
    q, r = aug_orthogonalize(L)
    qList = orthonormalize(q)
    mults = [(v*v)**(1/2) for v in q]
    for vector in r:
    	for i in range(len(vector.D)):
    		vector[i] = vector[i] * mults[i]
    return qList, r
    
