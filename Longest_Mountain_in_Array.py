class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        # start at the first index because the first and last element can't be peak of the mountain
        for idx in range(1, len(arr) - 1):
            # if this condition is satisfied, the number could be a possible peak of the mountain
            if arr[idx-1] < arr[idx]> arr[idx+1]:
                left = right = idx
                while left> 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right+1]:
                    right += 1
            # calculate the length of the mountain
            # has to be inclusive so add 1   
                result = max(result, (right - left + 1))
        return result
