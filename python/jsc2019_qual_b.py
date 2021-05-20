# 第一回日本最強プログラマー学生選手権-予選- B - Kleene Inversion
# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b
# tag: 数列 転倒数 考察 MOD 数え上げ

# A の中の数 Ai を考える。
# 転倒数を求める、すなわち、各 Ai より大きな数が左側にいくつあるか ＆ 
# 小さな数が右側にいくつあるかの合計を求めよ、という問題である。

# K < 10^9 という制限から、真面目に一つ一つを計算しては間に合わないので、
# どうにかまとめて計算をしてやる必要がある。

# 仮に自分の左側にある大きな数だけを考えるとする。
# まず、今自分が含まれている A における、自分より左側の大きな数を数える。
# 加えて、自分より左側の A にある、自分より大きな数を全て数えることになる。
# 1 番目の A に含まれる Ai から K 番目の Ai までを順番に考えていく
# とすると、結果的に 0 ~ K-1 の合計、(K-1) * K // 2 個の A を
# 見ていくことになる。 
# 右側を見ていく場合も全く同様。
from collections import Counter
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    MOD = 10**9 + 7

    # A の中での転倒数を求める。内包表記を用いて
    # inv_a = sum(1 if A[i] > A[j] else 0 for i in range(N-1) for j in range(i, N))
    # みたいにも書けなくはない
    inv_a = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] > A[j]:
                inv_a += 1

    # それぞれの A の内側での転倒数を加える
    result = (inv_a * K) % MOD

    # それぞれの数が何回現れているのかをカウントしておく
    cnt = Counter(A)

    # A に含まれる Ai より大きな数や小さな数、つまり Ai と異なる数は
    # 全て (K-1) * K // 2 回数えられることになるので、まとめて
    # しまってもよい。ただし、小→大と大→小の2回数えられているので注意。

    # ある数が n 回現れるとして、(N - n) を n 回数えることになる
    rest = 0
    for n in cnt.values():
        rest += (N - n) * n

    mult = (K - 1) * K // 2

    result = (result + rest * mult // 2) % MOD
    print(result)

main()
