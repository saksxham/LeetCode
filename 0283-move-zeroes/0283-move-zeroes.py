class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        l=len(nums)-1
        while j<=l:
            if nums[i]==0 and nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                i=i+1
                j=j+1
            elif nums[i]==0 and nums[j]==0:
                j=j+1
            elif nums[i]!=0 and nums[j]!=0:
                i=i+1
                j=j+1