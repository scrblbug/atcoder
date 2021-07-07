# AtCoder Beginner Contest 114 C - 755
# https://atcoder.jp/contests/abc114/tasks/abc114_c
# tag: BFS, DFS, N進法

# 3, 5, 7 を含む数を BFS もしくは DFS にて生成していき、
# 条件に合うものをカウントする

def main():
    N = int(input())

    result = 0
    # 探索用キューは、(現在の値, 357の出現チェック)
    # 357出現チェックについては、ビット管理とする
    queue = [(0, 0)]
    while queue:
        now, appeared = queue.pop()
        if appeared == 7:
            result += 1
        
        # 数字の末尾に 3, 5, 7 を加え、出現チェックを更新しつつ
        # キューに入れる
        for i, add in enumerate([3, 5, 7]):
            nxt = now * 10 + add
            appeared_nxt = appeared | 1<<i
            if nxt <= N:
                queue.append((nxt, appeared_nxt))

    print(result)

main()

# 公式解説では、3, 5, 7 と数字が 3種類しかないので、
# 一種の 3進法と考えて順に全探索を行うというやり方を取っている。
# 少し余裕をもって 3^10 まで探索したとしても、余裕で大丈夫。
def main2():
    N = int(input())

    ndic = {0: 3, 1: 5, 2: 7}

    result = 0

    for i in range(3**10):
        numbers = []

        # i を 3進法にするが、純粋な 3進法ではなく
        # 桁ごとに 1 ずつズレていくので注意。
        tmp = i
        while tmp:
            tmp -= 1
            numbers.append(tmp % 3)
            tmp //= 3

        # 対応する数字 (3, 5, 7) に置き換え、
        # 条件を満たすかどうかを確認する。
        real_num = 0
        check = [False, False, False]
        for i, n in enumerate(numbers):
            check[n] = True
            real_num += ndic[n] * 10**i

            # 小さい順にチェックを行うことになるので、
            # 超えた段階で探索を打ち切る。
            if real_num > N:
                break
        else:
            if all(check):
                result += 1
            continue
        break
    
    print(result)

# main2()
