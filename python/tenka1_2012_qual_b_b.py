# 天下一プログラマーコンテスト2012 予選B B - Camel_Case
# https://atcoder.jp/contests/tenka1-2012-qualB/tasks/tenka1_2012_6
# tag: 文字列

def main():
    S = input()

    AB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ab = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    # 文字列がアンダースコアのみの場合、そのまま出力して終了
    if all(c=='_' for c in S):
        print(S)
        return

    # 最初と最後のアンダースコアの数を数える
    begin_us = 0
    end_us = 0
    for i in range(len(S)):
        if S[i] == '_':
            begin_us += 1
        else:
            break
    for i in range(len(S)-1, -1, -1):
        if S[i] == '_':
            end_us += 1
        else:
            break

    words = S.strip('_').split('_')

    # 分割されていない＝途中に _ が無ければキャメルケースの疑い濃厚
    if len(words) == 1:
        # 数字か大文字から開始してたら、分類不能でそのまま出力
        if words[0][0] in AB+digits:
            print(S)
            return

        # 大文字で分割していく
        camels = []
        tmp = ''
        for c in words[0]:
            if c in AB:
                camels.append(tmp.lower())
                tmp = c
            elif c in ab + digits:
                tmp += c
            # 大文字小文字数字以外が出たら分類不能
            else:
                print(S)
                return
        camels.append(tmp.lower())

        print('_' * begin_us + '_'.join(camels) + '_' * end_us)

    # 分割されていればスネークの疑い濃厚
    else:
        snakes = ''
        for i, word in enumerate(words):
            # 空文字列、もしくは数字から始まっていたら分類不能
            if word == '' or word[0] in digits:
                print(S)
                return
            # 小文字と数字以外が入っていたら分類不能
            if not all(c in ab+digits for c in word):
                print(S)
                return
            if i != 0:
                snakes += word[0].upper() + word[1:]
            else:
                snakes += word

        print('_' * begin_us + snakes + '_' * end_us)

main()
