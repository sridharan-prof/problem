#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def __init__(self):
        self.head = None  # Head of the 2D linked list

    # Function to construct a 2D linked list from a matrix
    def constructLinkedMatrix(self, mat):
        if not mat or not mat[0]:
            return None
        
        n = len(mat)
        nodes = [[None for _ in range(n)] for _ in range(n)]
        
        # Step 1: Create all nodes
        for i in range(n):
            for j in range(n):
                nodes[i][j] = Node(mat[i][j])

        # Step 2: Link the nodes (right and down)
        for i in range(n):
            for j in range(n):
                if j < n - 1:
                    nodes[i][j].right = nodes[i][j + 1]  # Link to the right
                if i < n - 1:
                    nodes[i][j].down = nodes[i + 1][j]  # Link down

        # Set the head of the 2D linked list
        self.head = nodes[0][0]

        return self.head

    # Utility function to print the 2D linked list in matrix form
    def print_2D_linked_list(self):
        node = self.head
        while node:
            row = node
            while row:
                print(row.data, end=" ")
                row = row.right
            print()
            node = node.down



#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends