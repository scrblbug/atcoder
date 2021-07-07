# AtCoder Petrozavodsk Contest 001 B - Two Arrays
# https://atcoder.jp/contests/apc001/tasks/apc001_b
# tag: 考察 数列 一致

# 数列の差分のみに注目すればいい。
# f.e.（入力例2）
# a: 3  1  4  1  5
# b: 2  7  1  8  2
# の差分は、
# d: 1 -6  3 -7  3

# 元の操作は、
# 差分の数列のどこかに 2 を足し、 どこかから 1 を引く
# （あるいは、同じ場所を選んだ場合どこかに 1 を足す）
# のと同等。

# この差分を全て 0 にしたいので、ひとまず今 1 以上の場所を
# 全て 0 にするための操作回数を考える。
# 当然同じ回数だけどこかに 2 を足さなければならないので、
# -2 以下のところに 2 を足していくことになる。

# ここで、1 以上の場所を全て 0 に出来た時、
# 全ての値が 0 以下に収まっていれば、
# 一致可能となる。

# 念の為だが、最後に 1 -1 -1 -1 みたいな残り方の場合は
# 1 -1 -1 -1 → 0 1 -1 -1 → 0 0 1 -1 → 0 0 0 1 となり
# 残ってしまうことになるので不可。
# -1 に 2 を足してはダメ。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    diff = [a-b for a, b in zip(A, B)]

    # 1 以上のところを 0 にするための手数
    op_neg = sum(n for n in diff if n > 0)

    # -2 以下のところに 2 を足せる回数
    op_pos = sum((-n)//2 for n in diff if n < 0)

    if op_neg <= op_pos:
        print('Yes')
    else:
        print('No')

main()
