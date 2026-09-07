"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda x: x.start) 
        
        # 2. Compare each meeting's start to the previous meeting's end
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False  # Overlap found!
                
        return True  # No overlaps found