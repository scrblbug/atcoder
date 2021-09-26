# AtCoder Beginner Contest 042 C - こだわり物いろはちゃん
# https://atcoder.jp/contests/abc042/tasks/arc058_a
# tag: 愚直 いろはちゃん

# N 円から順に 1 円ずつ増やしながら、条件に合った金額か
# どうか確かめる。
# せいぜい 10N までいく間に見つかるので、十分間に合う。

def main():
    N, K = map(int, input().split())
    dislikes = input().split()

    result = N
    while True:
        if all(d not in str(result) for d in dislikes):
            print(result)
            return
        result += 1

main()
