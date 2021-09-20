# AtCoder Regular Contest 081 D - Coloring Dominoes
# https://atcoder.jp/contests/arc081/tasks/arc081_b
# tag: 考察 DP ドミノ 敷き詰め MOD 数え上げ すぬけ君

# 左端から敷き詰めていくことを考える。
# 敷き詰め方は、縦置きで 2マス埋めるか、
# 横置きで 4マス埋めるかの二通りしかなく、
# 通り数は前回の縦横と今回の縦横によって決定される。

# 縦→横は、2通り
# ABB    ACC
# ACC or ABB

# 縦→縦は、2通り
# AB    AC
# AB or AC

# 横→横は 3通り
# AABB    AABB    AACC
# BBAA or BBCC or BBAA

# 横→縦は 1通り
# AAC
# BBC

def main():
    N = int(input())
    s1, s2 = input(), input()
    MOD = 10**9 + 7

    # 縦置き横置きの状況を確認しておく。
    vert = []
    idx = 0
    while idx < N:
        if s1[idx] == s2[idx]:
            vert.append(True)
            idx += 1
        else:
            vert.append(False)
            idx += 2

    # 最初の縦横による組み合わせ数。
    # 最初の一回だけは組み合わせが多くなる。
    if vert[0]:
        result = 3
    else:
        result = 6

    # 次からは、前回が縦横どちらだったかで
    # 組み合わせ数の計算が変化する。
    for prev, now in zip(vert, vert[1:]):
        # 縦置き→縦置き or 縦置き→横置き なら 2通り
        if prev:
            result = (result * 2) % MOD
        # 横置き→縦置き は 1通り
        elif now:
            continue
        # 横置き→横置き なら 3通り
        else:
            result = (result * 3) % MOD

    print(result)

main()

