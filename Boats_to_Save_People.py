class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1
        # cant cross eachother but can be equal to eachother
        while left <= right:
            # subtract heaviest weight from the limit
            remaining = limit - people[right]
            right -= 1
            count += 1
            # edge case: what if the last and the right number are equal to eachother
            if left <= right and remaining >= people[left]:
                left += 1
        return count
