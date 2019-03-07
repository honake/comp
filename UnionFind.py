class UnionFind:
    # parent：親の番号を格納する
    # 親だった場合は-(その集合のサイズ)
    # すべてのノードが独立した状態でスタート
    def __init__(self, N):
        self.parent = [-1]*N
    
    # aがどのグループに属しているか再帰的に調べる
    def root(self, a):
        if(self.parent[a] < 0):
            return a
        else:
            # returnする前に親をメモしてしまう
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    
    # aのいるグループの頂点数を調べる
    def size(self, a):
        return -self.parent[self.root(a)]
        
    # aとbをくっつける
    def connect(self, a, b):
        # aとbを直接つなぐのではなくroot(a)にroot(b)をくっつける
        a = self.root(a)
        b = self.root(b)
        if(a==b):
            # 既にくっついているのでくっつけない
            return False
        else:
            # 大きいほうaに小さいほうbをくっつけたい
            # 大小逆ならひっくり返す
            if(self.size(a) < self.size(b)):
                a,b=b,a
            # aのサイズを更新する
            self.parent[a] += self.parent[b]
            # bの親をaに変更する
            self.parent[b] = a
            return True
            
# Example
# ABC120 D
# https://atcoder.jp/contests/abc120/submissions/4491646

N,M=list(map(int,input().split()))
A,B=[],[]
ans=[0]*M
Uni=UnionFind(N)
for i in range(M):
    a,b=list(map(int,input().split()))
    A.append(a-1)
    B.append(b-1)
 
ans[M-1] = int(N*(N-1)/2)
 
for i in range(M-1,0,-1):
    # 繋がってなかったのが繋がったとき
    if(Uni.root(A[i])!=Uni.root(B[i])):
        ans[i-1] = ans[i] - Uni.size(A[i])*Uni.size(B[i])
    else:
        ans[i-1] = ans[i]
    Uni.connect(A[i],B[i])
for i in range(M):
    print(ans[i])
