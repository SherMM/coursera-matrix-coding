## Task 2
def dict2list(dct, keylist):
	return [dct[keylist[i]] for i in range(0,len(keylist))]

def list2dict(L, keylist):
	return {keylist[i]:L[i] for i in range(0,len(L))}

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return {i:L[i] for i in range(0, len(L))}

