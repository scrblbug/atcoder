# CODE FESTIVAL 2016 qual A C - 次のアルファベット
# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c
# tag: 文字列 変換 辞書順 高橋君

# 各文字を変換する際には、
# 1) a に変換可能なら、変換する
# 2) a に変換できないなら、変換しないほうがいい
# ということを踏まえて組んでいく

def main():
    s = input()
    K = int(input())

    # とりあえず 0 ～ 25 と A ～ Z を相互変換しやすくしておく
    # ord と chr を使ってもいいけど、好みで……
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    num_to_ab = {k:v for k, v in zip(range(26), alphabets)}
    ab_to_num = {k:v for v, k in num_to_ab.items()}

    rest = K

    # 数字に変換しておく
    ch_list = [ab_to_num[c] for c in s]

    # 文字を順番に見ていき、'a' に変換可能なら変換する
    for i, n in enumerate(ch_list):
        # 文字列の最後なら、余っている操作回数を全て使用する
        if i == len(ch_list) - 1:
            ch_list[i] = (ch_list[i] + rest) % 26
            break

        # 元々 'a' なら変換しない
        if n == 0:
            continue

        # 'a' に変換可能な操作回数が残っていれば、変換する
        if n + rest > 25:
            rest -= 26 - n
            ch_list[i] = 0

    print(''.join(num_to_ab[n] for n in ch_list))

main()
