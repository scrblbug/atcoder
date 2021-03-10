# AtCoder Regular Contest 073 D - Simple Knapsack
# https://atcoder.jp/contests/arc073/tasks/arc073_b
# tag: ナップサック問題 DP

# 典型問題……かと思いきや、制限にひねりが加えられている。
# w の上限が 10^9 なので、そのままDPで実装するとダメ。
# ただし、w1 <= wi <= w1 + 3 という妙な制限になっているので、
# そこを利用した実装にしたい。

def main():
    N, W = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]

    w1 = items[0][0]

    # いろいろと書き方はあると思うけど……ここでは、
    # dpt[i][j]: i 個入れており、w1 * i より重い分が j の価値の最大値
    # みたいな感じで、配るDPで書いてみている

    # 最大入る可能性がある個数。これが最悪でも N 個なので、
    # 配列の最大サイズは 100 * 300
    # 全体での計算量は O(N^3) となっている。
    max_n = min(N, W // w1)

    dpt = [[-1] * (3 * N) for _ in range(max_n+1)]
    dpt[0][0] = 0

    for w, v in items:
        # i のループ方向に注意
        for i in range(max_n-1, -1, -1):
            for j in range(3 * N - 1):
                
                if dpt[i][j] == -1:
                    continue

                # 重さ制限を超える場合は、飛ばす
                w_now = w1 * i + j
                if w_now + w > W:
                    continue
                
                # 遷移
                rem = w - w1
                if dpt[i+1][j+rem] < dpt[i][j] + v:
                    dpt[i+1][j+rem] = dpt[i][j] + v

    # 回答時は全走査が必要
    result = max(max(row) for row in dpt)
    print(result)

main()
