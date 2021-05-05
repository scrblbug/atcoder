# AtCoder Beginner Contest 122 D - We Like AGC
# https://atcoder.jp/contests/abc122/tasks/abc122_d
# tag: 文字列 考察 DP MOD

from itertools import product
def main():
    N = int(input())
    MOD = 10**9 + 7

    ngs = set()
    for pattern in product('ACGT', repeat=4):
        for i in range(4):
            tmp = list(pattern)
            if i > 0:
                tmp[i-1], tmp[i] = tmp[i], tmp[i-1]
            tmp = ''.join(tmp)
            if 'AGC' in tmp:
                ngs.add(''.join(pattern))

    dpt = {'TTT': 1}
    for i in range(N):
        new_dpt = dict()
        for last3, cnt in dpt.items():
            for c in 'ACGT':
                if last3 + c in ngs:
                    continue
                new_last3 = last3[1:] + c
                if new_last3 not in new_dpt:
                    new_dpt[new_last3] = 0
                new_dpt[new_last3] = (new_dpt[new_last3] + cnt) % MOD
        dpt = new_dpt
    print(sum(dpt.values()) % MOD)

main()
