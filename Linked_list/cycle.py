class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Traverse the linked list
        while fast and fast.next:
            slow = slow.next  # Move slow pointer by 1 step
            fast = fast.next.next  # Move fast pointer by 2 steps

            # If slow and fast pointers meet, there is a cycle
            if slow == fast:
                return True

        # If fast pointer reaches the end, there is no cycle
        return False

# Example usage:

# Helper function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to create a cycle in the linked list
def createCycle(head, pos):
    if pos == -1 or not head:
        return head
    cycle_node = None
    current = head
    index = 0
    tail = None

    while current:
        if index == pos:
            cycle_node = current
        tail = current
        current = current.next
        index += 1

    if tail:
        tail.next = cycle_node  # Creating the cycle
    return head

# Example 1:
head_with_cycle = createLinkedList([3, 2, 0, -4])
createCycle(head_with_cycle, 1)  # Cycle at node with value 2
solution = Solution()
print(solution.hasCycle(head_with_cycle))

# Example 2:
head_without_cycle = createLinkedList([1, 2])
print(solution.hasCycle(head_without_cycle))

# Example 3:
single_node = createLinkedList([1])
print(solution.hasCycle(single_node))
