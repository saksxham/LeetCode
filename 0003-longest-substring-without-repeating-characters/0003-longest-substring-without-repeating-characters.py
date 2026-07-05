class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t=''
        sl=0
        left=0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left=left+1
            sl=max(sl,right-left+1)
        return sl

        