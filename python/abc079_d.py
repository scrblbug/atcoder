# AtCoder Beginner Contest 079 D - Wall
# https://atcoder.jp/contests/abc079/tasks/abc079_d
# tag: グラフ 最小コスト ワーシャル・フロイド法 典型問題 joisinoお姉ちゃん

# 各数字間の変換コストが与えられているので、
# これを数字間に辺が張られたグラフと見なすと、
# ワーシャル・フロイド法によって全ての数字間の
# 変換の最小コストを求めることができる。

# これを用いて、愚直に壁に書かれた数字を 1 へと変換
# していき、合計コストを求めればいい。

def main():
    H, W = map(int, input().split())
    dist = [list(map(int, input().split())) for _ in range(10)]
    wall = [list(map(int, input().split())) for _ in range(H)]

    # ワーシャル・フロイド法で各数字間の最小コストを求めておく
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    result = 0

    # あとは壁の数字を順に見ていく
    for row in wall:
        # -1 でなければ、1 に変換していく
        for n in row:
            if n != -1:
                result += dist[n][1]

    print(result)

main()
