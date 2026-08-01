class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #moore's voting algorithm      
        count=1
        element=nums[0]
        for i in range(1,len(nums)):
            if element==nums[i] and count>0:
                count=count+1
            elif element!=nums[i] and count>0:
                count=count-1
            elif element!=nums[i] and count==0:
                element=nums[i]
                count=1
            elif element==nums[i] and count==0:
                element=nums[i]
                count=1
        return element
        