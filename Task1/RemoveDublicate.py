class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        temp = head
        temp2 = head.next
        last = head.val
        
        while temp2: 
            if temp2.val == last:  
                if not temp2.next: 
                    temp.next = None
                    break
                temp2 = temp2.next  
                temp.next = temp2  
            else:  
                temp = temp2
                last = temp.val
                temp2 = temp2.next
        
        return head  