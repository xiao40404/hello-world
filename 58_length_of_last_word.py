class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        m = -1
        for i in range(1,len(s)+1):
            if s[0-i] != ' ':
                m = i
                break
        if m == -1:
            return 0
        
        for j in range(m,len(s)+1):
            if not ' ' in s[:-m]:
                return len(s)-m+1
            elif s[0-j] == ' ':
                return j-m
