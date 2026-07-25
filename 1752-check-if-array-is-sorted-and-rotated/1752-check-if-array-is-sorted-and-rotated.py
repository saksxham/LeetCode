class Solution:
    def check(self, nums: List[int]) -> bool:
        #Brute Force approach
        #Check for all the rotation array, if its sorted or not
        #an array of size n if rotated n times, becomes same array
        #so the total possible combination is 0,n-1 rotations
        # l=len(nums)

        # for i in range(l):
        #     new_arr=[]
        #     for j in range(i,l):
        #         new_arr.append(nums[j])
        #     for j in range(i):
        #         new_arr.append(nums[j])
        #     is_sorted=True
        #     for k in range(1,l):
        #         if new_arr[k]<new_arr[k-1]:
        #             is_sorted=False
        #             break
        #     if is_sorted:
        #         return True
        # return False


        #Optimal - Better solution
        #In a sorted array, either rotated or not, there can be atmost 1 invesrion point
        # i.e the point where prev element is more than next element
        #the inversion happens at the min elemt of the array
        #if there are more than 1 inversion points in the array, this means any number of the rotation cant make it a sorted array

        inversion_point=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inversion_point=inversion_point+1
        # also Check for 1st and last
        if nums[0] < nums[len(nums) - 1]:
            inversion_point=inversion_point+1


        if inversion_point>1:
            return False
        else:
            return True


