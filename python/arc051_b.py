# AtCoder Regular Contest 051 B - 互除法
# https://atcoder.jp/contests/arc051/tasks/arc051_b
# tag: ユークリッドの互除法 考察

# 問題の C++ を Python で書くとこんな感じだろうか。

# counter = 0
# def gcd(a, b):
#     global counter
#     if b == 0:
#         return a
#     counter += 1
#     return gcd(b, a % b)

# def main():
#     a, b = map(int, input().split())
#     gcd(a, b)
#     print(counter)

# 仮に 24 9 を入力したとすると、a, b, counter は
# 24, 9, 0
# 9, 6, 1
# 6, 3, 2
# 3, 0, 3
# と変化していき、3 が帰ってくる。

# さて、結論からいうと、
# 1, 0, K
# 2, 1, K-1
# 3, 2, K-2
# 5, 3, K-3
# ...
# という具合に遡っていってやればいい。

# 注意：
# 初期値を 1, 1 にすると、
# 1, 0, K
# 1, 1, K-1
# 2, 1, K-2
# となるが 2, 1 の次は本当は 1, 0 になるはずなので、
# きちんと動かない。

def main():
    K = int(input())

    a, b = 2, 1
    for k in range(K-1):
        a, b = a + b, a
    print(a, b)

main()
