# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummynode=ListNode(0)
        curr=dummynode
        sum=0
        while l1 != None or l2 != None or carry!=0:
                l1val=l1.val if l1 else 0
                l2val=l2.val if l2 else 0
                sum=l1val+l2val+carry
                carry=sum//10
                newNode=ListNode(sum%10)
                curr.next=newNode
                carry=sum//10
                if l1:
                    l1=l1.next
                else:
                    l1=None
                if l2:
                    l2=l2.next
                else:
                    l2=None
                curr=curr.next
        return dummynode.next