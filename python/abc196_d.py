# AtCoder Beginner Contest 196 D - Hanjo
# https://atcoder.jp/contests/abc196/tasks/abc196_d
# tag: グリッド 敷き詰め DFS

# H*W <= 16 と制約が緩いので、基本に忠実に
# DFSで全探索を行う。

# 畳の置かれている状態の管理は左上から右方向に番号をふり、
# 0 1 2
# 3 4 5
# 6 7 8
# それぞれの番号に応じたビットにて管理を行う。
# 例： 0, 2, 3 の場所が埋まっている時、0b1101 = 13

import sys
sys.setrecursionlimit(10**9)
def main():
    H, W, A, B = map(int, input().split())

    # 左上から右方向に畳を埋めていく
    # filled: 畳の敷かれている状態（全体をビットで管理）
    # now: 今見ている畳
    # rest_a, rest_b: 畳の残り枚数
    def dfs(filled, rest_a, rest_b):
        # 全部埋まれば 1 を返す
        if filled == 2**(H*W) - 1:
            return 1
        
        result = 0

        # 一番左上の空いている場所
        # i & -i で i の一番右側に立っているビットを得られるので、
        # (~filled & -(~filled)) で filled の一番右の 0 を得られる。
        now = (~filled & -(~filled)).bit_length() - 1
        now_h, now_w = now // W, now % W

        # 半畳を置く場合
        if rest_b > 0:
            nxt_filled = filled | 1<<now
            result += dfs(nxt_filled, rest_a, rest_b-1)
        
        # 一畳を置く場合
        if rest_a > 0:
            # 横に置く場合
            if now_w < W-1 and not filled & 1<<(W*now_h + now_w+1):
                nxt_filled = filled | 1<<now | 1<<(W*now_h + now_w+1)
                result += dfs(nxt_filled, rest_a-1, rest_b)
            # 縦に置く場合
            if now_h < H-1 and not filled & 1<<(W*(now_h+1) + now_w):
                nxt_filled = (filled | (1<<now)) | (1<<(W*(now_h+1) + now_w))
                result += dfs(nxt_filled, rest_a-1, rest_b)

        return result

    print(dfs(0, A, B))

main()
