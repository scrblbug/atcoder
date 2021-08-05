# AtCoder Regular Contest 031 B - 埋め立て
# https://atcoder.jp/contests/arc031/tasks/arc031_2
# グリッド 連結 BFS DFS

# ひとマスずつそこを埋め立てて連結になるかどうかを
# 確認していく。

def main():
    field = [[c=='o' for c in input()] for _ in range(10)]

    # 全部陸地なら YES
    if all(v==True for r in range(10) for v in field[r]):
        print('YES')
        return

    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # ひとマスずつ埋め立て地点を探索していく
    for fill_y in range(10):
        for fill_x in range(10):
            if field[fill_y][fill_x] == True:
                continue
            # 埋め立てる
            field[fill_y][fill_x] = True

            # 連結成分数を求める
            connect_n = 0
            visited = [[False] * 10 for _ in range(10)]

            # スタート位置を全探索 
            for y in range(10):
                for x in range(10):
                    # 訪問済みならスキップ
                    if visited[y][x]:
                        continue

                    # 陸地でなければスキップ
                    if field[y][x] == False:
                        continue

                    # 連結成分に +1 し、繋がっている陸地を訪問済みにする
                    visited[y][x] = True
                    connect_n += 1
                    queue = [(x, y)]
                    while queue:
                        x_now, y_now = queue.pop()
                        for dx, dy in moves:
                            x_nxt, y_nxt = x_now + dx, y_now + dy
                            if not (0 <= x_nxt < 10 and 0 <= y_nxt < 10):
                                continue
                            if visited[y_nxt][x_nxt]:
                                continue
                            if field[y_nxt][x_nxt] == True:
                                visited[y_nxt][x_nxt] = True
                                queue.append((x_nxt, y_nxt))

            # 連結成分数が 1 なら YES
            if connect_n == 1:
                print('YES')
                return

            # 埋め立てたものを元に戻す
            field[fill_y][fill_x] = False

    # 連結成分数が 1 になるものが見つからなければ、NO
    print('NO')

main()
