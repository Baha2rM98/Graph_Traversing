class DFS:

    def dfs(self, graph, src, visited=None):
        if visited is None:
            visited = set()
        visited.add(src)
        print(str(src) + " ", end=" ")
        for neighbour in graph[src] - visited:
            self.dfs(graph, neighbour, visited)
        return visited
