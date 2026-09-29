from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(array: List[str]):
            blank_counts = 0
            num_set = set()
            for ele in array:
                if ele != ".":
                    num_set.add(ele)
                else:
                    blank_counts += 1
            
            return len(num_set) == 9 - blank_counts

        def get_i_row(i):
            return board[i]

        def get_i_col(i):
            return [board[j][i] for j in range(9)]

        def get_i_box(i):
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3

            items = []
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    items.append(board[r][c])
            return items

        # check each row, col, box
        for i in range(9):
            row = get_i_row(i)
            if not is_valid_group(row):
                return False
            col = get_i_col(i)
            if not is_valid_group(col):
                return False
            box = get_i_box(i)
            if not is_valid_group(box):
                return False
        
        return True


        