class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorith
        sum=0
        max=float('-inf')
        for i in nums:
            sum=sum+i
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max
        