# AtCoder Beginner Contest 063 D - Widespread
# https://atcoder.jp/contests/abc063/tasks/arc075_b
# tag: 二分探索 典型問題

# x 回の爆発で全ての魔物を消せるかどうか、という問題なら
# 簡単に解けるので、二分探索を行う。

def main():
    N, A, B = map(int, input().split())
    monsters = [int(input()) for _ in range(N)]

    # x 回の爆発で可能？
    def check(x):
        need = 0
        # モンスターごとに、何回 A のダメージを与える
        # 必要があるかを求めていく。
        # その回数が x を越えるなら、不可能。
        for h in monsters:
            rem = h - B * x
            if rem > 0:
                # 割って切り上げと同義
                need += (rem - 1) // (A - B) + 1
        if need > x:
            return False
        else:
            return True

    # 二分探索
    left = 0
    right = 10**9 + 1

    while right - left > 1:
        mid = (right + left) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    
    print(right)

main()