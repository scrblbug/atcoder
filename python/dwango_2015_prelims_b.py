# dwangoプログラミングコンテスト B - ニコニコ文字列
# https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_2
# tag: 文字列 正規表現 考察

# "252525..." と N 回 "25" が繰り返されている文字列から、
# 何回部分文字列が取り出せるかを考えてみる。
# "25" は N 回取り出せ、"2525" は N-1 回取り出せ……と
# 順に考えていくと、1 ～ N までの合計回数取り出せることになる。

# あとは、"2525..." をどうやって抽出するのか、という話。

# 真面目に実装すると意外と面倒くさい……
def main():
    S = input()+'0'

    # 2525の連続回数を保存しておくリスト
    seq = []

    # 2525を蓄えるバッファ
    buffer = ''

    for c in S:
        # バッファに文字を加える場合
        if c == '2' and not buffer.endswith('2'):
            buffer += '2'
        elif c == '5' and buffer.endswith('2'):
            buffer += '5'

        # バッファをクリアし、2525の数をseqに加える場合
        else:
            if len(buffer) >= 2:
                seq.append(len(buffer)//2)
            # この処理を忘れがち（個人的戒め）
            if c == '2':
                buffer = '2'
            else:
                buffer = ''

    # 後は連続回数に応じて計算する
    result = 0
    for n in seq:
        result += (n + 1) * n // 2
    
    print(result)

main()
