class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#Another method we can use is hashing
#store elemnts in hash #dictionary in the python
#iterate through hash , if target-hash present then return the index
#hash[key,val]#Key:Value in the array num #val:Index of that value in array num
        hash=dict()
        for i in range(len(nums)):
            hash[nums[i]]=i
        print(hash)

        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hash and hash[complement] != i:
                return [i,hash[complement]]
        return []
        
#Brute force method
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

    

    
        