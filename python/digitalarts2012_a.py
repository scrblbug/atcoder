# DigitalArts プログラミングコンテスト 2012 A - C-Filter
# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1
# tag: 正規表現

# 単語ごとの判定なので、単語にばらしてから各NGワードと
# 比較していくのが簡単だと思われる。
# 正規表現を用いてサボってもいいが、ここでは真面目に（？）
# 実装してみることにした。
from collections import defaultdict
def main():
    S = input()
    N = int(input())
    ng_words = [input() for _ in range(N)]

    # せっかくなのでNGワードを長さ別に整理しておく
    # やってもやらなくても大差ないので、後で長さチェックを
    # 行ってもよい。
    # defaultdict(list) にすることで、無いキーを指定されても
    # [] （空リスト）を返すようになっている。
    ngw_by_len = defaultdict(list)
    for ngw in ng_words:
        ngw_by_len[len(ngw)].append(ngw)

    result = []

    # for ～ else 大好きっ子なので一見おぞましい書き方になっている。
    # 素直にフラッグを作成して実装するほうが分かりやすいかも。
    for wd in S.split():
        for ngw in ngw_by_len[len(wd)]:
            for i in range(len(ngw)):
                if ngw[i] == '*':
                    continue
                if wd[i] != ngw[i]:
                    break

            # 文字チェックが最後まで行き着く＝NGワードの条件を満たす
            # なら、****にして break。ここの break は、2 個目のfor
            # に対して働く
            else:
                result.append('*' * len(wd))
                break

        # NGワードを全部パスしたら、そのまま配列に入れる
        else:
            result.append(wd)

    print(' '.join(result))

main()


