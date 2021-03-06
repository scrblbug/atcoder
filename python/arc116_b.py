# AtCoder Regular Contest 116 B - Products of Min-Max
# https://atcoder.jp/contests/arc116/tasks/arc116_b
# tag: 考察 数列 部分列 最大値 最小値 順列・組み合わせ 総和 MOD

# 1 <= N <= 2 * 10^5 の制約が厳しく、正直にそのまま実装するのは
# もちろんのこと、(L, R) を決めるような O(N^2) のやり方でも
# 時間切れになりそう。

# まず、そのままだと考察しづらいので A をソート済みとする。
# 仮に A = (1, 2, 3, 4, 5) のケースで考えてみると、
# 最小値 1 を固定した時、うまく計算できないだろうか？

# 合計されるのは、1 ~ それぞれの最大値の間に挟まる数が
# それぞれある場合、ない場合の 2 通りずつになるので、
# 最大値 1: 1 * 1 - 1回 （数字が 1 しか残っていないケース）
# 最大値 2: 1 * 2 - 1回 （数字が 1, 2 しか残っていないケース）
# 最大値 3: 1 * 3 - 2回 （1 ～ 3 の間の 2 が 残る／残らない ケース）
# 最大値 4: 1 * 4 - 2^2回 (1 ～ 4 の間の 2, 3 がそれぞれ 残る／残らない)
# 最大値 5: 1 * 5 - 2^3回 （1 ～ 5 の間の 2, 3, 4 が以下略）
# となる。

# 同様に最小値が 2 の場合を考えると、
# 最大値 2: 2 * 2 - 1回
# 最大値 3: 2 * 3 - 1回
# 最大値 4: 2 * 4 - 2回
# 最大値 5: 2 * 5 - 2^2回

# 数字が一つしか残らない場合を別に扱うと、
# 最小値 1 の場合：
# 1 * 1 + 1 * (2 * 1 + 3 * 2 + 4 * 2^2 + 5 * 2^3)
# 最小値 2 の場合：
# 2 * 2 + 2 * (3 * 1 + 4 * 2 + 5 * 2^2)
# 以下同様に、
# 3 * 3 + 3 * (4 * 1 + 5 * 2)
# 4 * 4 + 4 * (5 * 1)
# 5 * 5 + 5 * (0)

# ここで一番右のカッコ内に注目すると、
# 最小値が減るに従って、2 倍して前の最大値を足した値になっている
# これは O(1) で求められるので、全体でも O(N) でいけそう。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # まずは数列をソート
    A.sort()

    result = 0

    # 先に数字が一つしか残らないケースを加算しておく
    for i in range(N):
        result = (result + A[i] ** 2) % MOD

    # 最小値を右から 2 番目～最左端へと動かしつつ計算していく
    # 上記の右カッコ内を管理する変数を用意
    mult = 0
    for min_i in range(N-2, -1, -1):
        # 右カッコ内を更新
        mult = (mult * 2 + A[min_i+1]) % MOD
        # 値を計算して足していく
        result = (result + A[min_i] * mult) % MOD
    
    print(result)

main()
