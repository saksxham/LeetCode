class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl=0
        left=0
#Using a Two-pointers Sliding window technique
#sl:substring lenght(maintain max)
#left:left pointer(remove all elemnts from left till the right most elemt hit by right is removed from string)
#right: traverse the string

        for right in range(len(s)):
            while s[right] in s[left:right]:
                left=left+1
            sl=max(sl,right-left+1)
        return sl

        