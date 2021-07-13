# AtCoder Beginner Contest 194 D - Journey
# https://atcoder.jp/contests/abc194/tasks/abc194_d
# tag: グラフ 確率 高橋君

# 1回あたりの確率 p の事象が初めて起こるまでの期待値を E とする。
# とりあえず 1回は試行する必要があるが、
# 1回試行した時に成功する場合と、失敗する場合に分けることができる。

# 成功：
# 起こる確率 = p, 追加で行われる回数の期待値 = 0

# 失敗：
# 起こる確率 = (1 - p), 追加で行われる回数の期待値 = E

# よって、
# E = 1 + p * 0 + (1 - p) * E
# E = 1 + E - pE
# pE = 1
# E = 1 / p

# さて、N 個の頂点のうち、a 個未訪問の頂点があると仮定する。
# 未訪問の頂点が選ばれる確率は a / N 。
# このとき、未訪問の頂点が 1個減るまでの期待値は N / a となる。

# この a を N-1 ～ 1 まで動かして合計したものが、期待値となる。

def main():
    N = int(input())
    result = 0.0

    for a in range(N-1, 0, -1):
        result += N / a

    print(result)

main()
