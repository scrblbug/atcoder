# AtCoder Beginner Contest 165 C - Many Requirements
# https://atcoder.jp/contests/abc165/tasks/abc165_c
# tag: 数列 生成 DFS

# 結論から書くと、あり得る数列 A を全列挙して、
# 最大の得点のものを探す。

# ところで、実際のところ数列 A は最大何種類くらい
# あるのだろうか？
# それは、結局の所、1 ～ 10 の整数の中から、
# 重複ありで 10 個の整数を選ぶ通り数と等しくなる。

# これは 19! / (10! * 9!) 通りなので、
# 92378 通りに過ぎない。

# 上記の通り数は 9 個の仕切りで区切られた 10 個の領域に、
# 好きなように 10 個のボールを入れていく通り数……
# つまり、9 個の区別できない仕切りと
# 10 個の区別できないボールを、好きな順番に並べる通り数、
# という具合に考えると分かりやすい。

# また、さらに考察を進めると、得点を計算する際には
# 各項目の差のみが重要なので、A1 = 1 の場合のみを
# 考慮すればいい。
# （仮に A1 = n の数列の場合、全ての項目から (n-1) を引けば
# A1 = 1 の場合と同じ得点になるため）

# 数列の生成については、DFS などを用いて行う。
# 実際に生成を行う際は、途中結果も含めるために上の計算量よりは
# やや大きめとなるが、定数倍程度なので問題ない。

def main():
    N, M, Q = map(int, input().split())
    score_conds = [list(map(int, input().split())) for _ in range(Q)]

    result = 0

    # DFS で数列を生成しつつ、得点を計算していく。
    queue = [[1]]
    while queue:
        now = queue.pop()
        # 数列が完成したら、得点計算する。
        if len(now) == N:
            score = 0
            for a, b, c, d in score_conds:
                if now[b-1] - now[a-1] == c:
                    score += d
            if score > result:
                result = score
        # 数列が完成するまでは、伸ばしていく。
        else:
            minimum = now[-1]
            for nxt in range(minimum, M+1):
                queue.append(now + [nxt])

    print(result)

main()
