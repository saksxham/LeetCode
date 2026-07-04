import math
class Solution:
    def reverse(self, x: int) -> int:
        s=0
        if x<0:
            sign=-1
        else:
            sign=1
        y=abs(x)
        while y:
            s=s*10+y%10
            y=y//10
            if s>2**31:
                return 0
        
        return s * sign

        