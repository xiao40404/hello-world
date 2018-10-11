class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        else:
            shortest = min(strs, key=len)
        for i in range(len(shortest)):
                for s in strs:
                    if s[i] != shortest[i]:
                        return shortest[:i]
