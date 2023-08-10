"""
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
"""
from typing import List


class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        79.25 %ile runtime
        90.86 %ile memory

        The fact that this solution is an in-place sort is what makes it so memory-efficient, but the implementation is much more complex than it needs to be as a result.
        """

        def swap(arr, redir, i, j):
            a, b = redir.setdefault(i, [i, i])
            c, d = redir.setdefault(j, [j, j])
            arr[i], arr[j] = arr[j], arr[i]
            redir[b][0] = j
            redir[d][0] = i
            redir[i][1] = d
            redir[j][1] = b

        idx = list(range(len(people)))
        redir = {}
        people.sort()
        prev, degeneracy = -1, 1
        for i in range(len(people)):
            print("------------------")
            f, b = redir.get(i, [i, i])
            ht, rk = people[f]
            print(
                f"prev = {prev}, ht = {ht}, rd = {rk}, degeneracy = {degeneracy}")
            print(f"redir = {redir}")
            if ht == prev:
                rk -= degeneracy
                degeneracy += 1
            else:
                degeneracy = 1
            prev = ht
            print(f"{i} --> redir({i}) = [{f}, {b}]")
            print(f"rk = people[f][1] - degeneracy = {rk}")
            print(f"people = {people}")
            print(f"idx = {idx}")
            # print(f"idx[people[{f}][1]] = {idx[people[f][1]]}")
            # print("------------------")
            swap(people, redir, f, j := idx.pop(rk))
            print(f"f = {f}, i = {i}, j = {j}, b = {b}")
        return people
