class Solution:
    """Accepted, but really bad runtime
    Obvious optimization: iterate over the rows, not the queens (since each queen has to go on a separate row)
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        solutions = []
        rows = set()
        cols = set()
        forward_diags = set()
        backward_diags = set()

        def add_queens(numqs, x, y):
            if numqs == n:
                solutions.append(["".join(row) for row in board])
                return
            while x in rows or y in cols or (x - y) in forward_diags or (
                    x + y) in backward_diags:
                x, y = x + (y + 1) // n, (y + 1) % n
            if max(x, y) >= n:
                return
            board[x][y] = "Q"
            rows.add(x)
            cols.add(y)
            forward_diags.add(x - y)
            backward_diags.add(x + y)
            add_queens(numqs + 1, x + (y + 1) // n, (y + 1) % n)
            rows.remove(x)
            cols.remove(y)
            forward_diags.remove(x - y)
            backward_diags.remove(x + y)
            board[x][y] = "."
            add_queens(numqs, x + (y + 1) // n, (y + 1) % n)

        add_queens(0, 0, 0)
        return solutions

    @staticmethod
    def print_soln(soln):
        for row in soln:
            print("  ".join([c for c in row]))
            print()
