# AtCoder Beginner Contest 174 C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c
# tag: 倍数 MOD

# そのまま計算すると数列の数字がとんでもなく大きくなるので、
# MOD K を取って計算することを考える。
# 毎回の操作を（0 から始めて） 10 倍して 7 を足し、MOD K を取る
# だと考えることができる。

# また、K 回試行しても割り切れる数字が出ない場合は、
# MOD の数字は K 種類しかないため、鳥の巣原理により
# 同じ数字が 2 回以上現れている ＝ どこかで循環している
# ＝ 割り切れることはない、ということになる。

def main():
    K = int(input())
    tmp = 0

    # K 回試行
    for i in range(K):
        # 10 倍して 7 を足し、MOD K を取り続ける
        tmp = (tmp * 10 + 7) % K

        # 0 になれば、割り切れたということなので、
        # 答えを返して終了
        if tmp == 0:
            print(i + 1)
            return

    # K 回やってダメなら割り切れることはない
    print(-1)

main()
