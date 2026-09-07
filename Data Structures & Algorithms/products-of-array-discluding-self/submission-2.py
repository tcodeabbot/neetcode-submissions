class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        def mult(nums):
            res = 1

            for n in nums:
                res *= n
            return res

        for i in range(len(nums)):
            left = mult(nums[:i]) if len(nums[:i]) > 0 else 1
            right = mult(nums[i + 1:]) if len(nums[i + 1:]) > 0 else 1

            result[i] = left * right
        return result