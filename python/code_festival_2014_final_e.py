# CODE FESTIVAL 2014 決勝 E - 常ならずグラフ
# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_e
# tag: 数列 部分列 Tさん

# 前の値に対して増加するか減少するかのみに注目する。
# （増加も減少もしない場合は無視していい）
# 二回以上連続で増加、あるいは減少する場合には
# 最後の数字のみを採用し、他の数字は取り除けばいい。

# f.e.
# [2, 3, 3, 5, 4, 5, 4, 3, 2, 3, 2, 1]
# なら差分は ↑→↑↓↑↓↓↓↑↓↓ となる。
# 最初の数字は必ず採用するとして、
# この連続する増加と減少の最後の数字のみを取り出すと
# [2, 5, 4, 5, 2, 3, 1] となる感じ。

# ところで、この問題で求める必要があるのは
# 最終的な個数のみ。
# まず、最初と最後の数字は必ずカウントすることになる。
# それに加えて、増加→減少、あるいは減少→増加と変化した
# 回数を数えればいい。


def main():
    N = int(input())
    R = list(map(int, input().split()))

    # 増加してるか、減少してるかだけを取り出す
    diff = []
    for a, b in zip(R, R[1:]):
        if a > b:
            diff.append(-1)
        elif b > a:
            diff.append(1)

    # 最後の数字は必ず採用
    result = 1

    # 増加と減少が入れ替わった回数を数えれば、採用する数字の個数になる
    # 初回を必ずカウントするために前回の増減を 0 とする。
    prev = 0
    for d in diff:
        if d != prev:
            result += 1
        prev = d

    if result >= 3:
        print(result)
    else:
        print(0)

main()
