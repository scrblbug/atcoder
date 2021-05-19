# AtCoder Beginner Contest 027 B - 島と橋
# https://atcoder.jp/contests/abc027/tasks/abc027_b
# tag: 考察 高橋君

# 左側から順番に、橋をかける必要があるかどうか判定していく。

def main():
    N = int(input())
    pops = list(map(int, input().split()))

    total = sum(pops)

    # そもそも人数を均等にできないなら、-1 を返して終了
    if total % N != 0:
        print(-1)
        return

    # 各島あたりの人数を確認しておく
    each = total // N

    # 今繋げている島の数と、そこにいる人数を管理
    n_islands = 0
    g_pop = 0

    result = 0
    # 左端から島を見ていき、今の状態で各島の人数を
    # 条件に合うように分配可能かどうかを確認する。
    # 条件にあっていれば、次の島に橋を架ける必要はないが、
    # 条件にあってなければ、橋を架ける必要がある。
    for p in pops:
        n_islands += 1
        g_pop += p

        # 今の状態で分配可能なら、橋は架けずに次の島から改めて見ていく
        if g_pop / n_islands == each:
            n_islands = 0
            g_pop = 0
        # ダメなら、橋を架ける ＝ 次の島の分も加算して考えていく
        else:
            result += 1
    
    print(result)

main()
