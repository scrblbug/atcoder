# AtCoder Beginner Contest 174 F - Range Set Query
# https://atcoder.jp/contests/abc174/tasks/abc174_f
# tag: 範囲問い合わせ フェニック木 セグメント木

# セグメント木で集合管理をすれば行けるんじゃない？
# と気軽にやってみたが、集合の合成に時間がかかりすぎてNG。

# その他いろいろ試してみては TLE だったが、最終的に以下のやり方が
# 一番楽でギリ間に合う……？
# 定数倍でもそれなりに削らないと、Python(Pypy)では厳しい。

# 玉の種類を数える＝最後に現れた玉だけをカウントする、と考える
# そこで、色 i の玉が前回現れた地点を管理するリストを用意する。

# クエリについては右端であらかじめソートしておき、
# 順次新しい玉を追加していくとともに、クエリへの回答を行う。

# 入力例2 [2, 5, 6, 5, 2, 1, 7, 9, 7, 2] の例
# 今最初の4つの玉 [2, 5, 6, 5] を見ている時、
# last_appeared = [-1, -1, 0, -1, -1, 3, 2, ...] (-1 は未出現)
# count = [1, 0, 1, 1, ....]

# 次に5つ目の玉を追加して [2, 5, 6, 5, 2] となった時、
# last_appeared = [-1, -1, 4, -1, -1, 3, 2, ...]
# count = [0, 0, 1, 1, 1, ...]
# のように更新される

# クエリ問い合わせ(l, r)については、
# sum(count[l-1:r]) が回答となるが、
# この sum を素早く計算するため、フェニック木 or セグメント木で
# 管理を行うこととする。

# ここでは、フェニック木を使用した
class BIT:
    def __init__(self, N):
        self.tree = [0] * (N + 1)
        self.N = N
    
    def add(self, pos, x):
        pos += 1
        while pos <= self.N:
            self.tree[pos] += x
            pos = pos + (pos & -pos)
    
    def get_sum_to(self,pos):
        pos += 1
        result = 0
        while pos > 0:
            result = result + self.tree[pos]
            pos = pos - (pos & -pos)
        return result
    
    def get_sum_from_to(self, l, r):
        return self.get_sum_to(r) - self.get_sum_to(l-1)

def main():
    N, Q = map(int, input().split())
    balls = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # r 毎にクエリを整理しておく
    # ついでに、l, r を 0-indexed に整理
    # あとからクエリ順に回答を行うので、インデックスも一緒に持っておく
    sorted_q = [[] for _ in range(N)]
    for i, (l, r) in enumerate(queries):
        sorted_q[r-1].append((l-1, i))

    # 管理用リスト・フェニック木
    last_appeared = [-1] * (N+1)
    count = BIT(N)

    # 回答保管用リスト
    answers = [0] * Q

    # ボールを追加しつつ、クエリがあれば処理していく
    # 当初クエリが現れる r まで while で回してやってみていたが、
    # while は for に比べて遅いので、全て for で回すのが吉
    for r in range(N):
        count.add(r, 1)

        # 以前現れている色の玉なら、前の玉をカウントから外す
        if last_appeared[balls[r]] != -1:
            count.add(last_appeared[balls[r]], -1)

        last_appeared[balls[r]] = r

        # 該当するクエリがあれば、処理して回答を格納
        for l, i in sorted_q[r]:
            answers[i] = count.get_sum_from_to(l, r)
    
    for ans in answers:
        print(ans)

main()
