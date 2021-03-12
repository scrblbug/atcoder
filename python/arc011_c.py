# AtCoder Regular Contest 011 C - ダブレット
# https://atcoder.jp/contests/arc011/tasks/arc011_3
# tag: グラフ BFS

# 各単語を頂点とするグラフを作成する。
# 単語の組み合わせ毎に変換可能かどうかを確認し、
# 変換可能ならその単語間に辺を張る。
# グラフを構成後、BFSで first → last の最短経路を求めていく。

from collections import deque
def main():
    first, last = input().split()
    N = int(input())

    # first == last なら、答えを出力して終了
    if first == last:
        print(0)
        print(first)
        print(last)
        return

    # 単語のダブリはあらかじめ除いておく
    words = [input() for _ in range(N)]
    words.append(first)
    words.append(last)
    words = list(set(words))
    N = len(words)

    # {ノード番号: 各単語} の辞書を作っておく
    i_to_w = {i:w for i, w in enumerate(words)}

    # first / last のノード番号も調べておく
    for i, w in i_to_w.items():
        if w == first:
            first_index = i
        if w == last:
            last_index = i
    
    # 単語間が遷移可能かどうか、全組み合わせを探索しつつ
    # グラフを構成していく
    paths = [[] for _ in range(N)]
    for i in range(N-1):
        w1 = words[i]
        for j in range(i+1, N):
            w2 = words[j]
            # 違っている文字数を数え、一文字違いなら辺を張る
            diff = sum(1 if c1 != c2 else 0 for c1, c2 in zip(w1, w2))
            if diff == 1:
                paths[i].append(j)
                paths[j].append(i)
    
    # first ～ last の最短経路を算出していく
    # とりあえず BFS で first からの距離を全探索しておく
    dist = [-1] * N
    dist[first_index] = 0
    queue = deque([first_index])
    while queue:
        now = queue.popleft()
        for nxt in paths[now]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[now] + 1
            queue.append(nxt)

    # last までたどり着いていない場合は、-1 を出力して終了
    if dist[last_index] == -1:
        print(-1)
        return

    # 今度は last から常に距離を縮めるように first まで
    # 探索していき、経路を再現する
    route = [last_index]
    now = last_index
    while now != first_index:
        for nxt in paths[now]:
            if dist[now] > dist[nxt]:
                route.append(nxt)
                now = nxt
                break
    
    result = [i_to_w[i] for i in route[::-1]]
    print(len(result) - 2)
    for w in result:
        print(w)

main()


