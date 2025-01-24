#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            if slow == fast:          # Loop detected
                return True
        
        return False                  # No loop detected
    
    # Utility function to create a linked list with a loop
    def create_linked_list_with_loop(arr, pos):
        if not arr:
            return None
    
        head = ListNode(arr[0])
        current = head
        loop_node = None
    
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
            
            if i + 1 == pos:          # Save the loop node based on the 1-based index
                loop_node = current
    
        if pos != 0:
            current.next = loop_node # Create a loop by pointing to the loop node
    
        return head

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    #connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))
        res = Solution().detectLoop(LL.head)
        if (res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends