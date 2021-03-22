# AtCoder Beginner Contest 026 C - 高橋君の給料
# https://atcoder.jp/contests/abc026/tasks/abc026_c
# tag: グラフ 木 再帰関数 

# 解き方はいろいろあると思うが、ここでは再帰関数を用いて解いている。
# 人数も少ないので、割と適当に書いてもどうにかなるだろう。

def main():
    N = int(input())
    path_dat = [int(input()) for _ in range(N-1)]

    # 1-indexed のままグラフを構成（どっちでもいいけど……）
    # グラフ～と聞くとややこしそうだが、各従業員ごとに
    # 直属の部下をリストにしているだけ。
    paths = [[] for _ in range(N+1)]
    for i, boss in enumerate(path_dat, start=2):
        paths[boss].append(i)

    # 再帰関数
    def get_payment(idx):
        # 部下がいないなら、給料は 1
        if paths[idx] == []:
            return 1

        # 部下がいるときは、部下の給料を取得してそこから計算
        staff_payments = [get_payment(p) for p in paths[idx]]
        return min(staff_payments) + max(staff_payments) + 1

    # 高橋君の給料を求める
    print(get_payment(1))

main()
