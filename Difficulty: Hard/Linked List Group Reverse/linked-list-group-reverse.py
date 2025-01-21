"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        def reverseLinkedList(start,end):
            prev=None
            curr=start
            while curr!=end:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        dum= Node(0)
        dum.next=head
        prev_group_end=dum
        while True:
            count=0
            group_end=prev_group_end
            while count<k and group_end.next:
                group_end=group_end.next
                count+=1
            if count<k:
                prev_group_end.next=reverseLinkedList(prev_group_end.next,None)
                break
            group_start=prev_group_end.next
            next_group_start=group_end.next
            group_end.next=None
            new_group_start=reverseLinkedList(group_start,None)
            prev_group_end.next=new_group_start
            group_start.next=next_group_start
            prev_group_end=group_start
        return dum.next
#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends