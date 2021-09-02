# AtCoder Regular Contest 121 B - RGB Matching
# https://atcoder.jp/contests/arc121/tasks/arc121_b
# tag: 考察

# 明らかに同じ色の犬同士をペアにするほうがいいのだが、
# 頭数が奇数なら余りが出てしまうことがある。
# それをどのように組み合わせてやるかがポイント。

# 奇数頭数の色のグループを R, G、
# 偶数頭数の色のグループを B と仮に考える。

# この際、考慮しなければならない組み合わせは以下の通り

# 1) R, G から 1 頭ずつを選び、それを組み合わせる。
# これは R, G を前から順に見ていくことで、
# 最小コストを求めることができる。

# 2) R, G から 1 頭ずつ選び、それぞれを B から
# 選んだものと組み合わせる。
# これも同様に可能だが、RB の組み合わせと GB の組み合わせで
# 使用される B が同一のものである可能性がある。
# しかし、その場合、その最小コストは 1) の最小コスト
# 以上となるので、考慮しなくてもいい（数直線上に書いて
# 考察すると分かりやすい）。

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

        idx_a, idx_b = 0, 0
        result = 10**16

        # 値の小さい方のインデックスを進めていきつつ、
        # 順に探索していく。
        while True:
            va, vb = list_a[idx_a], list_b[idx_b]
            if abs(va - vb) < result:
                result = abs(va - vb)

            if idx_a == len(list_a) - 1:
                idx_b += 1
            elif idx_b == len(list_b) - 1:
                idx_a += 1
            elif va <= vb:
                idx_a += 1
            else:
                idx_b += 1

            if idx_a == len(list_a) or idx_b == len(list_b):
                break

        return result

    result = min(
        get_min_diff(odd_groups[0], odd_groups[1]),
        get_min_diff(even_group, odd_groups[0]) + get_min_diff(even_group, odd_groups[1])
    )

    print(result)

main()
