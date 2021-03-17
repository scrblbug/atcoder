# AtCoder Beginner Contest 171 C - One Quadrillion and One Dalmatians
# https://atcoder.jp/contests/abc171/tasks/abc171_c
# tag: N進法

# 基本的な考え方は26進法だが、端の文字 (0) がない関係で、
# 桁ごとに 1 ずつずれていくので注意。

def main():
    N = int(input())
    result = []

    while N > 0:
        N -= 1
        result.append(N % 26)
        N //= 26
    
    print(''.join([chr(ord('a')+n) for n in result[::-1]]))

main()
