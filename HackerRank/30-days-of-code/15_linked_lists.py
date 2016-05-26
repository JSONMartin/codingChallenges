def insert(self,head,data):
    next = head
    if head == None:
        head = Node(data)
    else:
        while next.next != None:
            next = next.next
        next.next = Node(data)
    return head
