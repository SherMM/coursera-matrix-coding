# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    nonZeroIndex = 0
    for i in range(len(A)):
    	found = False
    	for j in range(len(A[i])):
    		if not found:
    			if A[i][j] != 0:
    				if i == 0:
    					nonZeroIndex = j
    					found = True
    				else:
    					if j <= nonZeroIndex:
    						return False
    					else:
    						nonZeroIndex = j
    						found = True
    		else:
    			break
    return True



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    from vecutil import zero_vec
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        for k in label_list:
        	row = rowlist[j]
        	if row[k] != 0:
        		x[k] = (b[j] - x*row)/row[k]
        		break
    return x



## Problem 6
rowlist = [Vec({'B', 'C', 'A', 'D'},{'A': one,'B':one,'D':one}),Vec({'B', 'C', 'A', 'D'},{'B': one}),Vec({'B', 'C', 'A', 'D'},{'C': one}),Vec({'B', 'C', 'A', 'D',},{'D': one})]    # Provide as a list of Vec instances
label_list = ['A','B','C','D'] # Provide as a list
b = [one, one, 0, 0]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [8/5,16/5]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-0.16666666666666666, -0.3333333333333333, 0.16666666666666666]
projection_orthogonal_2 = [1.1666666666666667, 1.3333333333333333, 3.8333333333333335]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

