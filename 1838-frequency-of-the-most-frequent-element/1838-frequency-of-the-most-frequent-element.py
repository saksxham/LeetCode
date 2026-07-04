class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        left=0
        curr=0
        print(nums)
        for right in range(len(nums)):
            target=nums[right]
            curr=curr+target
            while (((right-left+1)*target) - curr)>k:
                curr=curr-nums[left]
                left=left+1
            ans = max(ans, right - left + 1)
        return ans
        