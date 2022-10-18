class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        sums = 0
        for i in range(k):
            sums += arr[i]
        c = threshold * k
        # if sums is greater than c it intializes result with 1 otherwise with 0
        result = int(sums >= c)
        for start in range(k,len(arr)):
            sums += arr[start]
            sums -= arr[start - k]
            if sums >= c:
                result += 1
        return result
