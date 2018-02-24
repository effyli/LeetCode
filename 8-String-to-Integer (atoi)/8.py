class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        obj = ['0','1','2','3','4','5','6','7','8','9']
        symbol = ['+','-']
        res = ''
        buff = ''
        j = ''
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        for i in str:
            if i in obj:
                if j in obj or j in symbol or j == ' ' or j == '':
                    res += i
                else:
                    res = ''
                    break
            elif i in symbol:
                buff += i
            else:
                if(res!='' or buff!=''):
                    break
            j = i
        while(res and len(buff) <= 1):
            if(buff):
                if buff == '+':
                    num = int(res)
                if buff == '-':
                    num = -int(res)
            else:
                num = int(res)
            if num > INT_MAX:
                return INT_MAX
            elif num < INT_MIN:
                return INT_MIN
            else:
                return num
        return 0




s = "   123"
print(Solution.myAtoi(Solution.myAtoi,s))