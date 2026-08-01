class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Dutch National Flag Algorithm
        #0-Low-1==All 0's
        #low-mid-1==All 1's
        #mid-high==All unsorted
        #high-n==All 2's
        mid=0
        low=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid]=nums[low]
                nums[low]=0
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            elif nums[mid]==2:
                nums[mid]=nums[high]
                nums[high]=2
                high=high-1


