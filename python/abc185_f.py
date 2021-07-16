# AtCoder Beginner Contest 185 F - Range Xor Query
# https://atcoder.jp/contests/abc185/tasks/abc185_f
# tag: ビット操作 範囲参照 フェニック木 セグメント木 基礎問題 典型問題

# xor はビットの反転操作。
# 仮に Ti = 1 の時の操作、すなわち値の書き換えが
# なかった場合には、xor の一種の累積和が分かっていれば
# 簡単に解くことができる。

# 逆に言うと、値の書き換えがある場合には、単純な累積和で
# 解くことができない。
# フェニック木(Binary Indexed Tree)、
# あるいはセグメント木を
# 用いる必要がある。

# ここでは、実装の簡単な BIT で解いてみる。
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # Binary Indexed Tree (1-indexed)
    bitree = [0] * (N+1)
    def get_csum(x):
        result = 0
        while x:
            result ^= bitree[x]
            x -= x & -x
        return result

    def op_xor(x, y):
        while x <= N:
            bitree[x] ^= y
            x += x & -x
    
    # BIT 初期化
    for i, a in enumerate(A, start=1):
        op_xor(i, a)

    # クエリ処理
    for t, x, y in queries:
        if t == 1:
            op_xor(x, y)
        else:
            print(get_csum(y) ^ get_csum(x-1))

main()
