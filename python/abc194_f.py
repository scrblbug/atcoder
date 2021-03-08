# AtCoder Beginner Contest 194 F - Digits Paradise in Hexadecimal
# https://atcoder.jp/contests/abc194/tasks/abc194_f
# tag: n進数 桁DP

# 桁DPの典型問題に近いが、現れている数の種類をどのように
# 取り扱うかがやや難しい。
# また、DPの方針を思いついても、実装もそれなりに複雑になるので、
# 上級者でないとすんなりと解くのは難しいのではないだろうか。

def main():
    N, K = input().split()
    K = int(K)
    MOD = 10**9 + 7

    # とりあえず N を桁ごとの数字のリストに変換
    h_to_d = {k:v for k, v in zip('0123456789ABCDEF', range(16))}
    n_hd = [0] + [h_to_d[h] for h in N]

    # ついでに n_hd に上から i 桁目までに現れている数字を
    # 事前に確認しておく
    # 現れている数字をビットで表したもの
    appeared = [0]
    # 現れた数字の種類数
    kind = [0]
    for n in n_hd[1:]:
        prev_a, prev_k = appeared[-1], kind[-1]
        if prev_a & 1<<n:
            appeared.append(prev_a)
            kind.append(prev_k)
        else:
            appeared.append(prev_a | 1<<n)
            kind.append(prev_k + 1)

    # dpt[i][j]: 上から i 桁目までで N を下回り、j 種類の数字を
    # 使用しているものの通り数、とする

    # DP表の初期化。一桁目から下回っている場合の数字のみ入れておく。
    dpt = [[0] * 18 for _ in range(len(N) + 1)]
    dpt[1][1] = n_hd[1] - 1

    # 上の桁から順番に配るDPをしていく
    for i in range(1, len(N)):
        for j in range(17):
            # 次の桁に既出の数字を選ぶ場合
            dpt[i+1][j] = (dpt[i+1][j] + dpt[i][j] * j) % MOD
            # 次の桁が初出の数字の場合
            dpt[i+1][j+1] = (dpt[i+1][j+1] + dpt[i][j] * (16-j)) % MOD
        
        # 以下、dpt[i] に現れない分を追加していく

        # i 桁目まで N と一致し、次の桁で N を下回る場合
        # 次の桁の数字は 0 ～ N の i+1 桁目の数字未満となるが、
        # 入れる数字が N の i 桁目までに既出かそうでないかで
        # 遷移先が分岐するため、いちいちチェックしている。
        for nxt in range(n_hd[i+1]):
            if 1<<nxt & appeared[i]:
                dpt[i+1][kind[i]] += 1
            else:
                dpt[i+1][kind[i]+1] += 1
        dpt[i+1][kind[i]] %= MOD
        dpt[i+1][kind[i]+1] %= MOD

        # i 桁目までが 0 で、次の桁で初めて数字が現れる場合
        # これは下回るのが確実なので、1 ～ 15 のどれでもよい
        dpt[i+1][1] = (dpt[i+1][1] + 15) % MOD

    result = dpt[-1][K]

    # DPは N 未満を取り扱っているので、丁度 N の場合も考慮する
    if kind[-1] == K:
        result += 1

    print(result)

main()
