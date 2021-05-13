# CODE FESTIVAL 2017 qual C C - Inserting 'x'
# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_c
# tag: 文字列 回文

# 'x' 以外の文字を挿入できないので、元の文字列の 'x' 以外の
# 部分はあらかじめ回文になっている必要がある。

# なっていれば、各 'x' 以外の文字の間にいくつ 'x' が
# 入っているかをカウントし、それを左右合わせてやることで、
# 回文に変更できる。

# f.e.
# s = 'xabxa'
# 'x' 以外の文字、'a' 'b' を仕切りと考えるイメージ。
# 'b' を中央として、文字間の x の個数は
# 左から [1, 0] 個 'x'*1 + 'a' + 'x'*0 + 'b'
# 右から [0, 1] 個 'x'*0 + 'a' + 'x'*1 + 'b'
# これをどうにか合わせてやる……みたいな。

# 実装の際は、半分の地点で分けるのは面倒くさいので、
# 最後までリストを作り、逆にしたものと差分の絶対値を取り、
# 合計したものを2 で割ってやる。

# 上記の例で行くと、
# x の個数のリストを最後まで作成すると、
# ('x'*1 + 'a' + 'x'*0 + 'b' + 'x'*1 + 'a' + 'x'*0)
# より、[1, 0, 1, 0] となるので、
# [1, 0, 1, 0]
# [0, 1, 0, 1] - 上記のリストの逆順
#  1  1  1  1 - 差分（絶対値）
# この合計が 4 になる。
# が、ダブって計算しているので、半分に割る。

# 丁度真ん中に 'x' が来る場合は、そこの差分が 0 になるので
# 気にしなくてもいい。

def main():
    s = input()

    # 回分に変換可能かどうかを確認
    without_x = s.replace('x', '')
    if without_x != without_x[::-1]:
        print(-1)
        return

    # x の個数リストを作成
    x_seq = []
    x_cnt = 0
    for c in s:
        if c == 'x':
            x_cnt += 1
        else:
            x_seq.append(x_cnt)
            x_cnt = 0
    x_seq.append(x_cnt)

    # ひっくり返したものと差分を取り、合計する
    result = sum(abs(c1 - c2) for c1, c2 in zip(x_seq, x_seq[::-1]))

    # 実際の答えは、半分
    result //= 2
    print(result)

main()
