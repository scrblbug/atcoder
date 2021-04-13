# AtCoder Beginner Contest 198 E - Unique Color
# https://atcoder.jp/contests/abc198/tasks/abc198_e
# tag: グラフ 木 dfs

# 実は当初提出した回答では、色を set で管理し、
# dfs(prev, now, color_set) という感じで set のコピーを
# 引き渡していた。
# が、このやり方だと set が膨れ上がると TLE になる。
# （ダブってるのだけカウントする、というやり方で一応通りはした）

# 既出の色は一律で管理するようにし、木をたどるとともに
# 出し入れしていく、というやり方を取るのが正解だろう。
# その場合、set ではなく dict で数をカウントする形になる。

# 再帰回数の制限を解除しておくこと
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
def main():
    N = int(input())
    colors = list(map(int, input().split()))
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]

    # 0-indexed に変換しつつ、隣接リストを作成
    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        a -= 1
        b -= 1
        paths[a].append(b)
        paths[b].append(a)

    # 現在持っている色の管理
    color_cnt = defaultdict(int)

    result = []

    # 再帰関数
    def dfs(prev, now):
        # 現在の色が、持っている色になければ、結果に追加
        if color_cnt[colors[now]] == 0:
            # 結果に追加する際、1-indexed に戻す
            result.append(now+1)

        # 現在の色を持っている色に追加
        color_cnt[colors[now]] += 1

        # 各子について再帰
        for nxt in paths[now]:
            if nxt == prev:
                continue
            dfs(now, nxt)

        # 終わったら、さっき追加した色を削除しておく
        color_cnt[colors[now]] -= 1

    # スタート地点から開始
    # 親を存在しない値 (-1) にしておくといい。
    dfs(-1, 0)

    for r in sorted(result):
        print(r)

main()
