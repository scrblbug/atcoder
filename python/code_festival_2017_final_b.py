# CODE FESTIVAL 2017 Final B - Palindrome-phobia
# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b
# tag: 文字列 回文 連続部分列 考察 すぬけ君

# a, b, c の3文字で、条件を満たす文字列はどのようなものか考える。
# まず、同じ文字が aa, bb のように連続すると、回文なのでNG。
# 必然的に違う文字を並べることになるが、
# aba などのように1文字目と3文字目が同じものもNG
# 必然的に、abc, acb などのようにすべて違う文字が並ぶ必要がある。
# また、3文字目までの並びが決定すると、自動的に次の文字が決定される。
# すなわち、abcabcabc... といった繰り返し構造である必要がある。

# この条件を満たすためには、各文字の数の差が 1 以内であることが
# 必要十分となる。

def main():
    S = input()

    cnt = {'a':0, 'b':0, 'c':0}
    for c in S:
        cnt[c] += 1

    if max(cnt.values()) - min(cnt.values()) <= 1:
        print('YES')
    else:
        print('NO')

main()
