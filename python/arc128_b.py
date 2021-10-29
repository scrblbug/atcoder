# AtCoder Regular Contest 128 B - Balls of Three Colors
# https://atcoder.jp/contests/arc128/tasks/arc128_b
# tag: 考察

# 仮に R に統一すると考える。
# G / B については、ペアに出来るものは R に変換すればいいので、
# そのうちどちらかが余ることになる。

# 余った方を G と仮定する。
# これを R にするためには、次の手順を踏む必要がある。

# 1) RG → BB
# 2) GB → RR
# 3) GB → RR

# 左辺が使用する分になる。
# G / B の数の推移に注目すると、G は 3手を使用して
# 丁度 3 つずつしか
# 減らせないことが分かる。

# 以上を踏まえつつ、R / G / B それぞれに統一するための
# 手数を計算し、最小の値を回答すればいい。

def main():
    T = int(input())
    queries = [list(map(int, input().split())) for _ in range(T)]

    def get_turn_count(to, from1, from2):
        if from1 == from2 == 0:
            return 0
        
        # to と他 1種類が 0 の場合、to の数が不足することになるが、
        # 他の他の呼び出し時に 0 が返り、それが最小になるので気にしない。
        diff = abs(from1 - from2)
        
        # 不可能なケースは 10**10 あたりを返しておく。
        if diff % 3 != 0:
            return 10**10

        return min(from1, from2) + (diff // 3) * 3

    for r, g, b in queries:
        result = min(get_turn_count(r, g, b),
                     get_turn_count(g, b, r),
                     get_turn_count(b, r, g))
        if result == 10**10:
            print(-1)
        else:
            print(result)
main()
