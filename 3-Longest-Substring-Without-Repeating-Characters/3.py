class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ''
        buff = ''
        for i in s:
            if (i in buff):
                if(res):
                    res = res if len(res)>len(buff) else buff
                else:
                    res = buff
                # buff = buff.split(i)[1]     # 170ms
                buff = buff[buff.index(i)+len(i):]   # 139ms
            buff += i

        # return res if len(res)>len(buff) else buff
        return max(len(res),len(buff))


        # Hash table solution found on Leetcode
        # used = {}
        # max_length = start = 0
        # for i, c in enumerate(s):
        #     if c in used and start <= used[c]:
        #         start = used[c] + 1
        #     else:
        #         max_length = max(max_length, i - start + 1)
        #
        #     used[c] = i
        #
        # return max_length




s = "sjyzaeahyh"
print(Solution.lengthOfLongestSubstring(Solution.lengthOfLongestSubstring,s))