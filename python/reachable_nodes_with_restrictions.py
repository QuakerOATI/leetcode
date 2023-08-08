class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """
        91.58 %ile runtime
        76.85 %ile memory
        """
        restricted = set(restricted)
        adj = {}

        for a, b in edges:
            adj.setdefault(a, set())
            adj.setdefault(b, set())
            adj[a].add(b)
            adj[b].add(a)

        total = 0
        stack = [0]
        while len(stack) > 0:
            curr = stack.pop()
            if curr not in restricted:
                total += 1
                restricted.add(curr)
                neighbors = list(adj[curr].difference(restricted))
                stack.extend(neighbors)

        return total
            
