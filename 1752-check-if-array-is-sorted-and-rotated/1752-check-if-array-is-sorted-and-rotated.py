class Solution:
    def check(self, nums: List[int]) -> bool:
        #Brute Force approach
        #Check for all the rotation array, if its sorted or not
        #an array of size n if rotated n times, becomes same array
        #so the total possible combination is 0,n-1 rotations
        l=len(nums)

        for i in range(l):
            new_arr=[]
            for j in range(i,l):
                new_arr.append(nums[j])
            for j in range(i):
                new_arr.append(nums[j])
            is_sorted=True
            for k in range(1,l):
                if new_arr[k]<new_arr[k-1]:
                    is_sorted=False
                    break
            if is_sorted:
                return True
        return False
