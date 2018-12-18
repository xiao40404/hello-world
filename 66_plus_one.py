class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits)-1
        while i >= 0:
            if digits[i]+1 < 10:
                digits[i] = digits[i]+1
                break
            else:
                digits[i] = 0
                if i >= 1:
                    i = i-1
                else:
                    digits.insert(0,1)
                    i = i-1
        return digits
