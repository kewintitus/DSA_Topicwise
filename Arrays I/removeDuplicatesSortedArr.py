
class Solution:
    def removeDuplicates(self, nums):
            ref = {}
            i = len(nums)-1
            while i>=0:
                if nums[i] in ref: 
                    nums.pop(i)
                else:
                    ref[nums[i]] = i
                i -=1
            return nums
    
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))