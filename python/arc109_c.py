# AtCoder Regular Contest 109 C - Large RPS Tournament
# https://atcoder.jp/contests/arc109/tasks/arc109_c
# tag: 考察

# 入力例2を元に、具体的に考えてみる。
# トーナメントが仮に無限に行われているとすると、
# RPSSPRSPPRS （の繰り返し）の勝者を決めるためには、
# (RP)(SS)(PR)(SP)(PR)(S と一人余ってしまうので、
# RPSSPRSPPRS RPSSPRSPPRS と2回分あれば、
# 次の対戦の列（の繰り返しの元）を決定できる……
# というのがポイント。

# 余る人数は 0 or 1 （人数が偶数か奇数かによる）なので、
# ある対戦の列があるとして、それを 2 回繰り返してやれば、
# かならず次の対戦の列を決定できる。

def main():
    n, k = map(int, input().split())
    s = input()

    winner = {
        'RR': 'R',
        'RP': 'P',
        'RS': 'R',
        'PR': 'P',
        'PP': 'P',
        'PS': 'S',
        'SR': 'R',
        'SP': 'S',
        'SS': 'S'
    }

    # トーナメントの段数だけ次の対戦列を作成し、
    # その一番最初の手が勝者となる。
    for i in range(k):
        s = s * 2
        w = [winner[s[i:i+2]] for i in range(0, len(s), 2)]
        s = ''.join(w)
    print(s[0])

main()

