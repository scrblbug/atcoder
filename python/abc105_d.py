# AtCoder Beginner Contest 105 D - Candy Distribution
# https://atcoder.jp/contests/abc105/tasks/abc105_d
# 累積和 MOD

# 初見だと、発想力が問われる問題。
# 累積和を取るまではいいとして、(l, r)を全探索すると間に合わない。
# 子どもたちに均等に配ることが出来るという条件を言い換えると、
# 子どもたちの人数 M で割って剰余が 0 になるとなる。
# つまり、累積和 R から累積和 L を引く場合、R と L の剰余が
# 等しい場合、条件を満たす。
# つまり、剰余が等しい l, r の組み合わせの数を計算する……
# ということになる。

def main():
    N, M = map(int, input().split())
    A = list(map (int, input().split()))

    # 累積和を作成
    csum = [0]
    for a in A:
        csum.append(csum[-1] + a)

    # 辞書を作成し、各剰余の数を格納していく。
    # （リストだと M が大きい場合問題になる）
    mod_cnt = dict()
    for s in csum:
        if s % M not in mod_cnt:
            mod_cnt[s % M] = 0
        mod_cnt[s % M] += 1

    # 各剰余の個数毎に、答えを足し合わせていく
    # n 個から2個選ぶ組み合わせの数なので、n(n-1)/2 個ずつ増える
    result = 0
    for cnt in mod_cnt.values():
        if cnt > 0:
            result += (cnt * (cnt - 1)) // 2

    print(result)

main()
