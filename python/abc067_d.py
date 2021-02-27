# AtCoder Beginner Contest 067 D - Fennec VS. Snuke
# https://atcoder.jp/contests/abc067/tasks/arc078_b
# tag: 対戦ゲーム グラフ 木 距離

# 結局のところ、各マスについてそれぞれ
# 黒初期マス 0, 白初期マス N-1 のどちらに近いかで、
# 塗られる色が決定される

from collections import deque
def main():
    N = int(input())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]

    # 面倒くさいので0-indexedに変換しておく
    paths = [[] for _ in range(N+1)]
    for a, b in path_dat:
        paths[a-1].append(b-1)
        paths[b-1].append(a-1)

    # BFSを2回で距離を出しておき、最後に比較スキャン
    # 初期黒マスからの、各マスへの距離を求める
    black = [-1] * N
    black[0] = 0

    queue = deque()
    queue.append((-1, 0))
    while queue:
        prev, now = queue.popleft()
        dist_now = black[now]
        for nxt in paths[now]:
            if black[nxt] != -1 or prev == nxt:
                continue
            black[nxt] = dist_now + 1
            queue.append((now, nxt))

    # 初期白マスからの、各マスへの距離を求める
    # 関数をまとめたほうが良かった？……ま、2回だしいっか
    white = [-1] * N
    white[N-1] = 0

    queue = deque()
    queue.append((-1, N-1))
    while queue:
        prev, now = queue.popleft()
        dist_now = white[now]
        for nxt in paths[now]:
            if white[nxt] != -1 or prev == nxt:
                continue
            white[nxt] = dist_now + 1
            queue.append((now, nxt))
    
    # 各マスごとに、どちらに塗られるかを判定しつつ、カウント
    # 黒先手なので、同じ距離なら黒になる
    black_cnt, white_cnt = 0, 0
    for i in range(N):
        if black[i] <= white[i]:
            black_cnt += 1
        else:
            white_cnt += 1
    
    # 黒先手なので、同数なら黒の手番が先に尽きて負けになるのを注意
    if black_cnt > white_cnt:
        print('Fennec')
    else:
        print('Snuke')

main()
