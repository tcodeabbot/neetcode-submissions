class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        def binary_search(arr, target):
            l, r = 0, len(arr) - 1
            if target > arr[r]:
                return

            while l <= r:
                mid = (l + r) // 2
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True
        
        # loop row by row and call a binary search on each row

        for r in range(rows):
            if binary_search(matrix[r], target):
                return True
        return False