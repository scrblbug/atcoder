# AtCoder Regular Contest 118 B - Village of M People
# https://atcoder.jp/contests/arc118/tasks/arc118_b
# tag: 整数 分割 差分最少 ARC国

# max(|B/M - A/N|) を最少にしたい。

# とりあえず、各レーティングに対して floor(A * M / N) を
# 振り分ける。若干振り分ける人数が足りなくなるが、その残りを
# どのように振り分けるか。

# 上記振り分け後の厳密値（誤差 0 になる有理数人数）に対する誤差は、
# -1 より大きく 0 以下 に収まっている。
# 収まっている。つまり、余っている人数は K 人未満。

# 各レーティングごとの |B/M - A/N| （あるいは |N*B - M*A|）が
# 大きいものから順に、一人ずつ割り振ってやればいい。

import math
def main():
    K, N, M = map(int, input().split())
    ratings = list(map(int, input().split()))

    # 暫定振り分け
    result = [math.floor(M * a / N) for a in ratings]

    # 残り人数
    rem = M - sum(result)

    # 各レーティングごとの誤差をチェックし、ソート
    diff = [(abs(N * result[i] - M * ratings[i]), i) for i in range(K)]
    diff.sort(reverse=True)

    # 誤差が大きいところ（厳密値に対して人数がより足りないところ）に
    # 1 ずつ加えてやる
    for _, idx in diff[:rem]:
        result[idx] += 1

    # 回答を出力
    print(*result)

main()
