# AtCoder Regular Contest 031 B - 埋め立て
# https://atcoder.jp/contests/arc031/tasks/arc031_2
# グリッド 連結 BFS DFS

# ひとマスずつそこを埋め立てて連結になるかどうかを
# 確認していく。

def main():
    field = [[c for c in input()] for _ in range(10)]
    
    # 与えられた地図を元に、陸地が全てつながっているか
    # どうかを確認する関数を作成しておく。
    def land_connectedp(field):
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        connection = 0
        visited = [[False] * 10 for _ in range(10)]

        # 探索開始地点をすべての場所から試す
        for sx in range(10):
            for sy in range(10):
                # 訪問済み、もしくは海ならスキップする
                if visited[sy][sx] or field[sy][sx] == 'x':
                    continue
                
                # 陸地が見つかったら、連結成分数のカウントを増やしつつ、
                # 繋がっている陸地を全て訪問済みにする。
                connection += 1
                queue = [(sx, sy)]
                visited[sy][sx] = True
                while queue:
                    x, y = queue.pop()
                    for dx, dy in moves:
                        tx, ty = x + dx, y + dy
                        if not (0 <= tx < 10 and 0 <= ty < 10):
                            continue
                        if visited[ty][tx] == False and field[ty][tx] == 'o':
                            visited[ty][tx] = True
                            queue.append((tx, ty))

        # 連結成分数が 1 なら、陸地は全て繋がっている。
        return connection == 1
    
    # 最初から繋がっていれば YES
    if land_connectedp(field):
        print('YES')
        return
    
    # 埋立地の場所を全探索する。
    for fx in range(10):
        for fy in range(10):
            # 陸ならスキップ。
            if field[fy][fx] == 'o':
                continue
            
            # 海なら埋め立て、つながるかどうか確認する。
            field[fy][fx] = 'o'
            if land_connectedp(field):
                print('YES')
                return
            field[fy][fx] = 'x'
    
    # 条件に合う埋立地が見つからなければ、NO
    print('NO')

main()




