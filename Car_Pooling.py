class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = [] # to add the number of people that are gonna get on and get off at a certain stop 
        for people, start, stop in trips:
            lst.append((start,people)) # at the start more people are entering and the capacity decreases
            lst.append((stop, -people)) # getting off the car so less people (negative)
        lst.sort()
        for s_e, people in lst:
 # if people are added capacity decreases, if people are getting off capacity increase (capacity - neg = pos)
            capacity -= people 
            if capacity < 0: # too many people are in the car
                return False
        return True
