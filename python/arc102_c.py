# AtCoder Regular Contest 102 C - Triangular Relationship
# https://atcoder.jp/contests/arc102/tasks/arc102_a
# tag: 考察

# a + b, b + c, c + a が全て K の倍数ということは、
# 全て足して 2 * (a + b + c) も K の倍数
# ということは、2 * (a + b) を引いて
# 2c も K の倍数
# 同様に、2a, 2b も K の倍数である必要がある。

# a, b, c が全て K の倍数である場合は自明。

# a = K/2 (mod K) の時には、問題の定義より
# b, c も K/2 (mod K) である必要がある。

def main():
    N, K = map(int, input().split())

    result = 0

    # a, b, c が全て K の倍数の場合
    num_K_mult = N // K
    result += num_K_mult ** 3

    # a, b, c が K/2 (mod K) になれる場合
    if K % 2 == 0:
        k_half = K // 2

        # N < k_half の時はちゃんと 0 になる
        num_k_half = (N - k_half) // K + 1

        result += num_k_half**3

    print(result)

main()
