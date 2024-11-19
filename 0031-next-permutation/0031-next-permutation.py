class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        index = -1

        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                index = i
                break
        if index == -1:
            arr.reverse()
            return

        for j in range(n-1,index,-1):
            if arr[j] > arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
                break
        arr[index+1:] = reversed(arr[index+1:])
        