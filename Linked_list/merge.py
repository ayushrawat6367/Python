# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Base cases: if one of the lists is empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Compare the values of the two lists
        if list1.val <= list2.val:
            # If list1's value is smaller, link it to the merged result
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # If list2's value is smaller, link it to the merged result
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
if __name__ == "__main__":
    # Create two sorted linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    
    # Merge the two linked lists
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # Print the merged linked list
    print_linked_list(merged_list)
