import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        querys, values = test_input
        querys.pop(0)
        obj = SubrectangleQueries(values.pop(0))
        result = [None]
        for i in range(len(querys)):
            if querys[i] == "getValue":
                row, col = values[i]
                result.append(obj.getValue(row, col))
            else:
                row1,col1,row2,col2,newValue = values[i]
                result.append(obj.updateSubrectangle(row1,col1,row2,col2,newValue))
        return result


class SubrectangleQueries:

    def __init__(self, rectangle):
        self.sub_rectangle = rectangle.pop()
        # self.sub_rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        diff_col = col2 - col1
        new_val_row = [newValue] * (diff_col + 1)
        for r in range(row1, row2 + 1):
            self.sub_rectangle[r][col1:col2 + 1] = new_val_row

    def getValue(self, row: int, col: int) -> int:
        return self.sub_rectangle[row][col]
