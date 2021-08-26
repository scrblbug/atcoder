# 全国統一プログラミング王決定戦予選 C - Different Strokes
# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c
# tag: ゲーム 2人ゲーム 貪欲法 高橋君 青木君

# ある食べ物を高橋君、青木君それぞれが食べたときの
# 幸福度を t, a とする。

# 高橋君が食べたときの利得は、高橋君が得る幸福度 t と、
# 青木君が失う幸福度 a なので、t + a となる。
# 逆に青木くんが食べたときの利得も、同様に t + a となる。

# つまり、t + a が大きい順に、交互に食べられていくという
# ことになる。

def main():
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]

    # 考察のとおり、t + a で降順にソートしておく。
    scores.sort(key = lambda x:x[0] + x[1], reverse=True)

    tak_score = sum(s[0] for s in scores[::2])
    aok_score = sum(s[1] for s in scores[1::2])

    print(tak_score - aok_score)

main()
