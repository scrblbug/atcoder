# 三井住友信託銀行プログラミングコンテスト2019 F - Interval Running
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_f
# tag: 考察

# 二人の差だけを考えた場合、
# まず (a1 - b1) * t1 
# 次に (a2 - b2) * t2 加算される……というのを繰り返す。
# これが、何回 0 を通るのかという問題。

# 仮に前者を d1, 後者を d2 とする。
# 0 を通るためには、d1 と d1 + d2 は符号が反対の必要がある。
# つまり、
# d1 > 0 の場合、d1 + d2 > 0 なら常に差は 0 より大きくなり、
# 0 を通ることはない。
# d1 < 0 の場合、d1 + d2 < 0 なら同様に 0 を通ることはない。

# d1 + d2 = 0 の場合、差は d1 → d1+d2=0 → d1 → 0 と
# 無限回出会うことになる。

# 仮に d1 > 0 の時を考える。
# d1 + d2 = -t になるとすると、次回は丁度 t 左側にシフトすることになる。
# ----------0----------
#           ---->
#         <------
# t:      <>
#         ---->
#       <------
# t:    <>
#       ---->

# ここで、右向きの矢印に注目して考えてみると、
# d1 // t 回 右に行く時に 0 を通ることが出来る。
# また、次に左に行く時に 0 を通るので、計 2 回会うことになる。

# ただし、d1 が丁度 t で割り切れる時は、0 を通過せず、0 に丁度触れて
# 左に行くため、最後の 1 回は 1 回しか会わない。

# d1 < 0 のときも同様。

def main():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    d1 = (a1 - b1) * t1
    d2 = (a2 - b2) * t2

    # d1 + d2 = 0 なら無限回会う
    if d1 + d2 == 0:
        print('infinity')
        return

    # d1 と d1 + d2 は符号が反対の必要がある
    if d1 * (d1 + d2) > 0:
        print(0)
        return

    # 最初に 1 回出会う
    result = 1

    # 考察に基づき、さらに (d1 // t) * 2 回出会う。
    t = -(d1 + d2)
    result += 2 * (d1 // t)

    # ただし、d1 % t == 0 なら、1 回引く。
    if d1 % t == 0:
        result -= 1

    print(result)

main()