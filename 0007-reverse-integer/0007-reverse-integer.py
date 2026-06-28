import math
class Solution:
    def reverse(self, x: int) -> int:
        sum=0
        y=abs(x)
        while y:
            sum=sum*10+y%10
            y=y//10
            if sum > 2**31 -1 :
                return 0
        
        return sum *  [1, -1][x < 0]
    

        