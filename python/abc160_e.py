# AtCoder Beginner Contest 160 E - Red and Green Apples
# https://atcoder.jp/contests/abc160/tasks/abc160_e
# tag: 考察 事前ソート

# 食べられる可能性があるリンゴに注目すると、
# 赤色リンゴのうち上位 X 個は食べられる可能性がある。
# 緑色リンゴのうち上位 Y 個は食べられる可能性がある。

# この集合に、無色のリンゴを加えて美味しさ順にソートし、
# 上位 X+Y 個を食べれば最善になる。

def main():
    X, Y, A, B, C = map(int, input().split())
    reds = list(map(int, input().split()))
    greens = list(map(int, input().split()))
    others = list(map(int, input().split()))

    # 赤と緑を降順でソートしておく
    reds.sort(reverse=True)
    greens.sort(reverse=True)

    # 候補は、赤の上位 X 個と緑の上位 Y 個と無色全て
    candies = reds[:X] + greens[:Y] + others

    # 候補のリンゴを改めてソートし、上位 X+Y 個の合計を出力
    candies.sort(reverse=True)
    print(sum(candies[:X+Y]))

main()
