class Solution:
            # Function to find the majority element in an array
    def majorityElement(self, nums: List[int]) -> int:
        
        # Size of the given array
        n = len(nums)
        
        # Count
        cnt = 0
        
        # Element
        el = 0
        
        # Applying the algorithm
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        
        """ Checking if the stored element
        is the majority element"""
        cnt1 = nums.count(el)
        
        # Return element if it is a majority element
        if cnt1 > (n // 2):
            return el
        
        # Return -1 if no such element found
        return -1
        # #moore's voting algorithm      
        # count=1
        # element=nums[0]
        # for i in range(1,len(nums)):
        #     if element==nums[i] and count>0:
        #         count=count+1
        #     elif element!=nums[i] and count>0:
        #         count=count-1
        #     elif element!=nums[i] and count==0:
        #         element=nums[i]
        #         count=1
        #     elif element==nums[i] and count==0:
        #         element=nums[i]
        #         count=1
        # return element
        