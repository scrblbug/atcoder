# AtCoder Beginner Contest 036 C - 座圧
# https://atcoder.jp/contests/abc036/tasks/abc036_c
# tag: 座標圧縮 基礎問題 すぬけ君

# 座標圧縮に関する基礎問題。
# 辞書まで作成してやるのが簡単だと思う。

def main():
    N = int(input())
    pressures = [int(input()) for _ in range(N)]

    # set.sort() は出来ないが、sorted(set) は可能
    pr_set = sorted(set(pressures))

    # {元の値: 圧縮後の値} で辞書を作成
    comp_dic = {k:v for v, k in enumerate(pr_set)}

    # 変換しつつ出力
    for p in pressures:
        print(comp_dic[p])

main()
