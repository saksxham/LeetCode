class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for i in s:
            if i.isalnum():
                t=t+i.lower()
       # print(t)
#This is a brute force method        
        for i in range(len(t)//2):
            if t[i]!=t[len(t)-1-i]:
                return False
        return True
