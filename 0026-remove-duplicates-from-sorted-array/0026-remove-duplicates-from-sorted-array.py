class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #below is the optimal approach
        #using 2 pointers
        left=0
        for right in range(1,len(nums)):
            if nums[right]!=nums[left]:
                left=left+1
                nums[left]=nums[right]
        return left+1        