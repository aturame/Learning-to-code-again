#Attempting L-U Factorisation for Finding the determinant of a NxN matrix (Done)
#10/19/2026 12:03

import numpy as np

n=100 #Set your n lel
A = np.random.randint(0,100, size = (n,n)).astype(float) #Set astype.float or it will fuck around in the factor division
U = A.astype(float)
def identity_mat(n):
    L = np.zeros((n,n),dtype=int).astype(float)
    for row_index in range(L.shape[0]):
        for column_index in range(L.shape[1]): 
            if column_index==row_index:
                L[row_index,column_index] = 1
            if column_index!=row_index:
                L[row_index,column_index] = 0
    return(L)
L = identity_mat(n)


def LUFactor(L,U,A,n):
    determinant = 1 #Set to one or it will multiply by 0
    for column_index in range(U.shape[1]):  #first column iteration
        pivot_element = U[column_index,column_index]
        for row_index in range(column_index+1,U.shape[0]):
            target_element = U[row_index,column_index]
            factor = target_element/pivot_element
            U[row_index] = U[row_index] - factor*U[column_index] #Target - factor x pivot
            L[row_index,column_index] = factor #Add the factor to the ID matrix
    for i in range(U.shape[0]):
        determinant *= U[i,i]
    print (np.allclose(L@U,A)) #Check if it comes out to the original when you multiply them, Det(L)xDet(U) = Det(A), use np.allclose and @ means matrix multiplication
    print(L)
    print(U)
    print(determinant)

LUFactor(L,U,A,n)
 
#Compiled 10/20/2026 15:07
    
