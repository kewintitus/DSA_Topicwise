# brute force
def setMatrixZero(matrix:list):
    
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==0):
                matrix = checkRowCols(i,j,matrix)

    print(setValueZero(matrix))

def setValueZero(matrix:list):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==-1: matrix[i][j]=0
    return matrix


def checkRowCols(i,j,matrix):
    for i1 in range(len(matrix)):
        if matrix[i1][j] != 0:
            matrix[i1][j]=-1
    
    for j1 in range(len(matrix[0])):
        if matrix[i][j1] !=0:
            matrix[i][j1] = -1

    return matrix
    
    
setMatrixZero([[1,1,1],[1,0,1],[1,1,1]])