class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        k_flips = []
        for i in range(l):
            maxi = max(arr[:l-i])
            maxi_idx = arr.index(maxi) + 1
            arr[:maxi_idx] = reversed(arr[:maxi_idx])
            k_flips.append(maxi_idx)
            arr[:l-i] = reversed(arr[:l-i])
            k_flips.append(l-i)
        return k_flips
