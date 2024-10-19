"""
dict
{1: [2], 2: [1,3,4]: 3: [2], 4: [2]}

Now the problem boils down to find out the node which has n-1 neighbors.
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # edges = [[1,2], [4,2], [2,3]] 
        # dict = {a: []}
        graph = collections.defaultdict(list)
        res = 0

        # construct the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        #print(graph)
        n = len(graph)
        for k , v in graph.items():
            # k = 1, v = [2]
            if len(v) == n-1:
                return k
        return res

