#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
import heapq

class Solution:
    def sortAKSortedDLL(self, head, k):
        if not head or not head.next:
            return head
        
        # Create a min-heap
        heap = []
        
        # Custom comparison function for heap
        def heap_compare(node):
            return node.data
        
        # Add first k+1 elements to the heap
        current = head
        for _ in range(k + 1):
            if current:
                heapq.heappush(heap, (heap_compare(current), id(current), current))
                current = current.next
            else:
                break
        
        # Create a dummy node for the new sorted list
        new_head = DLLNode(0)
        tail = new_head
        
        # Process the rest of the list
        while heap:
            # Extract the minimum element
            _, _, min_node = heapq.heappop(heap)
            
            # Add to the sorted list
            tail.next = min_node
            min_node.prev = tail
            tail = tail.next
            
            # If there are more nodes in the original list, add to heap
            if current:
                heapq.heappush(heap, (heap_compare(current), id(current), current))
                current = current.next
        
        # Set the next of the last node to None
        tail.next = None
        
        # Set the prev of the first node (after dummy) to None
        result = new_head.next
        if result:
            result.prev = None
        
        return result
#{ 
 # Driver Code Starts
import heapq


# A node of the doubly linked list
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to insert a node at the end of the doubly linked list
def push(tail, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail

    if tail is not None:
        tail.next = new_node

    return new_node


# Function to print nodes in a given doubly linked list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Driver code
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int, input().split()))  # Read the input array
        k = int(input())  # Read the value of k

        head = DLLNode(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail = push(tail, arr[i])

        solution = Solution()
        sorted_head = solution.sortAKSortedDLL(head, k)
        printList(sorted_head)

# } Driver Code Ends