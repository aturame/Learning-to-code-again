import numpy as np

#Attempt at Laplace Transforms for NxN Matrices (10/19/2026 01:41)

#okay so basically i need to split row wise recursively
n=10  #Keep it <=10 or it lags hella
mat = np.random.randint(1,n+1,size = (n,n)) #This creates a matrix of array n,n filled with random values!!! super useful for loading matrices

def laplace_transform(mat):
    total_determinant = 0
    if len(mat) ==1:
        return mat[0,0]
    if len(mat)==2:
        return (mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0])
    else:
        for col_index in range(len(mat)):
            col_val = (-1)**col_index #-1**0 (first row) that is 1 which is positive and -1**1-> Negative, lowkey hella elegant solution not gonna lie _> almost like a alternating function
            new_mat = np.delete(mat,col_index, axis=1) #Strip the column first# The axes specify either row or column 0 - row, 1 - column
            new_mat = np.delete(new_mat,0,axis = 0) #Stripping row 0
            subdet = laplace_transform(new_mat) #recursively re run till the return value is a single digit through the 2x2 calculator
            total_determinant += col_val*mat[0,col_index]*subdet #Add all the determinants up together basically plus the sign and the first row value
    return (total_determinant)

print(laplace_transform(mat))

#Compiled 10/19/2026 02:41
