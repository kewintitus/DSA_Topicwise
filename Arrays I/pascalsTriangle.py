def generatePascalsTriangle(numRows, r, c):
    res = []
    for i in range(numRows):
        row=[]
        for j in range(i+1):
            
            if j==0 or j==i or i==0:
                row.append(1)
            else:
                row.append(res[i-1][j-1] + res[i-1][j])
            print(i,j)
        res.append(row)
    return res

    


result = generatePascalsTriangle(5,4,4)
print(result)
