# AtCoder Regular Contest 067 D - Walk and Teleport
# https://atcoder.jp/contests/arc067/tasks/arc067_b
# tag: 貪欲法

# 歩いたほうがいいのかテレポートしたほうがいいのかを
# 考える際、結局の所、ある町からすぐ隣の町へ向かうときの
# ことだけを考慮すればいい。

# また、スタート地点は西端なので、そこから東に向かって
# 貪欲法で訪れていけばいい。

def main():
    N, A, B = map(int, input().split())
    cities = list(map(int, input().split()))

    result = 0

    for i in range(N-1):
        # 次の町まで歩いたときとテレポートした時を比較
        dist = cities[i+1] - cities[i]
        if A * dist > B:
            result += B
        else:
            result += A * dist
    
    print(result)

main()
