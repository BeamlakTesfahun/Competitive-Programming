class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spe_pair=  [[pos,spe] for pos,spe in zip(position,speed)]
        stack = []
        
        for pos,spe in sorted(pos_spe_pair)[::-1]: #sort in reverse order
            stack.append((target- pos)/spe)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
