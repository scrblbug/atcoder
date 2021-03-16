# AtCoder Beginner Contest 174 F - Range Set Query
# https://atcoder.jp/contests/abc174/tasks/abc174_f
# tag: 範囲問い合わせ フェニック木 セグメント木

# セグメント木で集合管理をすれば行けるんじゃない？
# と気軽にやってみたが、集合の合成に時間がかかりすぎてNG。

# その他いろいろ試してみては TLE だったが、最終的に以下のやり方が
# 一番楽でギリ間に合う……？
# 定数倍でもそれなりに削らないと、Python(Pypy)では厳しい。

# 玉の種類を数える＝全部の玉の数から、ダブっている玉の数を引く、と考える。
# そこで、色 i の玉が前回現れた地点を管理するリストを用意する。
# また、ダブっている玉の場所を管理するリストも用意する。

# クエリについては右端であらかじめソートしておき、
# 順次新しい玉を追加していくとともに、クエリへの回答を行う。

# 入力例2 [2, 5, 6, 5, 2, 1, 7, 9, 7, 2] の例
# 今最初の4つの玉 [2, 5, 6, 5] を見ている時、
# last_appeared = [-1, -1, 0, -1, -1, 3, 2, ...] (-1 は未出現)
# dubbed = [0, 1, 0, 0, ....]

# 次に5つ目の玉を追加して [2, 5, 6, 5, 2] となった時、
# last_appeared = [-1, -1, 4, -1, -1, 3, 2, ...]
# dubbed = [1, 1, 0, 0, 0, ...]
# のように更新される

# クエリ問い合わせ(l, r)については、
# (r - l + 1) - sum(dubbed[l-1:r]) が回答となるが、
# この sum を素早く計算するため、フェニック木・セグメント木で
# 管理を行うこととする。が、numpy のコンパイルを使わない環境では
# セグ木では厳しいかも……？

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

    def get_sum_from_to(self, pos_from, pos_to):
        return self.get_sum_to(pos_to) - self.get_sum_to(pos_from - 1)

def main():
    N, Q = map(int, input().split())
    balls = list(map(int, input().split()))

    # インデックスを追加つつクエリを取り込み、r でソートする
    # 地味に定数倍改善のため、内包表記で行っている
    sort_q = [(i, l-1, r-1) for i, (l, r) in enumerate([list(map(int, input().split())) for _ in range(Q)])]
    sort_q.sort(key=lambda x:x[2])

    # 管理用リスト・フェニック木
    last_appeared = [-1] * (N+1)
    dubbed = BIT(N)

    # 今いくつ目のボールまで追加しているか
    now = -1

    result = [0] * Q

    for idx, l, r in sort_q:
        while now < r:
            now += 1
            color = balls[now]
            # ボールが初出の場合
            if last_appeared[color] == -1:
                last_appeared[color] = now
            # ボールが2個目以降の場合
            else:
                prev_pos = last_appeared[color]
                dubbed.add(prev_pos, 1)
                last_appeared[color] = now
        # ダブっているボールの数を引いたものが答え
        result[idx] = r - l + 1 - dubbed.get_sum_from_to(l, r)

    # 改めて元のクエリ順に回答を出力
    for r in result:
        print(r)

main()

