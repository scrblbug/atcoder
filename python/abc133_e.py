# AtCoder Beginner Contest 133 E - Virus Tree 2
# https://atcoder.jp/contests/abc133/tasks/abc133_e
# tag: グラフ 木 色塗り MOD
class Cowmod:
    def __init__(self, MOD=10**9+7):
        self._fact = [1, 1]
        self._inv = [1, 1]
        self._inv_fact = [1, 1]
        self._MOD = MOD

    def extend_fact(self, N):
        if len(self._fact) > N+1:
            return
        for i in range(len(self._fact), N+1):
            self._fact.append((i * self._fact[-1]) % self._MOD)

    def extend_inv(self, N):
        if len(self._inv) > N+1:
            return
        for i in range(len(self._inv), N+1):
            self._inv.append((-self._inv[self._MOD % i] * (self._MOD // i)) % self._MOD)

    def extend_inv_fact(self, N):
        if len(self._inv_fact) > N+1:
            return
        self.extend_inv(N)
        for i in range(len(self._inv_fact), N+1):
            self._inv_fact.append((self._inv[i] * self._inv_fact[-1]) % self._MOD)

    def fact(self, N):
        self.extend_fact(N)
        return self._fact[N]
    
    def inv(self, N):
        self.extend_inv(N)
        return self._inv[N]
    
    def inv_fact(self, N):
        self.extend_inv_fact(N)
        return self._inv_fact[N]

    def calc_comb(self, n, r):
        return (self.fact(n) * self.inv_fact(n-r) * self.inv_fact(r)) % self._MOD

def main():
    N, K = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]
    MOD = 10**9 + 7
    cowm = Cowmod(MOD)

    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        paths[a-1].append(b-1)
        paths[b-1].append(a-1)

    # 各ノードごとに、子供の塗り分け方が何通りあるのかを記録する
    vary = [1] * N

    queue = [(-1, 0)]
    while queue:
        prev, now = queue.pop()
        if len(paths[now]) >= K:
            print(0)
            return

        if now == 0:
            vary[now] = (cowm.fact(K-1) * cowm.inv_fact(K-len(paths[now])-1)) % MOD
        elif len(paths[now]) > 1:
            vary[now] = (cowm.fact(K-2) * cowm.inv_fact(K-2-(len(paths[now])-1))) % MOD

        for nxt in paths[now]:
            if nxt == prev:
                continue
            queue.append((now, nxt))

    result = 1
    for i in range(N):
        result = (result * vary[i]) % MOD 
    
    result = (result * K) % MOD
    print(result)

main()
