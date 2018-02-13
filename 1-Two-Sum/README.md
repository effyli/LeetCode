# Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

# Solution
Brute force(didn't pass):

Use two for loops to try to sum every two numbers in the list.
The second loop is from i+1 to the length of the list, so it won't use the same element twice.

Hash table(dictionary): passed, beats 49%, 70ms

Use a dictionary to store value, key. Find if value exist, and then return key. 
Reduce time complexity from O(n^2) to O(n) 