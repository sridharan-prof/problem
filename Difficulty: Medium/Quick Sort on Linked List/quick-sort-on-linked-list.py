#User function Template for python3

def quickSort(head):
    #return head after sorting
    if head is None:
        return None

    h, t = mysort(head)
    t.next = None
    return h


def mysort(head):

    if head is None:
        return None, None

    if head and head.next is None:
        return head, head

    left = None
    pleft = None
    right = None
    pright = None

    phead = head

    p = head.next

    while p:
        if p.data < head.data:
            if left is None:
                left = p
                pleft = p
                p = p.next
                pleft.next = None
            else:
                pleft.next = p
                pleft = p
                p = p.next
                pleft.next = None
        elif p.data > head.data:
            if right is None:
                right = p
                pright = p
                p = p.next
                pright.next = None
            else:
                pright.next = p
                pright = p
                p = p.next
                pright.next = None
        elif p.data == head.data:
            phead.next = p
            phead = p
            p = p.next
            phead.next = None

    lhead, ltail = mysort(left)
    rhead, rtail = mysort(right)

    if lhead is None and rhead is None:
        return head, phead
    if lhead is None and rhead is not None:
        phead.next = rhead
        return head, rtail
    elif lhead and rhead is None:
        ltail.next = head
        return lhead, phead
    elif lhead and rhead:
        ltail.next = head
        phead.next = rhead
        return lhead, rtail


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def nodeID(head, dic):
    while head:
        dic[head.data].append(id(head))
        head = head.next


def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # dictonary to keep data and id of node
        nodeID(ll.head, dic)  # putting data and its id

        resHead = quickSort(ll.head)
        printList(resHead, dic)  #verifying and printing
        print()

        print("~")

# } Driver Code Ends