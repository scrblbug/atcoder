# AtCoder Beginner Contest 193 D - Poker
# https://atcoder.jp/contests/abc193/tasks/abc193_d
# tag: 二人ゲーム 確率 高橋君 青木君

# 幸い伏せられているカードは 1 枚ずつの計 2 枚。
# カードの種類も 9 種類しかないので、伏せられているカードの
# 組み合わせを全探索すればいい。

from collections import Counter
# とりあえず手札のリストから点数を求める関数を作っておく。
# 持ってない数も点数に入るので、問題文をちゃんと読んで書こう。
def get_score(cards):
    cnt = Counter(cards)
    result = 0
    for i in range(1, 10):
        if i not in cnt:
            result += i
        else:
            result += i * 10**cnt[i]
    return result

def main():
    K = int(input())
    hand_tak = [int(c) for c in input()[:-1]]
    hand_aok = [int(c) for c in input()[:-1]]

    # とりあえず表になっている枚数のカウント
    cnt = Counter(hand_tak + hand_aok)

    # 高橋君が勝つカードの引き方の通り数を求める
    tak_win_comb = 0

    # a, b が高橋君、青木君の伏せているカードとして、全探索。
    for a in range(1, 10):
        s_tak = get_score(hand_tak + [a])
        for b in range(1, 10):
            s_aok = get_score(hand_aok + [b])

            # 高橋君が勝つ場合
            if s_tak > s_aok:
                # 伏せられていたカードが異なるなら、
                # それぞれの残り枚数を掛けた通り数になる
                # 残りカードの枚数が足りないケースは、自動的に 0 通りに
                # なるので、場合分けは気にしなくていい。
                if a != b:
                    rest_a = K - cnt[a]
                    rest_b = K - cnt[b]
                    tak_win_comb += rest_a * rest_b
                # 同じカードが伏せられていた場合、
                # (残り枚数) * (残り枚数 - 1) 通りになる
                else:
                    rest_a = K - cnt[a]
                    tak_win_comb += rest_a * (rest_a - 1)
    
    # 伏せカードの全通り数は、9 * K 枚から 8 枚判明している状態からなので
    # (9 * K - 8) * (9 * K - 9) 通り。
    # これで割ったものが答えの確率になる。
    print(tak_win_comb / ((9 * K - 8) * (9 * K - 9)))

main()
