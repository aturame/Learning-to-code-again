#Attempting L-U Factorisation for Finding the determinant of a NxN matrix
#10/19/2026 12:03

import numpy as np

n=4
A = np.random.randint(0,100, size = (n,n))
U = A

def identity_mat(n):
    L = np.zeros((n,n),dtype=int)
    for row_index in range(L.shape[0]):
        for column_index in range(L.shape[1]): 
            if column_index==row_index:
                L[row_index,column_index] = 1
            if column_index!=row_index:
                L[row_index,column_index] = 0
    print(L)
    return(L)
L = identity_mat(n)



def LUfactor(n,A,U,L):
    for iter in range(U.shape[0]):
        pivot_element = U[iter,0]
        for row_index in range(U.shape[1]):
            if pivot_element != 0:
                target_element = U[row_index,iter+1]
                factor = target_element/pivot_element
                U[row_index] = U[row_index] - U[0,iter]*factor
                L[row_index,0] = factor
    print(L)
    print(U)
#im exhausted will figure it out tmr 10/19/2026 23:52
