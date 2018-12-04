class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a,b = len(haystack),len(needle)
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(a-b+1):
                if haystack[i] != needle[0]:
                    continue
                elif haystack[i:i+b] == needle:
                    return i
