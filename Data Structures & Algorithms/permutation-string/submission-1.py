from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        
        for i in range(len(s2)):
            chunk = s2[i: i + len(s1)]
            count_sub_string = Counter(chunk)

            if count1 == count_sub_string:
                return True
        return False

        
        

