class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            for j in range(i+1,lens):
                if (nums[i] + nums[j] == target):
                    return ([i,j])
                


nums = [3,2,4]
target = 6
print(Solution.twoSum(Solution.twoSum,nums=nums,target=target))