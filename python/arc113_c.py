# AtCoder Regular Contest 113 C - String Invasion
# https://atcoder.jp/contests/arc113/tasks/arc113_c
# tag: 考察

# aabbbbb → aaabbbb → .... → aaaaaaa
# という具合に、操作を繰り返すことで、同じ文字が二文字
# 連続する部分から右側の文字列が同じ文字で埋められることになる。

# aabbc という文字列の変化を考えると、
# aabbc → aaabc → aaaac → aaaaa
# という変化順よりは、
# aabbc → aabbb → aaabb → aaaab → aaaaa
# の方が回数が多くなることから分かるように、
# 右から文字列を順番に見て、二文字連続していればそこから
# 右端までを書き換える……という手順で行うことになる。

# と、ここまでの考察でも、右から見ていくやり方で解ける。
# このやり方は、最後におまけで。

# さらに考察を進めると、各文字はそれ以前に現れている
# 連続文字によって、それぞれ書き換えられることになる。
# f.e.
# aabbc → aabbb → aaabb → aaaab → aaaaa
# の時、最後の c は a, b によって上書きされ（2回）、
# b は a によって上書きされる（1回ずつ）

# ということは、前から順に見ていき、二文字連続があれば
# 書き換え回数を 1 増やし、以降の文字がその書き換え回数分
# 書き換わる、としてやればいい。

# また、文字が書き換えられない条件について考えると、

# 1) 一つ前の連続する二文字と同じ文字の場合(aabc"a"c)
# この場合は、書き換え回数を 1 回減らす

# 2) 連続する二文字が、前の連続二文字と同じ文字だった場合(aab"aa"c)
# この場合は、書き換え回数の更新を行わない

# 3) 同じ文字が連続三文字以上
# 書き換え回数を減らし、更新を行わない

def main():
    S = input()

    # 前の文字と、前の前の文字
    prev_c, prev2_c = "", ""

    # 一つ前に連続していた文字
    prev_seq = ""

    # 書き換え回数
    replace_n = 0

    result = 0
    for i in range(len(S)):
        # 同じ文字が二文字連続かつ、三文字連続でない）
        if S[i] == prev_c != prev2_c and S[i] != prev_seq:
            # 書き換え回数を増やす
            replace_n += 1
            # 連続文字を更新
            prev_seq = S[i]

        # 答えを書き換え回数分増やす
        result += replace_n

        # が、前の連続文字と同じ文字なら 1 減らす
        if S[i] == prev_seq:
            result -= 1

        # 文字情報を更新（忘れがち）
        prev2_c, prev_c = prev_c, S[i]

    print(result)

main()

# 以下は右端から見ていくやり方で解いた場合。
# 連続で書き換えている最中に、自分と同じ文字が
# 現れる場合、そこは書き換わらないのに注意。
# つまり、現れた文字をそれぞれカウントしながら、逆順に
# みていっている。
from collections import defaultdict
def main2():
    S = input()

    result = 0

    # 文字カウント。
    # 初めての文字が現れた時の処理を簡略にするよう、defaultdictで。
    cnt = defaultdict(int)

    # 前の文字と、前の前の文字
    prev_c, prev2_c = "", ""

    for i in range(len(S)-1, -1, -1):
        now_c = S[i]

        # 前と違う文字が二回連続で現れたら
        if now_c == prev_c != prev2_c:
            # そこから右がその文字に書き換えられるので、
            # 該当文字を除く文字数を答えに加算。
            result += (len(S) - i - 1) - cnt[now_c]
            # カウントは全て書き変わった文字になる
            cnt = defaultdict(int, {now_c: len(S) - i - 1})
        cnt[now_c] += 1
        prev2_c, prev_c = prev_c, now_c
    
    print(result)

# main2()
