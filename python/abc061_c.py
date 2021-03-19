# AtCoder Beginner Contest 061 C- Big Array
# https://atcoder.jp/contests/abc061/tasks/abc061_c
# tag: 基礎問題 計算量

# 制約が大きいので、馬鹿正直に配列に数字を一個一個入れていくのはよくない。
# 下手すると 10^5 個の数字を 10^5 回入れた上で、ソートする羽目になる。
# 入れた数字の種類と個数だけを保存しておくのがいいだろう。
# 最終的に種類だけでソートし、後はそれぞれの数字が入っている個数を
# 確認しながら、上から K 番目の数字を確認すればいい。

def main():
    N, K = map(int, input().split())
    inserts = [list(map(int, input().split())) for _ in range(N)]

    # カウント用の辞書を用意
    counter = {}

    # 順に見ていき、最終的に何がいくつ入っているのかをカウントしておく
    for num, volume in inserts:
        if num not in counter:
            counter[num] = 0
        counter[num] += volume
    
    checked = 0

    # 入っている数字をソートしつつ順に取り出していく
    for num in sorted(counter.keys()):
        # 求める順位が次の数字の個数で達成できるなら、その数字を回答
        if checked <=  K <= checked + counter[num]:
            print(num)
            return
        # 足りないなら、数字の個数をチェック済みとして、次の数字を見る
        checked += counter[num]

main()
