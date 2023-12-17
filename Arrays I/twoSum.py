class Solution: 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target: return [nums[i],nums[j]]
        return [-1,-1]

sol = Solution()
print(sol.twoSum([1,2,3,4], 7))