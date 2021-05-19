# AtCoder Beginner Contest 037 C - 総和
# https://atcoder.jp/contests/abc037/tasks/abc037_c
# tag: 考察 数列 連続部分列 総和 基礎問題

# 部分数列がずれていくイメージなので、
# 足す数字も少しずらしていけばいい、みたいな発想で……。
# 例：部分数列の移行が (1,2,3,4,5) → (2,3,4,5,6) の場合、
# 元の合計から 1 を引いて 6 を足したもの（を答えに足してやる）。

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 初回の部分数列の合計
    part_sum = sum(A[:K])

    # 最初だけ合計に入れ込んでおく
    result = part_sum

    for left in range(N-K):
        # 次の部分数列の合計を求め、足し合わせていく
        part_sum -= A[left]
        part_sum += A[left+K]
        result += part_sum

    print(result)

main()

# 別解
# それぞれの数字が足される回数を考えていく。
# N=9, K=3 で考えてみると、
# (1,2,3) (2,3,4) (3,4,5) (4,5,6) (5,6,7) (6,7,8) (7,8,9)
# 1～9はそれぞれ 1,2,3,3,3,3,3,2,1 回となり、
# 左端と右端から最大 K 回まで 1 ずつ増えていくことが分かる。

# ただし、K が十分に大きい場合、例えば
# N=5, K=4 などのときは (1,2,3,4) (2,3,4,5) となるため、
# 最大 N-K+1 回までしか足されない。

def main2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    for i, a in enumerate(A):
        # 左端から 1 ずつ増える（最大 K）
        from_left = min(K, i+1)

        # 右端から 1 ずつ増える（最大 K）
        from_right = min(N-i, K)

        # 上記の小さい方を掛けて、足す（最大 N-K+1)
        result += min(from_left, from_right, N-K+1) * a

    print(result)

# main2()
