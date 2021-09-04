
# XOR は交換法則が成り立つので、好きな順で行ってもいい。
# また、任意の数 x について、 x XOR x = 0 となるので、
# f(0, B) = 0 xor 1 xor 2 xor ... xor A-1 xor A xor... B
# f(0, A-1) = 0 xor 1 xor 2 xor... xor A-1
# より、
# f(0, B) xor f(0, A-1) = 0 xor A xor A+1 xor ... B
# = f(A, B) となる。

# そこで、g(x) を 0 xor 1 xor 2 xor ... x とする。
# このとき、
# g(x) = (0 xor 1) xor (2 xor 3) xor .... x
#      = 1 xor 1 xor ....
# という具合に、偶数個ずつまとめることができる。

# 具体的には
# x % 4 == 0 のとき、g(x) = x
# x % 4 == 1 のとき、g(x) = 1
# x % 4 == 2 のとき、g(x) = 1 ^ x
# x % 4 == 3 のとき、g(x) = 0

def main():
    A, B = map(int, input().split())

    # 考察より、0 xor 1 xor 2 ... xor x を返す関数を作成。
    def g(x):
        if x % 4 == 0:
            return x
        elif x % 4 == 1:
            return 1
        elif x % 4 == 2:
            return 1^x
        elif x % 4 == 3:
            return 0

    print(g(B) ^ g(A-1))

main()
