class Solution:
    def finNumAppOnce(self, nums:list):
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                del res[nums[i]]
            else:
                res[nums[i]] = i

        print(res)
        return next(iter(res))
    

sol  = Solution()
print(sol.finNumAppOnce([1,1,2,2,3]))