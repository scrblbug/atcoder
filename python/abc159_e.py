# AtCoder Beginner Contest 159 E - Dividing Chocolate
# https://atcoder.jp/contests/abc159/tasks/abc159_e
# tag: グリッド 分割 累積和 二分探索

# 縦横の割り方全てを全探索すると、間に合わない。
# 縦が比較的小さい(10)ので、こちらをどう分割するかを
# 全探索する。（最大 2^9 = 512 通り）
# 横をどう分割するかは、単純に端から貪欲に取っていっても
# 十分に間に合う。
# が、ここでは最速を目指して二分探索でどこまで取れるかを
# 求めている。

def main():
    H, W, K = map(int, input().split())
    chocolate = [[int(c) for c in input()] for _ in range(H)]

    # とりあえず累積和を求めておく。
    # ちなみに、今回は取らなくても順次探索することで間に合うが、
    # 二分探索を行う予定なので求めておく。
    csum_choc = [[0] * (W+1)]
    for row in chocolate:
        csum = 0
        csum_row = [0]
        for index, n in enumerate(row, start=1):
            csum += n
            csum_row.append(csum + csum_choc[-1][index])
        csum_choc.append(csum_row)

    # 範囲の和を求める関数も作っておく
    # 今回は半開放で取ってあるので注意
    def get_csum(x1, y1, x2, y2):
        return csum_choc[y2][x2] - csum_choc[y1][x2] - csum_choc[y2][x1] + csum_choc[y1][x1]

    # どこまで横にチョコレートを取ることが出来るかを
    # 二分探索で求める関数
    def get_next_cut(pos_now):
        low = pos_now - 1
        high = W

        while (high - low > 1):
            mid = (high + low) // 2

            # 縦方向に条件を満たすか確認していく
            start = 0
            # 最後は一番下で切るように扱う
            for hc in h_cuts + [H]:
                tmp = get_csum(pos_now, start, mid+1, hc)
                if tmp <= K:
                    start = hc
                    continue
                else:
                    break
            else:
                low = mid
                continue
            high = mid
        
        # 次のポジションを返したいので、highを返す
        return high
    
    result = 10**18

    # 水平方向の分割を全探索するが、
    # ここでは、どこの手前で切るかをビットで管理することに
    for h_cut_status in range(1<<(H-1)):
        
        # カットする場所をとりまとめ
        h_cuts = []
        for i in range(H-1):
            if h_cut_status & (1<<i):
                h_cuts.append(i+1)

        # 今回のカットでの最小値を求める
        now_pos = 0
        tmp_r = len(h_cuts)

        # 水平方向のカットですでに現在の最小カットを
        # 超える場合、探索は飛ばす
        if tmp_r >= result:
            continue
        
        # 横方向にどんどん切っていく
        while True:
            next_pos = get_next_cut(now_pos)
            # ……切れない……だと……？
            if next_pos == now_pos:
                tmp_r = 10**18
                break

            # 最後まで行った＼(^o^)／
            elif next_pos == W:
                break

            else:
                tmp_r += 1
                now_pos = next_pos

        if result > tmp_r:
            result = tmp_r

    print(result)

main()
