from queue import Queue


class BFS:
    def bfs(self, graph, src):
        n = graph.__len__()
        queue = Queue()
        visited = [False for i in range(n)]
        queue.put(src)
        visited[src] = True
        while not queue.empty():
            current_node = queue.get()
            print(str(current_node) + " ", end=" ")
            for i in range(n):
                if graph[current_node][i] != 0 and not visited[i]:
                    queue.put(i)
                    visited[i] = True
