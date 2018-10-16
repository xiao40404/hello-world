class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {']':'[',')':'(','}':'{'}
        for a in s:
            if a in dic.values():
                stack.append(a)
            elif a in dic.keys():
                if stack == [] or stack.pop() != dic[a]:
                    return False
            else:
                return False
        return not stack
