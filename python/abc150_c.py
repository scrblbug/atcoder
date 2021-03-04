# AtCoder Beginner Contest 150 C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c
# tag: 順列組み合わせ作成 辞書順

# 順列を全通り作成し、P, Q それぞれが何番目にあるか確認する。
# ソートしてインデックスを取ってもいいが、確認するのが2つだけ
# なので、それぞれより下にいくつあるかを確認するほうが速い。

# 順列の作成については、itertool.permutations を使用してもいいが、
# せっかくなので再帰で書いてみることにする。

# たぶん、もっと良い書き方があるとは思う
def get_next_permutate(now, remaining_set):
    if remaining_set:
        for n in remaining_set:
            yield from get_next_permutate(now + [n], remaining_set - set([n]))
    else:
        yield now

def main():
    N = int (input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # もちろん↓の方が楽かつ速い
    # patterns = list(itertools.permutations(range(1, N+1), N))
    # itertools ではtupleが帰ってくるので、少しだけ注意。
    patterns = list(get_next_permutate([], set(range(1, N+1))))

    prev_p = 0
    prev_q = 0
    for p in patterns:
        if p < P:
            prev_p += 1
        if p < Q:
            prev_q += 1

    print(abs(prev_p - prev_q))

main()
