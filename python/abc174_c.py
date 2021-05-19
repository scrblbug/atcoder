# AtCoder Beginner Contest 174 C - Repsept
# https://atcoder.jp/contests/abc174/tasks/abc174_c
# tag: 整数 倍数 MOD 高橋君

# そのまま計算すると数列の数字がとんでもなく大きくなるので、
# MOD K を取って計算することを考える。
# 毎回の操作を
# （0 から始めて） 10 倍して 7 を足し、MOD K を取る
# だと考えることができる。

# また、毎回同じ操作を行っているということと、MOD K の
# 値が 0 ～ K-1 に限定されるということから、得られる値は
# 必ず循環するようになる。
# その循環の長さの上限は、MOD K の値が K 個に限定される
# ことから、K になる。
# よって K 回試行して割り切れなければ、0 を含まずに
# 循環が起こっていることになり、割り切れることはない。

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
