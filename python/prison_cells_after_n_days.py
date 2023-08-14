"""
Amazon interview question: failed to solve in time during practice exam

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).
"""


class Solution:

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        """
        96.15 %ile runtime
        51.10 %ile memory
        """
        num = int("".join(map(str, cells)), base=2)
        seen, iseen = {}, {}
        for i in range(2**8):
            num = (~((num >> 1) ^ (num << 1))) & (2**7 - 2)
            if num in seen:
                period = i - seen[num]
                if period != 1:
                    idx = seen[num] + ((n - i - 1) % period)
                    num = iseen[idx]
                break
            seen[num] = i
            iseen[i] = num
        return [int(c) for c in bin(num)[2:].rjust(8, '0')]
