# AtCoder Regular Contest 120 B - Uniformly Distributed
# https://atcoder.jp/contests/arc120/tasks/arc120_b
# tag: グリッド 色塗り 特殊構造 数え上げ

# 次の 3 x 3 の経路を考えてみる。
# 1 2 3
# 4 5 6
# 7 8 9

# 1 4 7 8 9
# 1 4 5 8 9
# という、一個違いの経路について考慮してみると、
# 5 と 7 は同じ色で無ければならない。
# 同様に、1 4 5 6 9 と 1 2 5 6 9 から
# 2 と 4 も同じ色。
# つまり、右上→左下の方向の斜めに隣り合ったマスは、
# すべて同じ色でなければならない。

# ところで、スタートからの距離をプロットすると
# 斜めの模様になることを考慮すると、逆にこの場合、
# あらゆる経路は全く同じ色のパターンとなり、
# 条件を満たすことになる。

def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    MOD = 998244353
    # スタートからの距離別に管理する

    # 0: どちらでもいい 
    # 1: 赤
    # 2: 青
    # 3: 矛盾
    # という感じでビットで色を管理
    dist_color = [0] * (H+W-1)

    for h in range(H):
        for w in range(W):
            dist = h + w
            if field[h][w] == 'R':
                color = 1
            elif field[h][w] == 'B':
                color = 2
            else:
                color = 0

            # 色はビット演算のORを利用して更新する
            dist_color[dist] |= color

    result = 1
    # 距離別に見ていく
    for d in range(H+W-1):
        # 赤と青の両方の色があれば、矛盾なので 0 を
        # 返して終了する
        if dist_color[d] == 3:
            print(0)
            return
        # 色が決定していない時のみ、赤 or 青にできるので、
        # 2 を掛ける
        elif dist_color[d] == 0:
            result = (result * 2) % MOD

    print(result)

main()
