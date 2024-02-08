class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

def mergeSort(head):
    if not head or not head.next:
        return head

    middle = getMiddle(head)
    next_to_middle = middle.next
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(next_to_middle)

    sorted_list = sortedMerge(left, right)
    return sorted_list

def getMiddle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sortedMerge(a, b):
    if a is None:
        return b
    elif b is None:
        return a

    if a.value <= b.value:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.value < l2.value:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

# Допоміжна функція для друку списку (для тестування)
def printList(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")
