# 第二回全国統一プログラミング王決定戦予選 B - Counting of Trees
# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b
# tag: グラフ 木 特殊構造 順列・組み合わせ MOD

# 頂点 1 を中心として、距離ごとに木を広げていくイメージ。
# 一つ前の距離の頂点数を A 、今回の距離の頂点数を B とすると、
# A 種類のものを B 個選ぶので A^B 通りとなる。

from collections import Counter
def main():
    N = int(input())
    D = list(map(int, input().split()))
    MOD = 998244353

    # 距離 0 になるのは、頂点 1 のみでなければならない
    if D[0] != 0 or 0 in D[1:]:
        print(0)
        return

    # 距離ごとに枝の本数を数えておき、順次掛ける
    cnt = Counter(D)
    result = 1
    for i in range(1, max(D)+1):
        # 一応、あるはずの距離の枝が無ければ 0 を返して終了
        # いずれにせよ、あとから 0 の n 乗が掛かるので必須ではない。
        if cnt[i] == 0:
            print(0)
            return

        # pow(a, b, mod) で (a**b) % mod を高速に計算してくれる
        result = (result * pow(cnt[i-1], cnt[i], MOD)) % MOD

    print(result)

main()
