class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for a in s:
            if a in ['(','[','{']:
                stack.append(a)
            elif stack == []:
                return False
            elif stack != []:
                if a == ')' and stack.pop() != '(':
                    return False
                elif a == ']' and stack.pop() != '[':
                    return False
                elif a == '}' and stack.pop() != '{':
                    return False
            else:
                return False
        return stack == []
