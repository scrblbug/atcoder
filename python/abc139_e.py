# AtCoder Beginner Contest 139 E - League
# https://atcoder.jp/contests/abc139/tasks/abc139_e
# tag: グラフ 閉路検出 典型問題 愚直

# 結局の所、試合同士の前後関係のみが問題となる。

# リーグ中、N 日目に行うべき試合を考えろ時には、N-1 日目までに、その前に行わなければならない
# 試合が全て終了しているような試合を行うようにすればいい。

# これは、実はグラフの BFS によるトポロジカルソートと
# 同じ動きとなる。

# すなわち、試合を頂点、試合の前後関係を有向辺と
# したときに、入辺がない頂点＝試合を行い、終わった頂点と
# そこからの出辺を全て取り除くという動作を繰り返す。

# 全ての頂点を取り除くまでの回数が試合の最短日数となり、
# また、すべての頂点を取り除けない場合は、そのグラフに
# 閉路が存在している＝前後関係が矛盾する試合が存在する
# ことになる。

# 実装の際には、ある頂点に対する入辺の数を管理しておき、
# 頂点と辺を取り除く動作を、次の頂点の入辺の数から 1 を引く
# ことで代用する。

from collections import deque
def main():
    N = int(input())
    match_dat = [list(map(int, input().split())) for _ in range(N)]

    # グラフ用隣接リスト
    paths = [[] for _ in range(N*(N-1))]

    # プレイヤー a とプレイヤー b の試合の前後関係をパスに変換
    for p_a, opponents in enumerate(match_dat):
        matches = []
        for p_b in opponents:
            # 0-indexed
            p_b -= 1

            # 試合を固有番号で管理するようにする
            match_id = min(p_a, p_b) * N + max(p_a, p_b)
            matches.append(match_id)

        for i in range(len(matches)-1):
            paths[matches[i]].append(matches[i+1])

    # 入辺数を管理
    edge_in = [0] * (N*(N-1))
    for nodes in paths:
        for nd in nodes:
            edge_in[nd] += 1

    # BFS によるトポロジカルソート
    # 開始する頂点を確認
    t_sorted = [nd for nd in range(N*(N-1)) if edge_in[nd]==0]

    queue = deque(t_sorted)

    # 頂点は入辺数が 0 になった時にのみ処理されるので、
    # 訪問済みかどうかを管理する必要はない
    while queue:
        now = queue.popleft()
        for nxt in paths[now]:
            edge_in[nxt] -= 1
            if edge_in[nxt] == 0:
                t_sorted.append(nxt)
                queue.append(nxt)

    # すべての頂点を訪れていなければ、-1 を返して終了
    if len(t_sorted) != N*(N-1):
        print(-1)
        return

    # トポロジカルソートされているので、前から順番に処理し
    # 試合ごとの開催日を求める
    n_day = [1] * (N*(N-1))
    for nd in t_sorted:
        for nxt in paths[nd]:
            n_day[nxt] = max(n_day[nxt], n_day[nd]+1)

    # トポロジカルソートで最後に来ているものが最後の試合
    print(n_day[t_sorted[-1]])

main()

# ……と汎用性の高い方法で解いてみたが、実は愚直に
# やっていっても解ける。

# 具体的には、試合を順番に見ていき、開催可能なもの、
# つまり、二人の選手が互いに先頭に相手を持っている
# ような組み合わせのみを開催していく。

# ただし、毎回全てのプレイヤーを調べていると TLE に
# なるので、二回目以降は相手が見つからなかったプレイヤーは
# 飛ばして調べる。

def main2():
    N = int(input())

    # 0-indexed
    matches = [[int(n) - 1 for n in input().split()] for _ in range(N)]

    matched = 0
    result = 0

    # プレイヤー毎に、次に表の何人目との試合待ちかを管理
    nxt_op = [0] * N

    # 開催可能な試合を持っている候補のプレイヤー
    candies = set(range(N))

    while matched < N*(N-1)//2:
        op_found = set()
        for p_a in candies:
            # 全試合消化済み
            if nxt_op[p_a] == N-1:
                continue
            
            # マッチング済み
            if p_a in op_found:
                continue
            
            # 次の試合予定
            p_b = matches[p_a][nxt_op[p_a]]

            # 次の試合予定相手の、次の試合予定相手が自分なら
            # マッチングを行う
            if matches[p_b][nxt_op[p_b]] == p_a:
                op_found.add(p_a)
                op_found.add(p_b)

        # マッチングが存在したら、処理を行う
        if op_found:
            result += 1
            matched += len(op_found) // 2
            candies = op_found
            for p in op_found:
                nxt_op[p] += 1
        # 全試合マッチング前に組めなくなったら -1
        else:
            print(-1)
            return

    print(result)

# main2()