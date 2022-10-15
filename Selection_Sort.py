class Solution:
    def selection_sort(self, arr, n):
        for i in range(0, len(arr)-1):
            current_min = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[current_min]:
                    current_min = j
            arr[i], arr[current_min] = arr[current_min],arr[i]
        return arr
    
    
n = int(input())
arr = list(map(int, input().split()))
a = Solution()
print(a.selection_sort(arr, n))
