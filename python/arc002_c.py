# AtCoder Regular Contest 002 C - コマンド入力
# https://atcoder.jp/contests/arc002/tasks/arc002_3
# tag: DP

# ショートカットの組み合わせを全探索する。
# 各ショートカットの組み合わせごとの最小入力回数は、
# DPを用いて求める。

# dpt[i]: i文字目までのコマンドを入力するための
# 最小ボタン入力回数、とおいてDPを行う。

# ショートカットを使用しない場合、
# dpt[i+1] = min(dpt[i+1], dpt[i]+1)

# ショートカットを使用する場合、
# dpt[i+2] = min(dpt[i+2], dpt[i]+1)

from itertools import combinations, product
def main():
    N = int(input())
    command = input()

    # ショートカットの組み合わせを作成しておく。
    # ここでは itertools.product を使用してみた。
    shortcuts = [''.join(sc) for sc in product('ABXY', 'ABXY')]

    result = 10**10
    # ショートカット 2個の組み合わせを全探索する。
    for sc1, sc2 in combinations(shortcuts, 2):
        # DPで最小入力回数を求める。
        dpt = [10**10] * (N+1)
        dpt[0] = 0

        for i in range(N):
            # ショートカットを使用しない場合。
            dpt[i+1] = min(dpt[i+1], dpt[i]+1)

            # ショートカットを使用する場合。
            if command[i:i+2] in [sc1, sc2]:
                dpt[i+2] = min(dpt[i+2], dpt[i]+1)
        
        if dpt[N] < result:
            result = dpt[N]

    print(result)

main()
