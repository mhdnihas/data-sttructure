class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverse(head):
    current=head
    while current:
        print(f"Data:  {current.data}    Address: {current.next}")
        current=current.next

def delete_begining(head):
    current=head
    head=current.next
    return head
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
traverse(head)
head=delete_begining(head)
print("after delete first node:")
traverse(head)