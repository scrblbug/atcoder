# AtCoder Beginners Contest 090 D - People on a Line
# https://atcoder.jp/contests/abc087/tasks/arc090_b
# tag: グラフ 連結成分 重み付きUnion-Find 典型問題

# 重み付きUnion-Findを用いると簡単に解ける典型問題。
# 使わずに解く場合は、人と位置をグラフで管理し、
# 条件が矛盾しないかどうかを確認しながら、各連結成分を
# 全探索していくことになる。

# 普通に解いていく場合
def main():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]

    # グラフを構築。paths[r][l] の場合コストを反転。
    paths = [dict() for _ in range(N)]
    for l, r, d in info:
        l -= 1
        r -= 1
        paths[l][r] = d
        paths[r][l] = -d

    INF = 10**10

    dist = [INF] * N

    result = 'Yes'

    # 連結成分ごとに全探索
    for start in range(N):
        if dist[start] != INF:
            continue
        
        # 連結成分ごとの探索開始
        # 探索開始時の距離は決め打ちで 0 としておく
        # 後々距離チェックを行うために、連結成分のノード情報も
        # 保存しておく(group)
        group = [start]
        dist[start] = 0
        queue = [start]
        while queue:
            now = queue.pop()
            d = dist[now]
            for nxt in paths[now]:
                nd = d + paths[now][nxt]
                if dist[nxt] != INF:
                    # 矛盾があればbreak
                    if nd != dist[nxt]:
                        result = 'No'
                        break
                    else:
                        continue
                else:
                    dist[nxt] = nd
                    queue.append(nxt)
                    group.append(nxt)
            # Pythonのfor ～ elseを利用した多重ループ脱出
            # なれると楽に書けるが慣れてないとちと分かりにくい
            else:
                continue
            break

        # 連結成分内で距離が長すぎないかどうかを確認
        group_d = [dist[i] for i in group]
        if max(group_d) - min(group_d) > 10**9:
            result = 'No'
            break
    print(result)

main()
