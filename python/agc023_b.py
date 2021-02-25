def main():
    N = int(input())
    field = [[c for c in input()] for _ in range(N)]

    # 上下、左右が循環するタイプのマップをずらして配置した際に、
    # x=y の軸に対して線対称となっているような
    # ずらし方は何種類あるか……といった感じ？

    # 線対称になったマップは、線対称の軸線に沿って動かしても
    # 線対称のまま（N種類ある）なので、とりあえず上下にだけ
    # ずらしてみて、線対称になればそれ＋斜め分を加算する。

    result = 0

    for shift in range(N):
        shifted = field[shift:] + field[:shift]
        if [list(r) for r in zip(*shifted)] == shifted:
            result += N
    
    # 条件を満たしたら、斜め分(N)を加算する
    print(result)

main()
