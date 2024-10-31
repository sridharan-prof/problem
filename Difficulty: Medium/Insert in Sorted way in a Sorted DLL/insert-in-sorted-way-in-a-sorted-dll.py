#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        new_node = Node(x)
        
        # Case 1: Empty list
        if head is None:
            return new_node
            
        # Case 2: Insert at beginning
        if x <= head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
            
        # Case 3: Insert in middle or end
        current = head
        while current.next and current.next.data < x:
            current = current.next
            
        # Insert after current node
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:  # If not inserting at the end
            current.next.prev = new_node
        current.next = new_node
        
        return head



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends