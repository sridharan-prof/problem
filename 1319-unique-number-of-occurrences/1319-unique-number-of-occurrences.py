class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        lst = []
        for key, value in count.items():
            if value not in lst:
                lst.append(value)
            else:
                return False
        return True

        