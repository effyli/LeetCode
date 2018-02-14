class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        start = 0
        end = 0
        for c,i in enumerate(s):
            j = c + 1
            k = c - 1
            while(j<lens and k>=0 and s[j] == s[k]):
                if(j-k+1 > maxlength):
                    start = k
                    end = j
                k-=1
                j+=1
            maxlength = end+1-start

        for c,i in enumerate(s):
            j = c + 1
            k = c
            while(j<lens and k >= 0 and s[j] == s[k]):
                if(j-k+1 > maxlength):
                    start = k
                    end = j
                k-=1
                j+=1
            maxlength = end+1-start

        return s[start:end+1]




s = "baabjiadcicda"
print(Solution.longestPalindrome(Solution.longestPalindrome,s))