# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Step 1: Base case, if head is None or only one element
        if not head or not head.next:
            return head
        
        # Step 2: Split the list into two halves
        def splitList(head: ListNode) -> ListNode:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None  # Cut the list into two parts
            return mid
        
        # Step 4: Merge two sorted lists
        def mergeList(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            # If one of the lists is exhausted, append the remaining part of the other list
            current.next = l1 if l1 else l2
            return dummy.next
        
        # Step 3: Recursively sort the two halves
        mid = splitList(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the two sorted halves
        return mergeList(left, right)

# Helper functions to create and print linked lists
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# Example usage
if __name__ == "__main__":
    # Creating an example linked list: [4, 2, 1, 3]
    lst = [4, 2, 1, 3]
    head = create_linked_list(lst)
    
    # Printing original list
    print("Original list:")
    print_linked_list(head)
    
    # Sorting the list
    solution = Solution()
    sorted_head = solution.sortList(head)
    
    # Printing sorted list
    print("Sorted list:")
    print_linked_list(sorted_head)
