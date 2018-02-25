class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) <= 0:
            return False
        else:
            return self.rec(matrix, target, 0, len(matrix[0]) - 1)

    def rec(self, matrix, target, row, col):
        rows = len(matrix)

        if row >= rows or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            return self.rec(matrix, target, row, col - 1)
        elif matrix[row][col] < target:
            return self.rec(matrix, target, row + 1, col)

        # brute force

        # shapes = np.shape(matrix)
        # if shapes[0] > 1:
        #     for i in range(shapes[0]):
        #         if target in matrix[i][:]:
        #             return True
        #     return False
        # elif shapes[0] == 1:
        #     if target in matrix[0]:
        #         return True
        #     return False
        # else:
        #     return False



matrix = []
target = 5
# print(Solution.isMatch(Solution.isMatch,s,p))
print(Solution.searchMatrix(Solution.searchMatrix, matrix, target))