class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=len(nums)
        k=k%l
        self.reverse(0,l-k-1,nums)
        self.reverse(l-k,l-1,nums)
        self.reverse(0,l-1,nums)
    def reverse(self,i,j,nums):
        while i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i=i+1
            j=j-1
# K=3

# l=len(nums)

# reverse(0,l-k,nums)
# reverse(l-k,l-1,nums)
# reverse(0,l-1,nums)

# [1,2,3,4-5,6,7]

# 4,3,2,1-7,6,5
# 5,6,7-1,2,3,4


[5,6,7,1,2,3,4]

        # #Optimal Solution not best
        # new_arr=[]
        # l=len(nums)
        # #mod of k is taken as array roated its len number of time is exactly same
        # k=k%l
        # for i in range(l-1-k+1,l):
        #     new_arr.append(nums[i])
        # for i in range(l-1-k+1):
        #     new_arr.append(nums[i])
        # for i in range(l):
        #     nums[i]=new_arr[i]

        