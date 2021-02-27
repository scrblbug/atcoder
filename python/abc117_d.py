# AtCoder Beginner Contest 117 D - XXOR
# https://atcoder.jp/contests/abc117/tasks/abc117_d
# tag: ビット演算 XOR 桁DP

# ビット毎に独立して考える
# 選ぶ数字 X によって、A を各ビット毎に反転させるかどうかを
# 選ぶことが出来る。つまり、上限が無い場合は、ビットごとにAを見て
# ビットが立っているのが少ないほうがベストな選択となる

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 確認しなければならない桁数
    max_bit = max(max(A).bit_length(), K.bit_length())

    # とりあえず各桁ごとの集計を取っておく
    bit_cnts = []
    # ついでに、下 n 桁の最善手における合計値を計算しておく
    best_csum = [0]
    
    for i in range(max_bit):
        zeros, ones = 0, 0
        for a in A:
            if (1<<i) & a:
                ones += 1
            else:
                zeros += 1
        bit_cnts.append([zeros, ones])
        best_csum.append(best_csum[-1] + (2**i) * max(zeros, ones))

    # Kを上限とし、上の桁から見ていく
    # Kを下回った桁から、ベストな選択を行っていく
    # そこで、i 桁目から下回ると仮定して、i の全探索を行う
    # 下回ることが可能な桁は、K のビットが立っている桁に限定される
    search_bits = []
    for i in range(max_bit):
        if (1<<i) & K:
            search_bits.append(i)

    # Kを下回らない、つまりKと一致するケースを初期値とする
    result = sum(K ^ a for a in A)

    for b in search_bits:
        tmp_r = 0

        # 下から b-1 桁目までは、ベストな選択
        tmp_r += best_csum[b]

        # b 桁目は、必ず 0 を選択。つまり、集計した 1 の数を見る
        tmp_r += bit_cnts[b][1] * (2**b)

        # それより上は、Kをそのまま利用する
        for i in range(b+1, max_bit):
            if (1<<i) & K:
                tmp_r += bit_cnts[i][0] * (2**i)
            else:
                tmp_r += bit_cnts[i][1] * (2**i)
        
        if tmp_r > result:
            result = tmp_r
    
    print(result)

main()
