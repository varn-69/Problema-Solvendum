# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Edge cases
        if not lists or len(lists) == 0:
            return None
        
        # Dividing and merging each block of list as per comparison
        while len(lists) > 1:
            mergedL = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedL.append(self.mergeL(l1, l2))
            lists = mergedL
        
        return lists[0]
    
    
    # Merging func. for 2 lists
    def mergeL(self, l1, l2):
        head = ListNode()
        tail = head


        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return head.next
'''
In this code , i performed the simple procedure of divide and conquer in which the 
the list of lists is iterated through a while loop until it throws out the each element
in it and thus every two were compared and a merged in list using the mergeL func.

It is an easy bite if merge sort is implemented.

Time comp - O(nlog(k))
Space comp - O(1) '''