
import heapq

class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = [] 

    def addNum(self, num: int):
        
        heapq.heappush(self.max_heap, -num)

        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0] 
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0 

    def getMedian(self, arr):
        medians = []
        for num in arr:
            self.addNum(num)
            medians.append(self.findMedian())
        return medians



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends