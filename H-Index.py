class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Quick Sort
        citations = [-i for i in citations]
        citations = self.quick_sort(citations, 0, len(citations) - 1)
        citations= [-i for i in citations]
        for idx,citation in enumerate(citations):
            if idx >= citation:
                return idx
        return len(citations)
    def quick_sort(self, arr, left, right):
        if left < right:
            partition_pos = self.partition(arr,left,right)
            self.quick_sort(arr,left, partition_pos - 1)
            self.quick_sort(arr, partition_pos + 1, right)
        return arr
    def partition(self, arr, left, right):
        i = left 
        j = right - 1
        pivot = arr[right]
        while i < j:
            while i < right and arr[i] < pivot:
                i += 1
            while j > left and arr[j] >= pivot:
                j -= 1
            if i < j:
                # swap elements
                arr [i], arr[j] = arr[j], arr[i]
        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]
        return i
