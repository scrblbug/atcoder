# AtCoder Regular Contest 040 B - 直線塗り
# https://atcoder.jp/contests/arc040/tasks/arc040_b
# tag: 考察 愚直 高橋君

# 塗られていない地点へ行き、銃を発射するのを繰り返すのが最短。
# ただし、必要以上に右には移動しないこと。

def main():
    N, R = map(int, input().split())
    field = [c for c in input()]

    # 塗られていない地点のインデックス
    unfilled = [i for i, c in enumerate(field) if c=='.']
    if len(unfilled) == 0:
        print(0)
        return
    else:
        last_unfilled = unfilled[-1]

    # last の地点を塗ることが出来る地点
    last_pos = max(0, last_unfilled - R + 1)

    result = 0

    # 現在地
    pos = 0

    for i, c in enumerate(field):
        if c == 'o':
            continue

        # 移動
        result += min(last_pos, i) - pos
        pos = min(last_pos, i)

        # 銃を発射
        result += 1
        for j in range(R):
            field[pos + j] = 'o'
    
    print(result)

main()

