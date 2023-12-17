class Solution(object):
    def sortArray(self, arr:list, startIndex:int):
        for i in range(startIndex, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]>arr[j]:
                    arr[i], arr[j] = arr[j],arr[i]
        return arr
    
    
    def nextPermutation(self, nums:list):
        largest = nums[1]
        secondLargest = -1
        index = nums[0]
        
        sortArr = self.sortArray(nums, 1)
        # for i in range(1, len(nums)):
        #     if sortArr[i]>sortArr[0]:
        #         sortArr[i], sortArr[0] = sortArr[0], sortArr[i]
        #         break
        
        print(sortArr)
        # for i in range(1, len(nums)):

            # print(nums[i])
            # if nums[i]>index:
            #     if nums[i]>largest:
            #         secondLargest = largest
            #         largest = nums[i]
            #     elif (nums[i]<largest and nums[i]>index and nums[i]>secondLargest):
            #         secondLargest = nums[i]
            #     largest = nums[i]
            #     # index = largest
        # print(secondLargest)


abc=  Solution()
abc.nextPermutation([3,5,4,6])

