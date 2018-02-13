class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # beats 49%, 70ms
        # using hash table(dictionary) to reduce the time complexity
        # notes:
        #   1. fastest way to create a empty dict:
        #        s = set(range(lens))
        #        dict.fromkeys(s)
        #   2. check if key or value is in dict:
        #        key in dict.keys()
        #        value in dict.values()

        lens = len(nums)
        nums_dict = {}
        s = set(range(lens))
        nums_dict.fromkeys(s)
        for i in range(lens):
            nums_dict[nums[i]] = i
        for j in range(lens):
            tar = target - nums[j]
            if (tar in nums_dict.keys() and nums_dict[tar] != j):
                return [j, nums_dict[tar]]



                # brute force : time limit issue
                # lens = len(nums)
                # for i in range(lens):
                #     for j in range(i+1,lens):
                #         if (nums[j] == target - nums[i]):
                #             return [i,j]
                


nums = [3,2,4]
target = 6
print(Solution.twoSum(Solution.twoSum,nums=nums,target=target))