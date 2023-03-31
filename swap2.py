class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
        self.prev = None
def push(head,x):
    a = Node(x)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = a
    a.prev = curr
    a.next = None    
    return head
def display(head):
    curr = head
    while curr:
        print(curr.key, end="-->")
        curr = curr.next
head = Node(10)
head.prev =None
head.next = Node(20) 
head.next.prev =head
head.next.next = Node(30)
head.next.next.prev = head.next
head=push(head,10)
head=push(head,40)
display(head)