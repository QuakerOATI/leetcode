from typing import Any, List
from collections import OrderedDict, Counter
from random import uniform


class LinkedTorusNode:

    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up if up is not None else self
        self.down = down if down is not None else self
        self.right = right if right is not None else self
        self.left = left if left is not None else self

    def is_excised_lateral(self):
        return self.left.right is not self or self.right.left is not self

    def is_excised_vertical(self):
        return self.up.down is not self or self.down.up is not self

    def excise_lateral(self):
        self.left.right = self.right
        self.right.left = self.left

    def excise_vertical(self):
        self.up.down = self.down
        self.down.up = self.up

    def restore_lateral(self):
        self.left.right = self
        self.right.left = self

    def restore_vertical(self):
        self.up.down = self
        self.down.up = self

    def equator(self, reversed=False):
        curr = self
        if reversed:
            while (curr := curr.left) is not self:
                yield curr
            yield self
        else:
            yield self
            while (curr := curr.right) is not self:
                yield curr

    def meridian(self, reversed=False):
        curr = self
        if reversed:
            while (curr := curr.up) is not self:
                yield curr
            yield self
        else:
            yield self
            while (curr := curr.down) is not self:
                yield curr


class ConstraintMatrix:
    """A sparse Boolean matrix for use in solving constraint problems."""

    class NoSolution(Exception):
        pass

    class Solution(Exception):
        pass

    class ConstraintMatrixElement(LinkedTorusNode):

        def __init__(self, header, row, **kwargs):
            super().__init__(**kwargs)
            self.header = header
            self.row = row
            self.visited = -1

    class ConstraintMatrixHeaderNode(LinkedTorusNode):

        class EmptyColumn(Exception):
            pass

        class RandomIterator:

            def __init__(self, header, seed):
                self._header = header
                self._seed = seed
                self._curr = header
                self._num = 0

            def __next__(self):
                if self._num >= self._header.count:
                    raise StopIteration
                while self._curr is self._header or self._curr.visited == self._seed or uniform(
                        0, 1) > self._header.RANDOMIZATION_PROBABILITY:
                    self._curr = self._curr.down
                self._curr.visited = self._seed
                self._num += 1
                return self._curr

            def __iter__(self):
                return self

            @property
            def curr(self):
                return self._curr

        RANDOMIZATION_PROBABILITY = 0.3

        def __init__(self, count=0, **kwargs):
            super().__init__(**kwargs)
            self.count = count
            self.num_random_traversals = 0

        def __iter__(self):
            """Iterate through a column, skipping the header node."""
            return filter(lambda n: n is not self, self.meridian())

        def __reversed__(self):
            return filter(lambda n: n is not self,
                          self.meridian(reversed=True))

        def is_empty(self):
            return self is self.down

        def randomized(self):
            if self.is_empty():
                raise self.EmptyColumn
            self.num_random_traversals += 1
            return self.RandomIterator(self, self.num_random_traversals)

    def __init__(self, rows: List[Any]):
        self._rows = OrderedDict({r: None for r in rows})
        self._columns = None
        self._solution = []
        self.maxdepth = 0
        self.num_eliminations = 0

    def add_column(self, rows):
        header = self.ConstraintMatrixHeaderNode(
            count=0,
            right=self._columns,
            left=None if self._columns is None else self._columns.left)
        header.restore_lateral()
        self._columns = header.right
        for r, pointer in self._rows.items():
            if r in rows:
                node = self.ConstraintMatrixElement(
                    header,
                    r,
                    up=header.up,
                    down=header,
                    right=pointer,
                    left=pointer.left if pointer is not None else None)
                node.restore_lateral()
                node.restore_vertical()
                self._rows[r] = node.right
                header.count += 1

    def _remove_conflicts(self, node):
        """The nested loop step of the Dancing Links algorithm.

        Note that this need not check for empty columns, as only columns 
        intersecting the "equator" of the passed node will be removed.
        """
        for col in map(lambda n: n.header, node.equator()):
            for n in col:
                for conflict in n.equator():
                    if n is not conflict:
                        conflict.header.count -= 1
                        conflict.excise_vertical()
            if col is self._columns:
                self._columns = col.right
            col.excise_lateral()
            if col is self._columns:
                self._columns = None

    def _restore_conflicts(self, node):
        """The backtracking step of Dancing Links."""
        for col in map(lambda n: n.header, node.equator(reversed=True)):
            col.restore_lateral()
            for n in reversed(col):
                for conflict in n.equator(reversed=True):
                    if conflict is not n:
                        conflict.header.count += 1
                        conflict.restore_vertical()
            if self._columns is None:
                self._columns = col

    def get_num_columns(self):
        """Traverses the header list and returns the number of column headers."""
        return len(list(self._columns.equator()))

    def get_min_column(self):
        """Returns the column with the fewest links."""
        if self._columns is None:
            raise self.Solution()
        ret = self._columns
        for header in self._columns.equator():
            ret = min(ret, header, key=lambda h: h.count)
        return ret

    def choose_row(self, row):
        """Specify that a solution must contain a given row."""
        self._remove_conflicts(self._rows[row])
        # del self._rows[row]

    def _pushcolumn(self):
        # if len(self._solution
        #        ) == 0 or self._solution[-1]._header.is_excised_lateral():
        # Raises EmptyColumn if min_column is empty
        self._solution.append(self.get_min_column().randomized())
        self.maxdepth = max(self.maxdepth, len(self._solution))

    def _pushrow(self):
        self._remove_conflicts(next(self._solution[-1]))
        self.num_eliminations += 1

    def _popcolumn(self):
        if self._solution[-1]._header.is_excised_lateral():
            self._poprow()
        self._solution.pop()

    def _poprow(self):
        self._restore_conflicts(self._solution[-1].curr)

    def _recurse(self):
        if self.depth == 0:
            raise self.NoSolution()
        try:
            if self._solution[-1]._header.is_excised_lateral():
                # assert not self._solution[-1]._header.is_empty(
                # ), "Inconsistent recursion state (empty column excised)"
                self._pushcolumn()
            else:
                self._pushrow()
                assert self._solution[-1]._header.is_excised_lateral(
                ), "Inconsistent recursion state (top column not excised after pushrow)"
        except self.ConstraintMatrixHeaderNode.EmptyColumn:
            # Should only occur when we attempt to push an empty column
            # Since columns are pushed deterministically, this means we should poprow()
            self._poprow()
            assert len(
                self._solution
            ) == 0 or not self._solution[-1]._header.is_excised_lateral(
            ), "Inconsistent recursion state (top column excised after poprow)"
        except StopIteration:
            # Should only occur when the top randomized iterator finishes
            self._popcolumn()
            assert len(
                self._solution
            ) == 0 or self._solution[-1]._header.is_excised_lateral(
            ), "Inconsistent recursion state (top column not excised after popcolumn)"
            self._poprow()

    def is_empty(self):
        return self._columns is None

    def solve(self):
        if self.is_empty():
            return True
        self._pushcolumn()
        while True:
            try:
                self._recurse()
            except self.Solution:
                return True
            except self.NoSolution:
                return False

    @property
    def depth(self):
        return len(self._solution)

    @property
    def solution(self):
        return [it.curr.row for it in self._solution]

    def get_column_counts(self):
        c = Counter()
        colnum = 0
        for header in self._columns.equator():
            colnum += 1
            ct = 0
            for n in header.meridian():
                if n is not header:
                    ct += 1
            assert ct == header.count, f"Count inconsistent with column state at column {colnum}"
            c[ct] += 1
        return c

    def take_snapshot(self):
        self.snapshot = self.get_state()

    def get_state(self):
        return {
            "depth": self.depth,
            "is_empty": self.is_empty(),
            "len(min_col)": self.get_min_column().count,
            "num_eliminations": self.num_eliminations,
            "column_counts": self.get_column_counts()
        }

    def audit(self):
        self._pushcolumn()
        while True:
            self._recurse()
            print(self.get_state())


class SudokuConstraintMatrix(ConstraintMatrix):

    def __init__(self):
        super().__init__([((i, j), k) for i in range(1, 10)
                          for j in range(1, 10) for k in range(1, 10)])
        # uniqueness constraints
        for i in range(1, 10):
            for j in range(1, 10):
                self.add_column([((i, j), k) for k in range(1, 10)])
        # rows
        for i in range(1, 10):
            for k in range(1, 10):
                self.add_column([((i, j), k) for j in range(1, 10)])
        # columns
        for j in range(1, 10):
            for k in range(1, 10):
                self.add_column([((i, j), k) for i in range(1, 10)])
        # boxes
        for bi in range(3):
            for bj in range(3):
                for k in range(1, 10):
                    self.add_column([
                        ((i, j), k)
                        for i in range(3 * bi + 1, 3 * (bi + 1) + 1)
                        for j in range(3 * bj + 1, 3 * (bj + 1) + 1)
                    ])


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = SudokuConstraintMatrix()
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                try:
                    matrix.choose_row(((i + 1, j + 1), int(elem)))
                except ValueError:
                    continue
        matrix.solve()
        self._apply_solution(matrix.solution, board)

    def _apply_solution(self, kv_pairs, board):
        for pos, val in kv_pairs:
            board[pos[0] - 1][pos[1] - 1] = str(val)


class TestSolution:
    from timeit import default_timer as now

    def __init__(self):
        self.runtime = 0
        self.matrix = None
        self.board = None

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.matrix = SudokuConstraintMatrix()
        self.board = [row.copy() for row in board]
        start = self.now()
        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                try:
                    print(f"Choosing element {(i+1, j+1, int(elem))}...")
                    self.matrix.choose_row(((i + 1, j + 1), int(elem)))
                    if self.matrix._columns is None:
                        raise Exception(
                            f"Choosing element {(i+1, j+1, int(elem))} abnormally emptied matrix"
                        )
                except ValueError:
                    continue
        try:
            self.matrix.solve()
            self._apply_solution(self.matrix.solution, self.board)
        finally:
            self.runtime = self.now() - start

    def _apply_solution(self, kv_pairs, board):
        for pos, val in kv_pairs:
            board[pos[0] - 1][pos[1] - 1] = str(val)


class HittingProblem:

    def __init__(self, variables: dict):
        """Defines a collection of discrete variables to be constrained.

        Params:
          variables: Map from variable names to iterables containing possible values.
        """
        self._matrix = ConstraintMatrix((varname, value)
                                        for varname in variables
                                        for value in variables[varname])

    def add_exact_constraint(self, variables: dict):
        """Adds a constraint to the collection of variables.

        Expresses the constraint that precisely one of the named variables must
        evaluate to its corresponding value.

        Params:
          variables: Map from variable names to iterables containing mutually-
            exclusive possible values.
        """
        self._matrix.add_column((varname, value) for varname in variables
                                for value in variables[varname])

    def solve(self):
        self._matrix.solve()
        return self._matrix.solution


class Sudoku:

    def __init__(self, mat):
        self._board = mat
        self._solved = [row.copy() for row in mat]
        self._matrix = SudokuConstraintMatrix()
        for i, row in enumerate(mat):
            for j, elem in enumerate(row):
                try:
                    self._matrix.choose_row(((i + 1, j + 1), int(elem)))
                except ValueError:
                    continue

    def _apply_solution(self, kv_pairs):
        for pos, val in kv_pairs:
            self._solved[pos[0] - 1][pos[1] - 1] = str(val)

    @classmethod
    def print_board(cls, board):
        for row in board:
            print("    ".join([*map(str, row)]))
            print()

    def print(self):
        print("Before:")
        print("------")
        print()
        self.print_board(self._board)
        print("After:")
        print("-----")
        print()
        self.print_board(self._solved)

    @classmethod
    def verify(cls, board):
        # rows
        for i in range(9):
            if len([*filter(str.isnumeric, board[i])]) != len(set(board[i])):
                print(f"Repeat found in row {i}")
                return False

        # cols
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if len(col) != len(set(col)):
                print(f"Repeat found in column {j}")
                return False

        # boxes
        for bi in range(3):
            for bj in range(3):
                box = [
                    board[3 * bi + i][3 * bj + j] for i in range(3)
                    for j in range(3)
                ]
                if len(box) != len(set(box)):
                    print(f"Repeat found in box {(bi, bj)}")
                    return False

        return True

    def solve(self):
        self._matrix.solve()
        self._apply_solution(self._matrix.solution)
