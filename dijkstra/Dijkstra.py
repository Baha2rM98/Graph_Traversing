import sys


class Dijkstra:
    INF = sys.maxsize
    parent = []

    def dijkstra(self, graph, src):
        n = graph.__len__()
        is_checked = [False for i in range(n)]
        dis = [self.INF for i in range(n)]
        self.parent = [-1 for i in range(n)]
        current_node = src
        dis[current_node] = 0
        is_checked[current_node] = True
        while True:
            for i in range(n):
                if not is_checked[i] and graph[current_node][i] != 0 and graph[current_node][i] + dis[current_node] < \
                        dis[i]:
                    dis[i] = graph[current_node][i] + dis[current_node]
                    self.parent[i] = current_node
            min_node = -1
            min_way = self.INF
            for i in range(n):
                if not is_checked[i] and dis[i] < min_way:
                    min_node = i
                    min_way = dis[i]
            if min_node == -1:
                break
            current_node = min_node
            is_checked[current_node] = True
        return dis

    def path(self, des):
        way = []
        i = des
        way.append(i)
        while self.parent[i] != -1:
            way.append(self.parent[i])
            i = self.parent[i]
        way.reverse()
        return way
