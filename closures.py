# This will use pure Python instead of SageMath
# because of this, we have to use nested lists instead of matrices
#
# Sample Matrix:
# A = [[1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]

# You can address the i,j entry in the matrix by: 
# A[i][j] 

# You can get the number of rows by:
# len(A)

# We need to make a *deepcopy* of the matrix to avoid modifying the original
# so leave those copy.deepcopy() calls alone
import copy

A = [[1, 0, 1, 0], 
     [0, 0, 1, 1],
     [0, 1, 1, 0], 
     [1, 0, 0, 0]]

def warshall(M):
    R = copy.deepcopy(M)
    
    # TODO Implement this
    return R

def reflexive_closure(M):
    R = copy.deepcopy(M)

    # TODO Implement this
    return R

def symmetric_closure(M):
    R = copy.deepcopy(M)

    # TODO Implement this
    return R

# Print the matrices nicely laid out
def pretty_print(M):
    for row in M:
        print(row)
    print() # newline

# Test ouput
pretty_print(warshall(A))
pretty_print(reflexive_closure(A))
pretty_print(symmetric_closure(A))