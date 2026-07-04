class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=0
        y=x
        if x<0:
            return False
        else:
            while x:
                t=t*10+x%10
                x=x//10
                print(t, x)
            if t==y:
                return True
            else:
                return False
        