# 回答中の get_min_diff は、二分探索を利用して書いてもいい。
# いずれにせよ、ソートがボトルネックとなるため O(N log N)。

from bisect import bisect
def main():
    N = int(input())
    dogs = [input().split() for _ in range(2 * N)]

    dog_groups = [[] for _ in range(3)]

    # 色別にグループ分け。
    for a, c in dogs:
        a = int(a)
        if c == 'R':
            dog_groups[0].append(a)
        elif c == 'G':
            dog_groups[1].append(a)
        else:
            dog_groups[2].append(a)

    # ソートしておく。
    for g in dog_groups:
        g.sort()

    # 全て偶数頭数なら、最小値は 0 になる。
    if all(len(g) % 2 == 0 for g in dog_groups):
        print(0)
        return

    # 偶数頭数のものと奇数頭数のものに分ける。
    odd_groups = []
    for g in dog_groups:
        if len(g) % 2 == 1:
            odd_groups.append(g)
        else:
            even_group = g

    # 2つのソート済みリストから一つずつ数字を選び、
    # その差の最小を求める関数を作成しておく。
    def get_min_diff(list_a, list_b):
        # リストの中身がない場合は、最大値を返しておく。
        if len(list_a) == 0 or len(list_b) == 0:
            return 10**16

        result = 10**16

        for va in list_a:
            idx = bisect(list_b, va)
            if idx < len(list_b):
                vb = list_b[idx]
                if abs(va - vb) < result:
                    result = abs(va - vb)
            if idx > 0:
                vb = list_b[idx-1]
                if abs(va - vb) < result:
                    result = abs(va - vb)

        return result

    result = min(
        get_min_diff(odd_groups[0], odd_groups[1]),
        get_min_diff(even_group, odd_groups[0]) + get_min_diff(even_group, odd_groups[1])
    )

    print(result)

main()
