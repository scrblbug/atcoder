# Tenka1 Programmer Beginner Contest C - Align
# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_c
# 数列 隣接 差分 最大 考察

# 直感としては、大小大小……もしくは小大小大……という具合に
# 並んでいるのがよさそうではある。

# 仮に途中に a <= b <= c となる並びがあった場合、
# その差分の合計は (c - b) + (b - a) = c - a となるが、
# b を移動した b a c あるいは a c b という並びのほうが、
# 差分の合計が (c - a) + (b - a) と大きくなる。

# さて、仮に大小大小……で数列を作成するとして、
# abcdef という並びの場合、その差分の合計は
# a + 2c + 2e - (2b + 2d + f) という感じになる。
# つまり、両端でない数は必ず 2回足されるか引かれるかする。

# よって考慮すべき内容としては、
# １）足す数に分類するか引く数に分類するか
# ２）端をどうするか

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    A.sort()

    # 偶数個の場合
    if N % 2 == 0:
        plus = A[N//2:]
        minus = A[:N//2]

        result = 2 * sum(plus) - 2 * sum(minus)

        # 足す数は一番小さいものを、
        # 引く数は一番大きいものを端に持っていく
        result = result - plus[0] + minus[-1]

    # 奇数個の場合
    else:
        plus = A[N//2+1:]
        minus = A[:N//2]
        mid = A[N//2]

        tmp_r = 2 * sum(plus) - 2 * sum(minus)

        # 中央の数を足す方にする場合
        # 両端が足す数になる。足す数のうち小さいものから順に 2個
        # 端に移動するが、そのうち1つは中央の数
        res1 = (tmp_r + mid * 2) - mid - plus[0]

        # 中央の数を引く方にする場合
        # 両端が引く数に（以下略
        res2 = (tmp_r - mid * 2) + mid + minus[-1]

        # 比べて大きい方を取る
        result = max(res1, res2)

    print(result)

main()

# 実は貪欲法でも通る。
# 残りから一番大きいもの or 一番小さいものを、
# 点数が高くなるように次々に数列の左右に追加していく感じ。

from collections import deque
def main2():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    A.sort()

    # 一番大きいのを取り出し、数列の元とする。
    # 以下両端のみ管理。
    left = right = A.pop()
    result = 0

    rem = deque(A)

    while rem:
        scores = []

        # (右|左)から取って(右|左)につける
        rr = abs(right - rem[-1])
        rl = abs(left - rem[-1])
        lr = abs(right - rem[0])
        ll = abs(left - rem[0])

        # 左右どちらから取る？
        if max(rr, rl) >= max(lr, ll):
            pick = rem.pop()
        else:
            pick = rem.popleft()
        
        # 一番差分が大きくなるようにつける
        if abs(pick - right) >= abs(pick - left):
            result += abs(pick - right)
            right = pick
        else:
            result += abs(pick - left)
            left = pick
    
    print(result)

# main2()

