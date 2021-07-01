# AtCoder Regular Contest 020 B - 縞模様
# https://atcoder.jp/contests/arc020/tasks/arc020_2
# tag: 数列 書き換え 最小回数 コーナーケース 考察 高橋君

# 縞模様になる必要がある＝偶数番目は全て同じ色、奇数番目も
# 全て同じ色、偶数番目と奇数番目は違う色

# 全体で書き換えずに残しておく枚数を最大化したいと考える。
# つまり、偶数番目と奇数番目で、それぞれ一番多い枚数のものを
# そのままにしておくのが理想……

# だが、偶数番目と奇数番目それぞれで一番多い枚数の色が、
# 一致していることがある。
# その場合は、二番目に多い色も含めて考慮する必要がある。

# ……が、そもそもそれぞれが一色しか無いときもあったり。
# このあたりを上手く実装していく。

from collections import Counter
def main():
    n, c = map(int, input().split())
    colors = [int(input()) for _ in range(n)]

    odds = colors[::2]
    evens = colors[1::2]

    # 偶数番目の色と枚数を確認し、枚数が多い順にソート
    # 2位が必ず存在するようにするため、(0, 0) を加えておく
    odd_cnt = list(Counter(odds).items()) + [(0, 0)]
    odd_cnt.sort(key=lambda x:x[1], reverse=True)

    # 奇数番目も同様
    even_cnt = list(Counter(evens).items()) + [(0, 0)]
    even_cnt.sort(key=lambda x:x[1], reverse=True)

    # 偶数番目、奇数番目の全体の枚数
    odd_num = (n+1)//2
    even_num = n // 2

    # 偶数番目で一番多いものと、奇数番目で一番多いものの色が
    # 不一致ならば、それを残しておく色に採用する。
    if odd_cnt[0][0] != even_cnt[0][0]:
        p_odd = odd_num - odd_cnt[0][1]
        p_even = even_num - even_cnt[0][1]
        result = (p_odd + p_even) * c

    # そうでなければ、どちらかで二番目に多い色を採用すればいい
    else:
        p1_odd = odd_num - odd_cnt[0][1]
        p2_odd = odd_num - odd_cnt[1][1]
        p1_even = even_num - even_cnt[0][1]
        p2_even = even_num - even_cnt[1][1]
        result = min(p1_odd + p2_even, p2_odd + p1_even) * c

    print(result)

main()
