# AtCoder Regular Contest 110 C - Exoswap
# https://atcoder.jp/contests/arc110/tasks/arc110_c
# tag: 数列 隣接操作 並び替え

# a b c 1 d e
# のようなケースを考えると、この 1 を左端へ持っていくには、
# a b c 1 d e
#  3 2 1
# 1 より左側の入れ替えについては、必ずこの順番で行う
# 必要がある。
# また、この操作を行った後、
# 1 a b c d e
#  x x x      ← 操作済
# となるため、必然的に a, b = 2, 3 でなければならない。

# 次に c d e のどれが 4 なのかに基づき、操作が決定される。

# c = 4 の場合。操作によって必ず移動するので、
# 条件を満たせない。よって不可能。

# d = 4 の場合。cd, de の順で交換を行う。
# e = 4 の場合。de の交換を先に行うことになる。

# ……みたいな感じで、確定していない最少の数字から
# 操作を決定していけばいけそう。

def main():
    N = int(input())
    P = list(map(int, input().split()))

    result = []

    # 次の数字。next-1 までは確定済みとする
    next = 1

    while next < N:
        # 次の数字の場所を探す。
        # 考察よりP[next] 以降でなければならない。
        next_idx = next
        while next_idx < N:
            if P[next_idx] == next:
                break
            next_idx += 1
        # 見つからなければ矛盾
        if next_idx == N:
            print(-1)
            return
        
        # 見つかった次の数字を持ってくる操作を行う。
        # 数字自体は、見つかった場所の一つ手前までが確定する。
        for i in range(next_idx, next-1, -1):
            P[i-1], P[i] = P[i], P[i-1]
            result.append(i)
        
        next = next_idx + 1
    
    # きちんと並び替わっているかどうかを確認
    if all(v == i for i, v in enumerate(P, start=1)):
        for r in result:
            print(r)
    else:
        print(-1)
        return

main()
