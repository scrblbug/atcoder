# AtCoder Beginner Contest 124 D - Handstand
# https://atcoder.jp/contests/abc124/tasks/abc124_d
# tag: 数列 範囲操作 反転 連続部分列 尺取法

# 最も効率のいい反転方法は、どこかしら連続する 0 を 1 に
# 書き換えるのを繰り返す手順である。

# なんとなくもっと効率がいい方法がありそうだが、1 を含む
# 連続部分列を反転した場合、結局そこを 0 に戻す反転を
# 行わなければならないため、最終的な効率は上記の方法と
# 同等になる。

# 例：
# 0101010 → 1101010 → 1111010 → 1111110 → 1111111
# 0101010 → 0100010 → 0111110 → 0000000 → 1111111

# となると、問題はやや簡単に置き換えることが可能。
# つまり、0 の連続する部分が K 個以内になる、
# 連続部分列の最長の長さを求めればいい。

# これは尺取法を用いて求めることが可能。
# あらかじめ itertools.groupby などを用いて
# 0 の連続列と 1 の連続列に分解しておくと楽ができる。

from itertools import groupby
def main():
    N, K = map(int, input().split())
    S = input()

    groups = [(item, len(list(group))) for item, group in groupby(S)]

    result = 0

    # ここから尺取法
    left, right = 0, 0

    # 0 の連続部分列の個数
    zero_seq = 0

    score = 0
    while right < len(groups):
        # 右を進めるだけ進める。
        while right < len(groups) and zero_seq + (groups[right][0] == '0') <= K:
            score += groups[right][1]
            zero_seq += groups[right][0] == '0'
            right += 1

        # 得点を評価。
        if score > result:
            result = score

        # 左を 1 個進める。
        score -= groups[left][1]
        zero_seq -= groups[left][0] == '0'
        left += 1
        # 条件より常に left <= right なので、
        # 追いついたときの処理は入れなくていい。

    print(result)

main()
