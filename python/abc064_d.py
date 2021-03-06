# AtCoder Beginner Contest D - Insertion
# https://atcoder.jp/contests/abc064/tasks/abc064_d
# tag: 文字列 括弧列 考察

# 与えられた文字列に対して、'(' を左端に、')' を右端に
# 適切な数追加することで、あらゆる括弧列を正しいものに
# できる。

# '(' をいくつ追加するかについて考えると、
# 左端から見ていった際に、')' が '(' より最大に過剰に
# なっている分だけ追加してやる必要がある。

# f.e.
# S = ')))())((' の場合
#   )  )  )  (  )  )  (  (
#   1  2  3  2  3  4  3  2
# 最大 4 個の ')' が '(' より多くなっているので、
# 左端に '(' を 4 個追加しなければならない。

# 今度は右から数えてみる
#   )  )  )  (  )  )  (  (
#  -2 -1  0  1  0  1  2  1
# 最大 2 個の '(' が ')' より多くなっているので、
# 右端に ')' を 2 個追加しなければならない。

# 以上より、完成形は
# "((((" + ")))())((" +  "))"

def main():
    N = int(input())
    S = input()

    # 左端から文字列を見ていき、')' が最大に
    # 過剰になっている個数を確認する。
    tmp = [0]
    for c in S:
        if c == '(':
            tmp.append(tmp[-1] - 1)
        else:
            tmp.append(tmp[-1] + 1)

    # その過剰分の '(' を左端に追加（最後に行う）
    left = max(tmp)

    # 右端から同様に '(' が最大に過剰に
    # なっている個数を確認する。
    tmp = [0]
    for c in S[::-1]:
        if c == ')':
            tmp.append(tmp[-1] - 1)
        else:
            tmp.append(tmp[-1] + 1)

    # その過剰分の ')' を（略
    right = max(tmp)

    print('(' * left + S + ')' * right)

main()
