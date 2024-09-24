# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to add two numbers represented as linked lists
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # Dummy node to simplify result list creation
    current = dummy  # Pointer to the current node in the result list
    carry = 0  # Initialize carry to 0

    # Traverse both linked lists
    while l1 or l2 or carry:
        # Get the values of the current nodes or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum of the current digits and the carry
        total = val1 + val2 + carry
        carry = total // 10  # Update carry (either 0 or 1)
        current.next = ListNode(total % 10)  # Create a new node for the result

        # Move to the next nodes
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next  # The actual result starts from dummy.next

# Helper function to create a linked list from a list of numbers
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to print linked list values
def printLinkedList(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Example usage:
if __name__ == "__main__":
    # Create two linked lists
    l1 = createLinkedList([2, 4, 3])  # Represents the number 342
    l2 = createLinkedList([5, 6, 4])  # Represents the number 465

    # Add the two numbers
    result = addTwoNumbers(l1, l2)

    # Print the result
    print("Resultant Linked List:")
    printLinkedList(result)
