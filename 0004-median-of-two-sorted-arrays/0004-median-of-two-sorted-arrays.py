class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #use a two pointers method to get the min attribute in each iteration of getmin()
        #for even let say 6, the median is 3,4/2
        #for odd median is let say 5, 3rd elemnt
        p1,p2=0,0
        l1,l2=len(nums1),len(nums2)
        def get_min():
            nonlocal p1,p2
            if p1<l1 and p2<l2:
                if nums1[p1]<nums2[p2]:
                    ans=nums1[p1]
                    p1=p1+1
                else:
                    ans=nums2[p2]
                    p2=p2+1
            elif p1==l1:
                ans=nums2[p2]
                p2=p2+1
            else:
                ans=nums1[p1]
                p1=p1+1
            return ans
#Point to remeber is // operation is taking place befor + , that will throw wrong output
        if (l1+l2)%2==0:
            for i in range(((l1+l2)//2)-1):#for 6, range is range(2),so runs for (0,1) iteration
                j=get_min()
            return (get_min()+get_min())/2#for 3rd and fourth element, its called twice in return
        else:
            for i in range((l1+l2)//2):
                j=get_min()
            return get_min()



#below method aint working in leetcode, as there is memory constraint so we will have to use sort in place
#without creating extra list
        # merged_list=[]
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i]<nums2[j]:
        #         merged_list.append(nums1[i])
        #         i=i+1
        #     else:
        #         merged_list.append(nums2[j])
        #         j=j+1
        # while i < len(nums1):
        #     merged_list.append(nums1[i])
        # while j < len(nums2):
        #     merged_list.append(nums2[j])