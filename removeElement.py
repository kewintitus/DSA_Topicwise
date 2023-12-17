class Solution(object):
    def removeElement(self, nums, val):
        arr = []
        for i,n in enumerate(nums):
            if n!=val:
                arr.append(n)
        return arr
        
test = Solution()
print(test.removeElement([0,1,2,2,3,0,4,2], 0))