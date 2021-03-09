# AtCoder Regular Contest 073 D - Simple Knapsack
# https://atcoder.jp/contests/arc073/tasks/arc073_b
# tag: ナップサック問題 DP 累積和

# 典型問題……かと思いきや、制限にひねりが加えられている。
# w の上限が 10^9 なので、そのままDPで実装するとダメ。
# ただし、w1 <= wi <= w1 + 3 という妙な制限になっているので、
# そこを利用した実装にしたい。

def main():
    N, W = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]

    # いろいろと書き方はあると思うけど……ここでは、
    # 公式解説を参考に解いてみる。

    # 各品物の重さは w, w+1, w+2, w+3 の4種類しかない。
    # そこで、各重さごとにいくつ選ぶのかを全探索する。

    # あらかじめ品物を仕分けておく
    w1 = items[0][0]
    items_by_w = [[], [], [], []]
    for w, v in items:
        rem = w - w1
        items_by_w[rem].append(v)
    
    # 選ぶ時は価値の高いものから選んでいくので、
    # 各品物のリストをソート、ついでに累積和を取っておく
    csum_items_by_w = [[0], [0], [0], [0]]
    for i, item_list in enumerate(items_by_w):
        item_list.sort(reverse=True)
        tmp = 0
        for v in item_list:
            tmp += v
            csum_items_by_w[i].append(tmp)
    
    result = 0
    # 全探索の4重ループ
    for n0 in range(len(items_by_w[0]) + 1):
        for n1 in range(len(items_by_w[1]) + 1):
            for n2 in range(len(items_by_w[2]) + 1):
                for n3 in range(len(items_by_w[3]) + 1):
                    total_w = n0 * w1 + n1 * (w1+1) + n2 * (w1+2) + n3 * (w1+3)
                    if total_w > W:
                        continue
                    total_v = csum_items_by_w[0][n0] + csum_items_by_w[1][n1] + \
                              csum_items_by_w[2][n2] + csum_items_by_w[3][n3]
                    if result < total_v:
                        result = total_v
    print(result)

main()



