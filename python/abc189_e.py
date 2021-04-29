# AtCoder Beginner Contest 189 E - Rotate and Flip
# https://atcoder.jp/contests/abc189/tasks/abc189_e
# tag: 計算幾何 アフィン変換

# アフィン変換を知っていると解きやすい。
# 今回の一連の操作はアフィン変換、つまり行列計算とみなせるので、
# i 回目の操作後の変換行列をあらかじめ計算、保持しておき、
# クエリごとに求める点の座標を変換して答えてやる。

# 行列計算
def m_by_v(m, v):
    result = []
    for row in m:
        result.append(sum(e1 * e2 for e1, e2 in zip(row, v)))
    return result

def m_by_m(m1, m2):
    result = []
    for r1 in m1:
        tmp = []
        for r2 in zip(*m2):
            tmp.append(sum(e1 * e2 for e1, e2 in zip(r1, r2)))
        result.append(tmp)
    return result

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    ops = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    conv_ms = []

    # 最初は単位行列をもたせておく
    conv_ms.append([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    for op in ops:
        # 時計回りに90度回転
        if op[0] == 1:
            cm = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
        
        elif op[0] == 2:
        # 反時計回りに90度回転
            cm = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        
        else:
            o, p = op
            # x = p を軸に反転
            if o == 3:
                cm = [[-1, 0, 2*p], [0, 1, 0], [0, 0, 1]]
            # y = p を軸に反転
            else:
                cm = [[1, 0, 0], [0, -1, 2*p], [0, 0, 1]]

        # 後の変換を前から掛けるので注意。
        conv_ms.append(m_by_m(cm, conv_ms[-1]))

    for a, b in queries:
        pos = points[b-1]
        pos.append(1)

        result = m_by_v(conv_ms[a], pos)
        print(*result[:-1])

main()
