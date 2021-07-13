# AtCoder Beginner Contest 209 E - Shiritori
# https://atcoder.jp/contests/abc209/tasks/abc209_e
# tag: グラフ ゲーム 二人ゲーム 高橋君 青木くん

from collections import deque
def main():
    N = int(input())
    words = [input() for _ in range(N)]

    beg_dic = dict()

    # とりあえず頭3文字ごとに辞書で整理しておく
    for i, w in enumerate(words):
        beg = w[:3]
        if beg not in beg_dic:
            beg_dic[beg] = []
        beg_dic[beg].append(i)

    # グラフ構築、ついでに逆辺ももっておく
    paths = [[] for _ in range(N)]
    rev_paths = [[] for _ in range(N)]

    # 後のチェック用キュー
    check_queue = deque([])

    # 勝ち負け判定用変数
    win_lose = [0] * N

    for i, w in enumerate(words):
        end = w[-3:]

        # 移動可能な単語があるなら
        if end in beg_dic:
            for nxt in beg_dic[end]:
                # 辺と逆辺を追加
                paths[i].append(nxt)
                rev_paths[nxt].append(i)
        else:
            # 行き止まりなので、キューに保存しておく
            check_queue.append(i)

    # 行き止まりの集合からキューを開始する
    while check_queue:
        now = check_queue.pop()
        if win_lose[now] != 0:
            continue
        # 行き止まりチェック
        if paths[now] == []:
            win_lose[now] = -1
            for p in rev_paths[now]:
                check_queue.append(p)
            continue

        # 移動先に一個でも負けがある
        if any(win_lose[n] == -1 for n in paths[now]):
            win_lose[now] = 1
            for p in rev_paths[now]:
                check_queue.appendleft(p)
            continue

        # 移動先が全て勝ち
        if all(win_lose[n] == 1 for n in paths[now]):
            win_lose[now] = -1
            for p in rev_paths[now]:
                check_queue.append(p)
            continue

    for wl in win_lose:
        if wl == -1:
            print('Takahashi')
        elif wl == 1:
            print('Aoki')
        else:
            print('Draw')

main()
