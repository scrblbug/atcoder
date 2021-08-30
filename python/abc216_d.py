# AtCoder Beginner Contest 216 D - Pair of Balls
# https://atcoder.jp/contests/abc216/tasks/abc216_d
# tag: 愚直 グラフ トポロジカルソート

def main():
    N, M = map(int, input().split())
    tubes = []
    for _ in range(M):
        k = int(input())

        # pop() で処理しやすいように逆順にしておく。
        tubes.append(list(map(int, input().split()))[::-1])

    # 現在ペアになっている色。
    paired = []

    # 色別に取り出せる位置を管理。
    available = [[] for _ in range(N+1)]

    # 初回準備。
    for pos, colors in enumerate(tubes):
        if len(tubes) > 0:
            color = colors[-1]
            available[color].append(pos)
            if len(available[color]) == 2:
                paired.append(color)

    # 取り除いたボールの個数を数えておく。
    removed = 0

    # ここから具体的な操作のシミュレートを行う。
    while len(paired) > 0:
        # ペアに出来る色を取り出し、新たに現れる色を管理する。
        color = paired.pop()
        removed += 1
        for pos in available[color]:
            # 取り出し。
            tubes[pos].pop()
            if len(tubes[pos]) == 0:
                continue

            # まだボールがあるなら、available を更新する。
            new_color = tubes[pos][-1]
            available[new_color].append(pos)

            # 一番上に 2つあるなら、取り除くペアに追加。
            if len(available[new_color]) == 2:
                paired.append(new_color)

    if removed == N:
        print('Yes')
    else:
        print('No')

main()
