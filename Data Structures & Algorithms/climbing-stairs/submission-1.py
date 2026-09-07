class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        """ 
        - One of the possible solution is by running a recursive tree from the first option
        - At each position we can always take either 1 or 2 steps to reach the top of the stairs
        - 


        """
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one