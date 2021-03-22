# AtCoder Grand Contest 017 A - Biscuits
# tag: 考察 順列・組み合わせ

# 選んだ袋のなかのビスケットの合計を偶数 or 奇数にできる
# 組み合わせの数を答える問題。

# ビスケットが全て偶数だった場合は、どのように選んでも偶数に
# なる。すなわち、P = 0 の場合は 2^N 通りで、P = 1 なら 0 通り。

# ビスケット袋に一つでも奇数があった場合、そのうち一つを
# 適当に選ぶ。それ以外の袋から選ぶ組み合わせは、2^(N-1) 通り。
# そのそれぞれに対して、先に選んだ奇数の袋を選ぶ or 選ばないことで、
# 合計は奇数、偶数それぞれに振り分けられる。
# すなわち、合計を奇数、もしくは偶数にする組み合わせの数は、
# どちらも 2^(N-1) 通りということになる。

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))

    # 全部偶数だったら……
    if all(n % 2 == 0 for n in A):
        if P == 0:
            print(2**N)
        else:
            print(0)
    # それ以外
    else:
        print(2**(N-1))

main()

# ……というのが公式解説によるスマートな回答だが、制約が緩いので
# 実はそれなりにゴリゴリと組み合わせを計算しても十分間に合う。
# 合計の偶数・奇数に応じて奇数袋を(0,1,3...) 個 or (0, 2, 4...) 個
# 選ぶ組み合わせの合計に、2^(偶数袋の数) を掛ける……みたいな
# 感じで、初見の時は計算した。
# 以下、その時の恥ずかしい回答を晒しておく。答えは合うし、通る。

# from math import factorial
# def main():
#     N, P = map(int, input().split())
#     A = list(map(int, input().split()))
 
#     rem_zero = 0
#     rem_one = 0
 
#     for a in A:
#         if a % 2 == 0:
#             rem_zero += 1
#         else:
#             rem_one += 1
    
#     result = 0
 
#     if P == 0:
#         for p in range(0, rem_one + 1, 2):
#             result += factorial(rem_one) // (factorial(rem_one - p) * factorial(p))
#     else:
#         for p in range(1, rem_one + 1, 2):
#             result += factorial(rem_one) // (factorial(rem_one - p) * factorial(p))
 
#     result *= 2**(rem_zero)
 
#     print(result)
    
# main()
