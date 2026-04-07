class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for i in range(9):
            count_row = set()
            for j in range(9):
                value = board[i][j]
                if(value!="."):
                    if value in count_row:
                        return False
                    else:
                        count_row.add(value)

        #column check
        for i in range(9):
            count_column = set()
            for j in range(9):
                value = board[j][i]
                if(value!="."):
                    if value in count_column:
                        return False
                    else:
                        count_column.add(value)

        # 3*3 box check

        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[3*box_row + i][3*box_col + j]
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)
        return True
