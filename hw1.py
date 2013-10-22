# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [x+y for x,y in zip(p1_v, p1_u)]
p1_v_minus_u = [x-y for x,y in zip(p1_v, p1_u)]
p1_three_v_minus_two_u = [3*x-2*y for x,y in zip(p1_v, p1_u)]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [x+y for x,y in zip(p2_v, p2_u)]
p2_v_minus_u = [x-y for x,y in zip(p2_v, p2_u)]
p2_two_v_minus_u = [2*x-y for x,y in zip(p2_v, p2_u)]
p2_v_plus_two_u = [x+2*y for x,y in zip(p2_v, p2_u)]



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [one, 0, 0]
p3_vector_sum_2 = [0, one, one]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

u_0010010 = {'c','d','e'}
u_0100010 = {'b','c','d','e'}



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'c','d'}
v_0100010 = set()



## Problem 6
uv_a = sum([x*y for x,y in zip([1,0],[5,4321])])
uv_b = sum([x*y for x,y in zip([0,1],[12345,6])])
uv_c = sum([x*y for x,y in zip([-1,3],[5,7])])
uv_d = sum([x*y for x,y in zip([-1*((2**(1/2))/2), (2**(1/2))/2], [(2**(1/2))/2, -1*((2**(1/2))/2)])])



## Problem 7
# use 'one' instead of '1'
x_gf2 = [one, 0, 0, 0]



## Problem 8
v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

