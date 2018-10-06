class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        D = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        a = 0
        for i in range(len(s)-1):
            if D[s[i]]<D[s[i+1]]:
                a = a-D[s[i]]
            else:
                a = a+D[s[i]]
        return a+D[s[-1]]
