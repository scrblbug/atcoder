# AtCoder Beginner Contest 110 C - String Transformation
# https://atcoder.jp/contests/abc110/tasks/abc110_c
# tag: 文字列 考察

# 文字列上の 2 つの文字が
# 1) 同じ文字の場合は、異なる文字に変えることが出来ず
# 2) 異なる文字の場合は、同じ文字に変えることが出来ない

# よって、各文字のある場所の対応が、S と T で
# 同一である必要がある。

# そこで、各文字列を頭から見ていき、
# その文字が初めて登場した場合は 0, 1, 2 と順に数字を当て、
# 既出の文字なら対応する数字を当てはめる数列を作成する。
# この数列が S と T で一致すれば、構造が一致している
# ことになる……という方針で。

def main():
    S = input()
    T = input()

    # 文字列 → 数列の関数
    def s_to_nlist(st):
        tmp = 0
        result = []

        # 文字 → 数字の対応辞書
        sn = dict()

        for c in st:
            # 初めての文字なら対応する数字を用意する
            if c not in sn:
                sn[c] = tmp
                tmp += 1
            # 対応する数字を数列に加える
            result.append(sn[c])
        return result

    # 生成された数列が同じなら 'Yes'
    if s_to_nlist(S) == s_to_nlist(T):
        print('Yes')
    else:
        print('No')

main()
