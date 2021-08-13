# パナソニックプログラミングコンテスト2020 D - String Equivalence
# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d
# tag: 文字列 辞書順 生成 考察

# ある任意の文字列を、標準形に変換することを考える。
# zyxzx の場合を仮に考える。

# 辞書順最少なので、一文字目は必ず a。また、全ての z に a を当てる。
# zyxzx
# a##a#

# 二文字目の y は初めて現れる文字なので、b を当てる
# ab#a#

# 三文字目の x は初めて現れる文字なので、c を当てる
# abcac

# つまり、異なる文字が現れる場合は、必ず a, b, c の順に
# 当てていく必要があるということ。

# さて、ある標準形 S に一文字付け加えることを考えると、
# S + （Sに含まれる一文字） もしくは
# S + （新しい文字、但し辞書順最少）
# ということになる。

# 以上を踏まえて、文字数をどんどん伸ばしていく方針で組んでみる。

def main():
    N = int(input())

    ab = 'abcdefghijklmnopqrstuvwxyz'

    # [現在の文字のリスト, 次の文字（数値）] を保存していく。
    standards = [[[], 0]]

    # 手持ちの標準形から、新たに一文字多い標準形を生成していく
    for i in range(N):
        nxt_std = []
        for c_list, nxt in standards:
            # すでに使用している文字を付け加えたもの
            for j in range(nxt):
                nxt_std.append([c_list + [ab[j]], nxt])

            # 初めての文字を付け加えたもの
            nxt_std.append([c_list + [ab[nxt]], nxt+1])

        # 持っている標準形を更新
        standards = nxt_std

    # 自動的に辞書順になっている
    for c_list, _ in standards:
        print(''.join(c_list))

main()
