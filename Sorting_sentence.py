class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitted = s.split(" ")
        final_sen = ""
        
        for i in range(0,len(splitted)):
            cur_min_idx = i
            for j in range(i+1,len(splitted)):
                if splitted[j][-1] < splitted[cur_min_idx][-1]:
                    cur_min_idx = j
            if i != cur_min_idx:
                splitted[cur_min_idx], splitted[i] = splitted[i], splitted[cur_min_idx]
            final_sen += splitted[i][:-1] + ' '
        return (final_sen[:-1])

