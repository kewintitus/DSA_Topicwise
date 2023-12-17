class Solution:
    def generateUnion(self, array1:list, array2:list):
        res = {}
        for i in range(len(array1)):
            if array1[i] in res:
                res[array1[i]]+=1
            else:
                res[array1[i]] = 1

        for i in range(len(array2)):
            if array2[i] in res:
                res[array2[i]]+=1
            else:
                res[array2[i]] = 1

        return res.keys()
    
sol = Solution()
print(sol.generateUnion([1,2,3,4,5],[2,3,4,4,5]))