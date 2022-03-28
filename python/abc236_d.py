# AtCoder Beginner Contest 236 D - Dance
# https://atcoder.jp/contests/abc236/tasks/abc236_d
# tag: DFS

def main():
    N = int(input())
    affin = [list(map(int, input().split())) for _ in range(2*N-1)]

    result = 0

    bit_to_n = [-1] * (2**(2*N))
    for i in range(2*N):
        bit_to_n[2**i] = i

    def dfs(rest, score):
        nonlocal result
        if rest == 0:
            if score > result:
                result = score
                return

        nxt_a = rest & -rest
        tmp = rest ^ nxt_a

        while tmp:
            nxt_b = tmp & -tmp
            tmp -= nxt_b

            t_score = affin[bit_to_n[nxt_a]][bit_to_n[nxt_b]-bit_to_n[nxt_a]-1]
            dfs(rest ^ nxt_a ^ nxt_b, score ^ t_score)
    dfs((1<<(2*N))-1, 0)
    print(result)

main()
