# AtCoder Beginner Contest 088 D - Grid Repainting
# https://atcoder.jp/contests/abc088/tasks/abc088_d
# tag: グリッド BFS 典型問題 すぬけ君 一人ゲーム

# 最短手数で (1, 1) から (H, W) までたどり着くルートを見つけ、
# その時通ったマス以外を全て黒に塗ったときが答え。
# BFS で最短距離を求めればいい。

from collections import deque
def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    dist = [[0] * W for _ in range(H)]

    # すでにある黒マスの数を数えておく
    n_black = sum(row.count('#') for row in field)

    # インデックスを合わせて、スタートは (0, 0)
    # ゴールは (W-1, H-1) としておく
    # グリッドをBFSで全探索しつつ、スタートからの
    # 歩数を求めていく
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque([(0, 0)])
    while queue:
        # 左から次の地点を取得(BFS)
        x_now, y_now = queue.popleft()
        dist_now = dist[y_now][x_now]

        # 次の地点を見ていく
        for dx, dy in moves:
            x_nxt, y_nxt = x_now + dx, y_now + dy
            # 範囲外ならスキップ
            if not (0 <= x_nxt < W and 0 <= y_nxt < H):
                continue
            # 壁 or 探索済みならスキップ
            if field[y_nxt][x_nxt] == '#' or dist[y_nxt][x_nxt] != 0:
                continue
            # 次の地点の距離を現在地 +1 に確定し、探索キューに入れる
            dist[y_nxt][x_nxt] = dist_now + 1
            queue.append((x_nxt, y_nxt))

    # ゴールにたどり着けない場合
    if dist[H-1][W-1] == 0:
        print(-1)

    # ゴールまでの歩数 + 1 マスの白マスが必要
    # 残りを全て黒マスにする（もともと黒マスのところはそのまま）
    else:
        print((H * W) - dist[H-1][W-1] - 1 - n_black)

main()

