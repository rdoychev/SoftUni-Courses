 # 1. Define the structural node class
class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next


# 2. Helper function to print it out cleanly so you can see it
def print_linked_list(head):
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    print(" -> ".join(nodes) if nodes else "Empty List")


# 3. Helper function to turn a standard Python list into a Linked List
def build_linked_list(arr: list):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
print(l1)

print_linked_list(l1)
print_linked_list(l2)