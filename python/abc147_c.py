# AtCoder Beginner Contest 147 C - honestpOrUnkind2
# https://atcoder.jp/contests/abc147/tasks/abc147_c
# tag: bit全探索 典型問題

# N <= 15, 証言数も N^2 未満なので、bit全探索を行う。
# 計算量は、O(2^N * N^2)

def main():
    N = int(input())
    testimonies = []
    for i in range(N):
        t_n = int(input())
        test = [list(map(int, input().split())) for _ in range(t_n)]
        testimonies.append(test)

    result = 0

    # bit全探索。1 が立っている人が正直者とする
    for st in range(1<<N):
        for witness, test in enumerate(testimonies):
            # 証言者が不親切なら、証言を無視する
            if not st>>witness & 1:
                continue

            # 正直者の証言が、矛盾していないかどうかチェック
            for person, h_stat in test:
                # 0-indexedにする
                person -= 1
                if st>>person & 1 != h_stat:
                    break
            # 証言が全て矛盾無ければ、次の人へ
            else:
                continue

            # 証言に矛盾があり break した場合は、
            # ここで多重ループ脱出、次の bit状態へ
            break

        # 全ての証言者のチェックを正常に終えたら、
        # 正直者の人数をカウントする
        else:
            # いわゆる popcount だが、この書き方でもそこまで遅くない
            tmp_r = bin(st).count('1')
            if tmp_r > result:
                result = tmp_r
    
    print(result)

main()