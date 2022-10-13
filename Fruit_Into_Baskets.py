class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0 
        max_len = 0
        dic = {}
        while end < len(fruits):
            # the number and the last instance of the number is stored in the dictionary
            dic[fruits[end]] = end
            if len(dic) >= 3:
                min_value = min(dic.values())
                del dic[fruits[min_value]]
                start = min_value + 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
