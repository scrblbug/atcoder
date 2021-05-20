# AtCoder Beginner Contest 003 C - AtCoderプログラミング講座
# https://atcoder.jp/contests/abc003/tasks/abc003_3
# tag: 最大値 考察 高橋君

# まず、動画のうちレートの高い上位 K 個を選ぶほうがいいのは自明。

# あとはどのような順序で見るほうがいいのか、という問題になる。
# 直感的には、下から観る方が良さそうだけど……。

# ここで、仮に今のレートを R とし、レートが A, B の動画を
# 続けて観るとしてみる。

# すると最終的なレートは、
# R → (R + A) / 2 → (R + A + 2*B) / 4 となる
# つまり、あとから見る動画のほうが、最終的なレートに対する
# 寄与は大きくなる。
# というわけで、レートの低い順に動画を観ていく方針で良い。

def main():
    N, K = map(int, input().split())
    movies = list(map(int, input().split()))

    movies.sort()

    rating = 0

    # ソートしたものの、上位 K 個を下から確認
    for r in movies[N-K:]:
        rating = (rating + r) / 2
    
    print(rating)

main()
