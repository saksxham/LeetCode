class Solution:
    def longestPalindrome(self, s: str) -> str:
        #this approach uses Dynamic programmimg
        #we are storing result of smaller set of values already calculated so that its not required to be calculated again
        n=len(s)
        dp=[[False]* n for i in range(n)]#initialized a n*n matrix with false values#stores all the substring sizes possible
        ans=[0,0]
        for i in range(n):#string sizes of only 1 character will always be the palindrome, so initialized as true, this becomes the first base case 
            dp[i][i]=True
        for i in range(n-1):#this becomes the 2nd base case, checking if charcter substring is palindrome or  not
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                ans=[i,i+1]

        for diff in range(2,n):#Because we already checked 1-letter words (diff = 0) and 2-letter words (diff = 1) earlier in the code, this loop starts at diff = 2
            for i in range(n-diff):
                j=i+diff#J is the index of elemnt at last of diff
                if s[i]==s[j] and dp[i+1][j-1]:#if new elemt is matching , does previously inner string is substring or not
                    dp[i][j]=True
                    ans=[i,j]
        i,j=ans
        return s[i:j+1]



#below is the brute force recursive approach, not all test cases can pass due to time exceeding issues
        # def check_palindrome(i: int, t: str) -> bool:
        #     if t == "":
        #         return True
        #     # Minor optimization: >= prevents an extra unnecessary recursive call
        #     if i >= len(t) // 2: 
        #         return True

        #     if t[i] != t[len(t) - 1 - i]:
        #         return False
            
        #     return check_palindrome(i + 1, t)
        
        # res = 0
        # palindrome = ""
        
        # for i in range(len(s)):
        #     # FIX: Start at i + 1 so we don't evaluate empty strings (s[i:i])
        #     for j in range(i + 1, len(s) + 1): 
        #         bul_check = check_palindrome(0, s[i:j])
                
        #         if bul_check:
        #             # FIX: The length of slice s[i:j] is simply j - i
        #             if j - i > res: 
        #                 res = j - i
        #                 palindrome = s[i:j]
                        
        # return palindrome