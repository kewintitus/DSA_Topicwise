class Solution:
    def __init__(self, nums:list) -> None:
        self.nums = nums

    def sumNums(self):
        numsum = 0
        for val in self.nums:
            numsum+=val
        return numsum

    def findMissingNo(self):
        length = max(self.nums)
        ad = length*(length+1)/2
        sumNums = self.sumNums()
        diff = ad - sumNums
        print(sumNums, ad)
        if diff == 0:
            return -1
        else:
            return f'missing no {int(diff)}' 
        

sol = Solution([1,2,3,4,6])
print(sol.findMissingNo())