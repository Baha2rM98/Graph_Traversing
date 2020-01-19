class FloydWarshall:
    parent = [[]]

    def floyd_warshall(self, graph):
        n = graph.__len__()
        self.parent = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                self.parent[i][j] = -1

        for k in range(n):
            for j in range(n):
                for i in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        self.parent[i][j] = k
        return graph

    def path(self, src, des):
        if self.parent[src][des] != -1:
            self.path(src, self.parent[src][des])
            print(str(self.parent[src][des]) + " ", end=" ")
            self.path(self.parent[src][des], des)
