class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        #?
        modulo = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        n = len(keys)
        result = 0
        for i,num1 in enumerate(keys):
            j,k = i, n-1
            t = target - num1
            while j<= k:
                num2, num3 = keys[j], keys[k]
                if num2 + num3 < t:
                    j+=1
                elif num2 + num3 > t:
                    k-=1
                # if num1 + num2 is equal to target - 1
                else:
                    if i<j<k:
                        result += count[num1] * count[num2] * count[num3]
                    elif i==j<k:
                        result += count[num1] * (count[num2]-1)/2 * count[num3]
                    elif i<j==k:
                        result += count[num1] * count[num2] * (count[num3]-1)/2
                    # if i==j==k
                    else:
                        result += count[num1] * (count[num2]-1) * (count[num3]-2)/6
                    j+=1
                    k-=1
        return int(result%modulo)
