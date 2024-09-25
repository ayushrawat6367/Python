class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to reverse the sublist between left and right positions
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    # Step 1: Create dummy node and set `prev` to dummy
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Step 2: Move `prev` to the node just before the `left`-th node
    for _ in range(left - 1):
        prev = prev.next

    # Step 3: Set `start` to the `left`-th node and `then` to the node after `start`
    start = prev.next
    then = start.next

    # Step 4: Reverse nodes from left to right
    for _ in range(right - left):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return dummy.next

# Helper function to print the linked list
def printLinkedList(head: ListNode):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
if __name__ == "__main__":
    # Create a linked list [1, 2, 3, 4, 5]
    head = createLinkedList([1, 2, 3, 4, 5])
    print("Original List:")
    printLinkedList(head)

    # Reverse the sublist from position 2 to 4
    left, right = 2, 4
    new_head = reverseBetween(head, left, right)

    # Output the modified list
    print(f"\nList after reversing between positions {left} and {right}:")
    printLinkedList(new_head)
