# AtCoder Beginner Contest 006 B - トリボナッチ数列
# https://atcoder.jp/contests/abc006/tasks/abc006_2
# tag: 基礎問題

# 特に悩むところの無い問題。変にメモなし再帰で解いたりして
# ハマったりしないように……。

def main():
    n = int(input())
    MOD = 10007

    tribo = [0, 0, 1]

    for _ in range(4, n+1):
        tribo.append((tribo[-1] + tribo[-2] + tribo[-3]) % MOD)

    print(tribo[n-1])

main()
