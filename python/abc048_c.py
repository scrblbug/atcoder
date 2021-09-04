# AtCoder Beginner Contest 048 C - Boxes and Candies
# https://atcoder.jp/contests/abc048/tasks/arc064_a
# tag: 貪欲法

# 左端から連続する2つをセットに順に見ていき、必要な数だけ
# 食べていく。ただし、セットのうちなるべく右側から食べる。

# という貪欲法で解ける。
# つまり、可能な限り次の操作が有利になるような食べ方を
# していく、ということ。

def main():
    N, x = map(int, input().split())
    candies = list(map(int, input().split()))

    result = 0

    for i in range(N-1):
        # 隣り合う 2個セットで確認する。
        former, latter = candies[i], candies[i+1]
        if former + latter <= x:
            continue

        must_eat = former + latter - x
        result += must_eat

        # なるべく右から食べる。
        if latter >= must_eat:
            candies[i+1] -= must_eat
        else:
            must_eat -= candies[i+1]
            candies[i+1] = 0
            candies[i] -= must_eat

    print(result)

main()



