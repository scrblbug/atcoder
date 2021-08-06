# AtCoder Beginner Contest 035 C - オセロ
# https://atcoder.jp/contests/abc035/tasks/abc035_c
# tag: 範囲操作 いもす法 典型問題

# 範囲操作のクエリが多数あるため、そのまま実装すると TLE。
# どうにか情報を圧縮してやる必要がある。

# 00000000 に対して、(2, 6) の操作が行われるとすると
# 01111100 となる。これを素直に実装すると 5 箇所書き換える
# 必要があるのを、
# 01000010 (imos) という具合に記録することを考える。
# これは、1 の現れたところで直前の駒に対して反転させるという
# 意味合い。
# ちなみにここに更に (4, 6) の操作を行うと、
# 01010000 (imos)
#    ^  ^  ここを書き換える
# といった感じになる。

# これにより、操作一回分につき 2 箇所を書き換えるだけで
# 済むようになる。

# 回答列は、この操作を記録した列を元に再構成していく。
# 01010000 (imos)
#  ^ ^      反転箇所
# 01100000 (result)

def main():
    N, Q = map(int, input().split())
    ops = [list(map(int, input().split())) for _ in range(Q)]

    # 駒が反転するところに 1 を設定していく。
    imos = [0] * (N+1)
    for l, r in ops:
        # 反転の反転を元通りにするため、xor 1 としている。
        imos[l-1] ^= 1
        imos[r] ^= 1
    
    # 順に回答の列を再現していく。
    # imos の末尾は使用しないので注意。
    result = []
    tmp = 0
    for v in imos[:-1]:
        tmp ^= v
        result.append(tmp)

    print(''.join(str(v) for v in result))

main()
