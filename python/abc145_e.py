# AtCoder Beginner Contest 145 E - All-you-can-eat
# https://atcoder.jp/contests/abc145/tasks/abc145_e
# tag: DP 高橋君

# ナップサックの要領でそのまま DP で解こうとすると、
# 実は最後に何を食べるかで最大効率が変わってくるため、
# WA になってしまう。

# ところで、最後に食べるものは、食べると決定したものの中で
# もっとも時間がかかる料理として問題無い。
# 仮に他の料理が最後に来ていたとしても、もっとも時間がかかる
# ものと入れ替え可能なため。

# ということは、あらかじめ料理を掛かる時間順にソートしておき、
# あとは通常通り DP を回せばいい。

def main():
    N, T = map(int, input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]

    # 料理を食べるのに掛かる時間順にソート
    foods.sort()

    # ナップサック DP に近い感じで……
    dpt = [[0] * (T+1) for _ in range(N+1)]
    for i, (cost, value) in enumerate(foods):

        # 食べ始めは 0 ～ T-1 の範囲
        for j in range(T):
            # 食べ終わる時間は T で丸めてやる
            nxt_cost = min(T, j+cost)

            # あとは通常通り更新
            dpt[i+1][j] = max(dpt[i+1][j], dpt[i][j])
            dpt[i+1][nxt_cost] = max(dpt[i+1][nxt_cost], dpt[i][j] + value)

        # 時間 T の最大値は前の値のみを参考して更新
        dpt[i+1][-1] = max(dpt[i+1][-1], dpt[i][-1])

    print(dpt[-1][-1])

main()
