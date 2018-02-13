# Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Solution

1. Sliding window, store the first unique substring to buff, then compare the following substring, take the longer one as result.
2. Hash table solution, found on Leetcode. Use dictionary as hash table. Store the characters in used dict, if found the same char, update the index.