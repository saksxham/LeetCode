class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for j in s:
            if j.isalnum():
                t=t+j.lower()
# this is a recursive solution 
        def palindrome(i: int,k: str):
            if i>=len(k)//2:
                return True
            if k[i]!=k[len(k)-1-i]:
                return False
            else:
                return palindrome(i+1,k)
        return palindrome(0,t)
       # print(t)
# #This is a brute force method        
#         for i in range(len(t)//2):
#             if t[i]!=t[len(t)-1-i]:
#                 return False
#         return True

#     #
        

      
