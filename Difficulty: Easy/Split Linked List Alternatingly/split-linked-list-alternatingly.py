#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        if not head:
            return [None, None]

        # Initialize two pointers for the two new lists
        head1, head2 = None, None
        temp1, temp2 = None, None
        
        # Boolean flag to alternate between the two lists
        is_even = True
        current = head

        while current:
            if is_even:
                # Add to the first list
                if head1 is None:
                    head1 = current
                    temp1 = head1
                else:
                    temp1.next = current
                    temp1 = temp1.next
            else:
                # Add to the second list
                if head2 is None:
                    head2 = current
                    temp2 = head2
                else:
                    temp2.next = current
                    temp2 = temp2.next
            
            # Move to the next node and flip the flag
            current = current.next
            is_even = not is_even
        
        # Terminate the two new lists to avoid cycles
        if temp1:
            temp1.next = None
        if temp2:
            temp2.next = None
        
        # Return the two lists as an array
        return [head1, head2]
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends