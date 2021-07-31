# AtCoder Grand Contest 034 B - ABC
# https://atcoder.jp/contests/agc034/tasks/agc034_b
# tag: 文字列 置換 最大値 事前操作 正規表現

# 'ABC' を 'BCA' に書き換えるとき、'BC' の並びは変更されない。
# そこで、とりあえず 'BC' を 'D' と書き換えてから考える。

# 文字列全体は、'B' もしくは 'C' によって分割された、
# 'A' 'D' の組み合わせによる文字列と考えられる。
# 'A'と'D'は交換可能だが、'B' 'C' の壁を越えることは出来ない。
# 例えば入力例3 だと、
# ADA C C B ADDAAD B
# となり、この ADA と ADDAAD を考慮することになる。

# それぞれの塊を、DD..DAA...A という状態になるまで
# 操作すれば、それが最大の回数となる。

import re
def main():
    S = input()
    S = S.replace('BC', 'D')

    # 正規表現を用いて AD のグループを探す
    groups = re.findall(r'[AD]+', S)

    result = 0

    for g in groups:
        # 'D' を順番に数えつつ探し、左端に持っていくための
        # 操作回数を足していく
        cnt_d = 0
        for idx, c in enumerate(g, start=1):
            if c == 'D':
                cnt_d += 1
                result += idx - cnt_d
    
    print(result)

main()
