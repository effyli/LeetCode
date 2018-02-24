class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #         if not p:return not s

        #         first_match = bool(s) and p[0] in {s[0],'.'}

        #         if(len(p) > 1 and p[1] == '*'):
        #             return(self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p))
        #         else:
        #             return(first_match and self.isMatch(s[1:],p[1:]))
        # init the table
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # init the first corner and first row and column
        dp[0][0] = True
        for i in range(2, len(p) + 1):
            dp[i][0] = p[i - 1] == '*' and dp[i - 2][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] in {s[j - 1], '.'})
                else:
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j]
                    if p[i - 2] in {s[j - 1], '.'}:
                        dp[i][j] |= dp[i][j - 1]

        return dp[-1][-1]


s = 'aa'
p = 'a*'
# print(Solution.isMatch(Solution.isMatch,s,p))
print(Solution.isMatch(Solution.isMatch, s, p))