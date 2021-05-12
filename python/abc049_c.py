# AtCoder Beginner Contest 049 C - 白昼夢
# https://atcoder.jp/contests/abc049/tasks/arc065_a
# tag: 文字列 考察

# 文字列の途中の 'eraser' は、これで必ずひとまとまりになる。
# 'eraser' を除いた後の 'erase' はひとまとまり。
# 残りの 'dream' / 'dreamer' は、まず
# 'dreamer' を確定させて、最後に 'dream' が確定。

# というわけで、順番に各要素を空文字列に置き換えていき、
# 文字列全体が最終的に空文字列になるなら、
# 問題の条件を満たしていることになる。

def main():
    S = input()

    # eraser, erase, dreamer, dream の順に消していく
    S = S.replace('eraser', '')
    S = S.replace('erase', '')
    S = S.replace('dreamer', '')
    S = S.replace('dream', '')
    if S == '':
        print('YES')
    else:
        print('NO')

main()
