# AtCoder Beginnaer Contest 016 C - 友達の友達
# https://atcoder.jp/contests/abc016/tasks/abc016_3
# tag: グラフ 高橋君

# 1 <= N <= 10 なので何も考えずに探索したあと、
# 自分自身と友達を除いて出力する方針で……

def main():
    N, M = map(int, input().split())
    relations = [list(map(int, input().split())) for _ in range(M)]

    # 隣接リストでグラフ構築
    friends = [[] for _ in range(N+1)]
    for a, b in relations:
        friends[a].append(b)
        friends[b].append(a)

    # 友達の友達、つまりグラフ上で 2 回移動する先を全て求める。
    # 今回は制約も緩いので set でやってみることにしてみた。
    # いろいろやり方はあると思うが、今回の制約ならかなり効率の
    # 悪い判定でも、きちんと組めていれば十分間に合うだろう。
    for i in range(1, N+1):
        f_of_f = set()
        for f in friends[i]:
            f_of_f = f_of_f | set(friends[f])

        # 自分自身と友達は引いて数える（集合演算）
        excludes = {i} | set(friends[i])
        print(len(f_of_f - excludes))

main()
