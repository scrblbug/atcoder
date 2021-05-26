# AtCoder Regular Contest 114 B - Special Subsets
# https://atcoder.jp/contests/arc114/tasks/arc114_b
# tag: グラフ 閉路 MOD

# 条件を満たすのはどのような場合かを考えると、

# 1 → 1 など自分自身になるもの。
# 1 → 2 → 3 → 1 などのようにループしているもの。
# 上記のものを（自由に）組み合わせたもの。

# といった感じ。

# つまりは、f(a) = b としたとき、
# a から b へと辺を張ったグラフとみなし、
# そのグラフに閉路がいくつ存在しているかを
# 数えてやればいい。

# 答えは、それぞれの閉路を入れる or 入れないパターンがあるので
# 2^(閉路の数) - 1 （空集合を引く）
# となる。

def main():
    N = int(input())
    func = list(map(int, input().split()))
    MOD = 998244353

    visited = [-1] * N

    # 閉路の数を数える
    loop_n = 0

    # start: 今回の探索開始地点
    # visited: 探索開始地点を保存していく。-1 は未訪問
    for start in range(N):
        # start が訪問済みなら飛ばす
        if visited[start] != -1:
            continue

        # ノードを順にたどっていく
        now = start
        while True:
            visited[now] = start
            nxt = func[now] - 1

            # 次のノードが、今回と同じ探索開始地点なら閉路となっている。
            # 1 → 2 → 3 → 2 のような合流付きのケースもあるが、
            # 閉路の数さえ数えればいいので気にしない。
            if visited[nxt] == start:
                loop_n += 1
                break

            # そうでない場合は、閉路は増えない。
            # 具体的には他の経路への合流となる。
            elif visited[nxt] != -1:
                break

            # 未訪問なら次のノードへ移動
            else:
                now = nxt

    # 答えは 2^(閉路の数) - 1 となる
    print((pow(2, loop_n, MOD) - 1) % MOD)

main()
