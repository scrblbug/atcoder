# CODE FESTIVAL 2014 決勝 D - パスカルの三角形
# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_d
# tag: 二項係数 基礎問題

# 何段か書いてみれば、すぐに気づくと思うが、
# n 段目の左から（もしくは右から） 2 個目の数字は
# n-1 になる (n >= 2)

def main():
    A = int(input())
    print(A+1, 2)

main()
