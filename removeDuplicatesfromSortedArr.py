class Solution(object):
    def removeDuplicates(self, nums:list):
        ref = {}
        i = len(nums)-1
        while i>=0:
            if nums[i] in ref: 
                nums.pop(i)
            else:
                ref[nums[i]] = i
            i -=1
        return nums
        # for i in range(len(nums)):
        #     if nums[i] in ref:
        #         nums.pop(i)
        #     ref[nums[i]] = i
        #     print(nums[i])
        # return nums
    

sl = Solution()
print(sl.removeDuplicates([1,1,2,2,3,3]))
