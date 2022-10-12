class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {} # holds character and the last instance of the character
        for idx,char in enumerate(s):
            last_idx[char]= idx
            
        size, end = 0,0 
        result = [] # holds the size of each partition
        for idx, char in enumerate(s):
            # increase size after every character
            size += 1
            """
            if last_idx[char] > end:
                end = last_idx[char]
            """
            end = max(end, last_idx[char])
            if idx == end:
                result.append(size)
                # reset size back to zero
                size = 0
        return result
