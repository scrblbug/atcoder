# deque を使用せず、次回探索用のリストを作成し、
# 切り替えていく方式でも解ける。ついでに番兵法も用いてみた。
def main():
    H, W = map(int, input().split())

    # 番兵を置いておく。
    # pythonは list[-1] で最後尾になるので、
    # 置くのは一つだけでいい。
    field = [[c for c in input()] + ['#'] for _ in range(H)]
    field.append(['#'] * (W+1))

    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 初回のキューの作成
    queue = []
    for y in range(H):
        for x in range(W):
            if field[y][x] == '#':
                queue.append((x, y))

    result = 0

    # ここから探索。
    while True:
        new_queue = []
        for x, y in queue:
            for dx, dy in moves:
                tx, ty = x + dx, y + dy
                if field[ty][tx] == '.':
                    field[ty][tx] = '#'
                    new_queue.append((tx, ty))

        # キューの更新。
        queue = new_queue

        if len(queue) > 0:
            result += 1
        else:
            break

    print(result)

main()
