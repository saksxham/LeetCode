class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #Optimal Solution not best
        new_arr=[]
        l=len(nums)
        #mod of k is taken as array roated its len number of time is exactly same
        k=k%l
        for i in range(l-1-k+1,l):
            new_arr.append(nums[i])
        for i in range(l-1-k+1):
            new_arr.append(nums[i])
        for i in range(l):
            nums[i]=new_arr[i]

        