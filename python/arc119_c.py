# AtCoder Regular Contest 119 C - ARC Wrecker 2
# https://atcoder.jp/contests/arc119/tasks/arc119_c
# tag: 範囲クエリ 累積和 順列・組み合わせ AtCoder街道 ARC解体業者 高橋君

# ある範囲のビルの高さが、
# [a, b, c, d] とする。
# 左端の a は (a, b) の組み合わせでしか下げられないので、
# [0, b-a, c, d] とするしか無い。同様に続けていくと
# [0, 0, c-(b-a), d]
# [0, 0, 0, d-(c-(b-a))]
# この時、右端の d-(c-(b-a))、つまり d-c+b-a が 0 と
# なっていれば、ビルを全て高さ 0 にすることができる。

# さて、一種の累積和を取ってみる。
# [0, a, a-b, a-b+c, a-b+c-d, a-b+c-d+e.....]
# ここで、同じ数字が現れているところを両端とする範囲は、
# 上記の条件を満たす。
# 具体的に例を考えると、
# a-b = a-b+c-d+e であるとき、両辺から a-b を引くと
# c-d+e = 0 となるので、c ~ e、つまり (3, 5) の範囲で
# 条件を満たすことになる。

# というわけで、0, a, a-b, a-b+c... といったものを
# 計算し、各数値が現れる回数を数えれば、条件を満たす
# 通り数を決定できる。

from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 0, A[0], A[0]-A[1], A[0]-A[1]+A[2]...
    # において、各数字がどれくらいの回数現れるかをカウント。
    tmp = 0
    cnt = Counter()
    cnt[0] = 1
    for i, a in enumerate(A):
        if i % 2 == 0:
            tmp += a
        else:
            tmp -= a
        cnt[tmp] += 1

    # 同じ数字が n 回現れていれば、そこを範囲の両端とできる。
    # その通り数は n C 2 = (n * (n-1)) // 2
    result = 0
    for n in cnt.values():
        result += (n * (n-1)) // 2

    print(result)

main()
