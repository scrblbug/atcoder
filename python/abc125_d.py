# AtCoder Beginners Contest 125 D - Flipping Signs
# https://atcoder.jp/contests/abc125/tasks/abc125_d
# tag: 数列 考察

# 反転している、していないを 1, 0 で表すとする。
# ..00100.. とある地点が反転している時、その隣を
# 操作することで、 ..00010.. や ..01000.. とできる。
# すなわち、どこが反転しているかは自由に動かすことが出来る。
# また、反転そのものは 2 個ずつ行われることも考慮すると、
# 結局の所、好きなところを偶数個反転できる、ということになる。

# 数列全体で負の数が偶数個なら、その全てを反転させればいい。

# 負の数が奇数個のときを考える……と、
# 全数列のうち、数字をどれか一つ負にしてやる必要がある。

# つまり、絶対値が一番小さいものを負にしてやればいい。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 絶対値の合計、最小値、負数の個数を求めていく
    abs_total = 0
    abs_min = 10**18
    negative_cnt = 0

    for n in A:
        if n < 0:
            abs_total -= n
            negative_cnt += 1
        else:
            abs_total += n
        if abs(n) < abs_min:
            abs_min = abs(n)

    # 負数が偶数・奇数で分岐
    if negative_cnt % 2 == 0:
        print(abs_total)
    # 絶対値がマイナスに変わるので、2倍してして引く
    else:
        print(abs_total - 2 * abs_min)

main()
