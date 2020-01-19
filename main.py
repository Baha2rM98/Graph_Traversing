import sys
from floydwarshall.FloydWarshall import FloydWarshall
from dijkstra.Dijkstra import Dijkstra
from dfs.DFS import DFS
from bfs.BFS import BFS

#   Floyd Warshall  *****************************************************************************
#
# INF = sys.maxsize
# graph = [[0, 5, INF, 2, INF],
#          [INF, 0, 2, INF, INF],
#          [3, INF, 0, INF, 7],
#          [INF, INF, 4, 0, 1],
#          [1, 3, INF, INF, 0], ]
# f = FloydWarshall()
# print(f.floyd_warshall(graph))
# f.path(1, 3)


#   Dijkstra    *****************************************************************************
#
# dijk = Dijkstra()
# graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#          [4, 0, 8, 0, 0, 0, 0, 11, 0],
#          [0, 8, 0, 7, 0, 4, 0, 0, 2],
#          [0, 0, 7, 0, 9, 14, 0, 0, 0],
#          [0, 0, 0, 9, 0, 10, 0, 0, 0],
#          [0, 0, 4, 14, 10, 0, 2, 0, 0],
#          [0, 0, 0, 0, 0, 2, 0, 1, 6],
#          [8, 11, 0, 0, 0, 0, 1, 0, 7],
#          [0, 0, 2, 0, 0, 0, 6, 7, 0],
#          ]
# print(dijk.dijkstra(graph, 0))
# print(dijk.path(8))


# DFS    *****************************************************************************
#
# dfs = DFS()
# graph = {0: {1, 2},
#          1: {2},
#          2: {0, 3},
#          3: {3}}
# dfs.dfs(graph, 1)


#   BFS    *****************************************************************************
#
# bfs = BFS()
# graph = [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1]]
# bfs.bfs(graph, 2)
