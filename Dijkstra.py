from collections import defaultdict
from heapq import heappop, heappush

class Graph(object):
    """
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]

# Example
# ABC135 D
# https://abc035.contest.atcoder.jp/submissions/6216380

g = Graph()
ginv = Graph()

N,M,T=list(map(int, input().split()))
A=list(map(int, input().split()))

for i in range(M):
    s,e,w=list(map(int,input().split()))
    g.add_edge(s-1, e-1, w)
    ginv.add_edge(e-1, s-1, w)
    
d = Dijkstra(g, 0)
dinv = Dijkstra(ginv, 0)
ans = -1

for i in range(N):
    ans = max(ans,(T - (d.shortest_distance(i) + dinv.shortest_distance(i)))*A[i])

print(ans)
