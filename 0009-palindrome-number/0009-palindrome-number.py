class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            sum=0
            y=x
            while x>0:
                sum=sum*10+x%10
                x=x//10
            print(sum)
            if sum==y:
                return True
            else:
                return False
        