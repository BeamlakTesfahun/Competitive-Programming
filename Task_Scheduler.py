class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            d[i] = d.get(i,0) + 1
        # a list that contains the frequency of each task
        d = [value for key,value in d.items()]
        max_d = max(d)
        # how many tasks have the same freq as the highest freq
        num_max_freq = d.count(max_d)
        # formula alone may not work so return the max out of len of tasks and the formula
        # if input = [AAABBB] and n = 0 the formula alone doesn't work
        return (max(len(tasks),(max_d - 1) * (n + 1) + num_max_freq))
        
