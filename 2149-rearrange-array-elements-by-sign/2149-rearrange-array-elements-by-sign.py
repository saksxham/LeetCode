class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums2=[0] * len(nums)
        positive_idx=0
        negative_idx=1
        for i in nums:
            if i>=0:
                nums2[positive_idx]=i
                positive_idx=positive_idx+2
            else:
                nums2[negative_idx]=i
                negative_idx=negative_idx+2
        return nums2
        