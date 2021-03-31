# CODE FESTIVAL 2015 あさぷろ Middle A - ヘイホーくんと最終試験
# https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_c
# tag: 基礎問題

# この問題に限らず、基本的な方針として、なるべく小数を
# 使用しないようにしたい。
# 書き方によっては、K==N のとき微妙に処理が変わるので注意すること。

def main():
    N, K, M, R = map(int, input().split())
    scores = [int(input()) for _ in range(N-1)]

    # コーナーケース (K==N) 対応のため、とりあえず 0 点を追加してから
    # ソートしておく。
    # もちろん、あとから個別に条件分岐させてもOK。
    scores.append(0)
    scores.sort(reverse=True)

    # 上位 K 個の平均が R 以上である必要がある。
    # つまり、上位 K 個の合計が、 R * K である必要がある。
    needed = K * R

    # 現在の上位 K 個の合計
    sum_now = sum(scores[:K])

    # すでに上回っているなら、0 点でもよい
    if sum_now >= needed:
        print(0)
        return
    
    # 上回っていない場合、少なくとも現在の上から K 個目の点数より
    # 高い点数を取る必要がある。
    # よって、上から K 個目の点数を差し引き、必要な点数を求める。
    # （先程のコーナーケース対応は、ここで必要）
    result = needed - (sum_now - scores[K-1])

    # 求めた点数が、満点を超えている場合は、達成不可能なので注意
    if result > M:
        print(-1)
    else:
        print(result)

main()
