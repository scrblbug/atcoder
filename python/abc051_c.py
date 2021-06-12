# AtCoder Beginner Contest 051 C - Back and Forth
# https://atcoder.jp/contests/abc051/tasks/abc051_c
# tag: グリッド 最短経路 愚直

# s:(0, 0) t:(1, 1) の時を考えてみると、

# jih    
# kgtb   
# lsac   
#  fed   

# 上図で
# satbcdefsgthijkls
# の順に行くのが最短（一例）

# スタートとゴールが離れている場合は、途中を伸ばすだけでいい

def main():
    sx, sy, tx, ty = map(int, input().split())

    dx = tx - sx
    dy = ty - sy

    result = ''

    # 往路 1
    result += 'R'*dx + 'U'*dy

    # 復路 1
    result += 'RD' + 'D'*dy + 'L'*dx + 'LU'

    # 往路 2
    result += 'U'*dy + 'R'*dx

    # 復路 2
    result += 'UL' + 'L'*dx + 'D'*dy + 'DR'

    print(result)

main()
