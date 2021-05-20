# AtCoder Regular Contest 080 D - Grid Coloring
# https://atcoder.jp/contests/arc080/tasks/arc080_b
# tag: グリッド 特殊構造 構築

# 同じ色なら全て繋がっている必要がある ＝ 繋がってさえいれば形は問わない
# グリッド全体をひと筆書きできるような経路があれば、
# 一筆書きの各分割区間は連結しているとみなせるので、
# そこに各色を求められる数だけ順番に置いていけばいい。

# たぶん一番簡単で例外がないのが、
# 123
# 654
# 789
# みたいな経路。

# ↑を簡単に作るにはどうしよう……
# 123
# 456
# 789
# みたいに普通に並べてから、一行おきにひっくり返せばいいのでは？

def main():
    H, W = map(int, input().split())
    N = int(input())
    n_by_color = list(map(int, input().split()))

    # とりあえずひとつなぎの配列を作成し、後から整形する
    seq = []
    for c, n in enumerate(n_by_color, start=1):
        for i in range(n):
            seq.append(c)

    # 先程作ったものを、W ごとに H 個に分割しつつ……
    for h in range(H):
        row = seq[h*W:h*W+W]

        # 一行おきにひっくり返しながら出力する
        if h % 2 == 0:
            print(*row)
        else:
            print(*row[::-1])

main()
