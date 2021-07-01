# AtCoder Beginner Contest 153 E - Creasted Ibis vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_e
# tag: DP 基礎問題

# 一つの要素を好きな回数使用することができる場合の、
# 典型かつ基礎的な DP を使用する問題。
# ここでは、配列を使いまわしながら解いていっている。

# ちなみに、Python だと TLE になってしまうので
# Pypy で提出するようにしよう。

# 配るDP
def main():
    H, N = map(int, input().split())
    magics = [list(map(int, input().split())) for _ in range(N)]

    # dpt[d]: = 合計使用魔力
    # d = モンスターに与えたダメージ量
    dpt = [10**9] * (H+1)
    dpt[0] = 0
    for dmg, mp in magics:
        for d in range(H):
            dmg_nxt = min(H, d + dmg)
            mp_nxt = dpt[d] + mp
            if dpt[dmg_nxt] > mp_nxt:
                dpt[dmg_nxt] = mp_nxt
    
    print(dpt[-1])

main()

# もらうDP
def main2():
    H, N = map(int, input().split())
    magics = [list(map(int, input().split())) for _ in range(N)]

    # dpt[d]: = 合計使用魔力
    # d = モンスターに与えたダメージ量
    dpt = [10**9] * (H+1)
    dpt[0] = 0
    for dmg, mp in magics:
        for d in range(1, H+1):
            prev_dmg = max(0, d - dmg)
            prev_mp = dpt[prev_dmg]

            if dpt[d] > prev_mp + mp:
                dpt[d] = prev_mp + mp
    
    print(dpt[-1])

# main2()
