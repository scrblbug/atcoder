# AtCoder Grand Contest 023 B - Find Symmetries
# https://atcoder.jp/contests/agc023/tasks/agc023_b
# tag: グリッド 対称判定

# 上下、左右が循環するタイプのマップをずらして配置した際に、
# x=y の軸に対して線対称となっているような
# ずらし方は何種類あるか……といった感じ？

# 線対称になったマップは、線対称の軸線に沿って動かしても
# 線対称のまま（N種類ある）なので、とりあえず上下にだけ
# ずらしてみて、線対称になればそれ＋斜め分を加算する。

def main():
    N = int(input())
    field = [[c for c in input()] for _ in range(N)]

    result = 0

    for shift in range(N):
        shifted = field[shift:] + field[:shift]
        # 条件を満たしたら、斜め分(N)を加算する
        if [list(r) for r in zip(*shifted)] == shifted:
            result += N
    
    print(result)

main()
