# Atcoder Beginner contest 006 C - スフィンクスのなぞなぞ
# https://atcoder.jp/contests/abc006/tasks/abc006_3
# tag: 考察

# 大人、老人、 赤ちゃんの人数をそれぞれ
# a, b, c とする。
# 人数の関係より
# a + b = N - c
# よって、
# 2a + 2b = 2(N - c)

# 足の本数の関係より
# 2a + 3b = M - 4c

# 以上から、
# b = (M - 4c) - 2(N - c)
#   = M - 2N - 2c

# なので、
# a + b = N - c より
# a = N - c - (M - 2N - 2c)
#   = 3N - M + c

# というわけで、c を全探索しつつこれらを求め、
# a >= 0, b >= 0 となるものが見つかればそれが答え。

def main():
    N, M = map(int, input().split())

    # 考察に基づき、c を全探索。
    for c in range(N+1):
        b = M - 2*N - 2*c
        a = 3*N - M + c
        if a >= 0 and b >= 0:
            print(a, b, c)
            return

    # 回答が見つからなければ、-1 を出力。
    else:
        print(-1, -1, -1)

main()
