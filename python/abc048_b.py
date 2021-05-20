# AtCoder Beginner Contest 048 B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b
# tag: 整数 倍数 基礎問題 コーナーケース 数え上げ

# 一見簡単だが、意外とコーナーケースに引っかかりがちな問題。
# 余りの差分が～などと、ややこしく考え始めるとハマるので、
# シンプルに問題を分解してやるほうがいい。

# まず、0 ~ n の間に x で割り切れる数はいくつあるのかを考えてやる。
def count_div(n, x):
    # n < 0 のコーナーケースに注意……といいつつ
    # (-1 // 2) + 1 = 0 なので、実は無くてもちゃんと動く。 
    if n < 0:
        return 0
    # 0 も含むので、1 足してやる
    else:
        return (n // x) + 1

def main():
    a, b, x = map(int, input().split())

    # 0 ～ b の区間の数から、0 ～ a-1 の区間の数を引いてやればいい
    print(count_div(b, x) - count_div(a-1, x))

main()
