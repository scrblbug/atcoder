# AtCoder Regular Contest 049 B - 高橋ノルム君
# https://atcoder.jp/contests/arc049/tasks/arc049_b
# tag: 二分探索

# なんかこう、数学的に一発で求めることも可能そうだけど……
# それを解けるだけの数学力は無い。

# 代わりに、集合可能かどうかは O(N) で判定可能なので、
# 二分探索で答えを求めていく。

def main():
    N = int(input())
    taks = [list(map(int, input().split())) for _ in range(N)]
    x, y, c = zip(*taks)
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)

    # 時間 t で全員集合可能かどうか？
    def eval(t):
        # t で移動できる範囲を全員分チェックし、
        # どこかわずかでも重なっている必要がある。
        
        # left, right, down, up で重なっている範囲を管理
        # 初期値は、全員を含める四角とする
        left, right = x_min, x_max
        down, up = y_min, y_max
        
        # 高橋ノルム君毎に、集合可能な範囲が狭まっていく
        for x, y, c in taks:
            mv = t / c
            left = max(left, x - mv)
            right = min(right, x + mv)
            down = max(down, y - mv)
            up = min(up, y + mv)

            # 集合可能な範囲がなくなれば、False
            if left > right or down > up:
                return False
        # 最後まで範囲が残れば True
        return True

    # さっきの評価関数を用いて、二分探索で答えを求める
    right = 10**9
    left = 0
    while right - left > 0.00001:
        mid = (right + left) / 2
        if eval(mid):
            right = mid
        else:
            left = mid
    
    print(right)

main()

# おまけ：当初思いついた、三分探索により集合位置を決めてみるバージョン
# X 軸と Y 軸を独立に考える。
# 集合場所を端から端まで移動させていくと、掛かる時間は凹型のグラフになるので、
# その最小値を返す場所を三分探索で求める……みたいな。
def main2():
    N = int(input())
    taks = [list(map(int, input().split())) for _ in range(N)]

    x_nums, y_nums, costs = zip(*taks)

    # 評価用関数
    def get_cost(now, nums):
        return max(abs(now-n)*c for n, c in zip(nums, costs))

    def get_min_cost(nums):
        # 三分探索で、最小値を返す場所を求める
        left, right = min(nums), max(nums)
        while right - left > 0.00001:
            mid1 = (left * 2 + right) / 3
            mid2 = (left + right * 2) / 3
            if get_cost(mid1, nums) > get_cost(mid2, nums):
                left = mid1
            else:
                right = mid2
    
        # 三分探索後、もとめられる最小値を返す
        return get_cost(left, nums)

    print(max(get_min_cost(x_nums), get_min_cost(y_nums)))

# main2()