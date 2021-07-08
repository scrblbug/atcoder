# AtCoder Beginner Contest 152 D - Handstand 2
# https://atcoder.jp/contests/abc152/tasks/abc152_d
# tag: 整数 順列・組み合わせ 数え上げ

# 先頭が top、末尾が bottom の数が、N 以下に
# いくつあるのかを数えられればいい。

# 1 <= N <= 200000 なので、これを全探索しつつ
# 数え上げておく。

# あとは (top, bottom) の数と (bottom, top) の数を
# 掛けたものを、全ての top, bottom に対して足したものが
# 組み合わせ数になる。

def main():
    N = int(input())

    # カウンタ初期化
    cnt = dict()
    for top in range(10):
        for bottom in range(10):
            cnt[(top, bottom)] = 0

    # 全ての cnt[(top, bottom)] の数を数えておく
    for i in range(1, N+1):
        top = int(str(i)[0])
        bottom = int(str(i)[-1])
        cnt[(top, bottom)] += 1

    result = 0

    # 全ての (top, bottom) に対して、
    # cnt[(top, bottom)] * cnt[(bottom, top)] を
    # 足し合わせる
    for top in range(10):
        for bottom in range(10):
            result += cnt[(top, bottom)] * cnt[(bottom, top)]

    print(result)

main()
