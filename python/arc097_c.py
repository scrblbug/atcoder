# AtCoder Regular Contest 097 C - K-th Substring
# https://atcoder.jp/contests/arc097/tasks/arc097_a
# tag: 文字列 部分連続列 辞書順 考察

# 1 <= K <= 5 という制限がポイント。
# 求める文字列は、必ず 5 文字以内の長さになる。
# （正確には、K 文字以内）

# 背理法：
# 求めるものが 6 文字以上の文字列、仮に'abcdef'になったと仮定する。
# 条件より、'a' 'ab' 'abc' 'abcd' 'abcde' のように、右端から
# 文字を取り除いていった文字列は、かならず 'abcdef' よりも
# 辞書順で小さくなる。つまり、'abcdef' は少なくとも 6 番目に小さい
# 文字列となる。よって、矛盾。

# 5 文字以内なら、十分全探索可能。

def main():
    s = input()
    K = int(input())

    substrings = set()

    # 全箇所から K 文字以内の文字列を切り出し、set() に入れていく
    for left in range(len(s)):
        for right in range(left+1, left+1+K):
            substrings.add(s[left:right])

    # 全体をソート
    substrings = sorted(list(substrings))

    # 回答
    print(substrings[K-1])

main()
