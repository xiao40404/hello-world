class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        r=0
        if self.x > 0 & self.x < 2**31:
            while self.x > 0:
                y = self.x//10
                z = self.x%10
                self.x = y
                r = r*10+z
            if r<2**31:
                return(r)
            else:
                return 0

        elif self.x < 0 & self.x >= -2**31:
            self.x = -self.x
            while self.x > 0:
                y = self.x//10
                z = self.x%10
                self.x = y
                r = r*10+z
            if -r>-2**31:
                return(-r)
            else:
                return 0
        else:
            return 0
