class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for row in range(9):
            seen=set()
            for coloumn in range(9):
                num=board[row][coloumn]
                if num=='.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        #coloumn
        for coloumn in range(9):
            seen=set()
            for row in range(9):
                num=board[row][coloumn]
                if num=='.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        #sub-boxes
        for row in range(0,9,3):
            for coloumn in range(0,9,3):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        num=board[row+i][coloumn+j]
                        if num=='.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
        