class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = n * [0]
        lst = []
        for first,last, seats in bookings:
            lst.append ((first-1, seats))
            lst.append ((last, -seats))
        lst.sort()
        current_num = 0
        prev_i = 0
        for i, seats in lst:
            for j in range(prev_i,i):
                result[j] += current_num
            prev_i = i
            current_num += seats
        return result
            
