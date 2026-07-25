class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new_arr=[]
        l=len(nums)
        k=k%l
        for i in range(l-1-k+1,l):
            new_arr.append(nums[i])
        for i in range(l-1-k+1):
            new_arr.append(nums[i])
        for i in range(l):
            nums[i]=new_arr[i]

        