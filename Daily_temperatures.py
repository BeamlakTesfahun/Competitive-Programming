class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # [temperature, index] pair
    # enumerate returns index, value pair
        for idx, temp in enumerate(temperatures):
    # while stack is not empty and the last element of stack is less than the current value
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = (idx - stackIdx)
            stack.append([temp,  idx])
    # the default value is already zero so no need to fill in zero
        return result
