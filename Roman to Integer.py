class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = []
        for ss in s:
            if ss == 'I':
                x.append(1)
            if ss == 'V':
                x.append(5)
            if ss == 'X':
                x.append(10)
            if ss == 'L':
                x.append(50)
            if ss == 'C':
                x.append(100)
            if ss == 'D':
                x.append(500)
            if ss == 'M':
                x.append(1000)
            
            a = 0
            for i in range(len(x)-1):
                if x[i]<x[i+1]:
                    a = a-x[i]
                else:
                    a = a+x[i]
        return a+x[-1]
