class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        len_ = len(arr)
        # n + 1 size prefix
        prefix_sum = [0 for x in range(len_ + 1)]
        for i in range(len_):
            prefix_sum[i+1] = prefix_sum[i] ^ arr[i]
        result = []
        for left,right in queries:
            result.append(prefix_sum[right+1] ^ prefix_sum[left])
        return result
