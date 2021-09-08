# AtCoder Beginner Contest 217 D - Cutting Woods
# https://atcoder.jp/contests/abc217/tasks/abc217_d
# tag: 座標圧縮 BIT Union_Find 平衡二分木

# 実は C++ だと std::set を利用して割とあっさり解けるが、
# Python3 では該当する標準ライブラリが無いため、かなり
# 難しくなる問題。

# ひとまず、1 <= L <= 10^9 という制限が厳しいので、
# 座標圧縮をしてから考える。

# 切られているか切られていないかは BIT で管理する。
# つまり、圧縮後の座標において切られているところに
# 1 を加えていくことで、左端から数えて何回切られているか
# という情報を管理するようにする。

# 長さを求めるクエリが来たときには、BIT 上で
# 手前で切られている地点と次に切られている地点を求め、
# 長さを出力する……という方針。

# BITクラス
# 内部処理は 1-indexed だが、引数・返り値は 0-indexed に統一。
class Binary_Indexed_Tree:
    def __init__(self, N):
        self._len = 1 << ((N-1).bit_length())
        self._tree = [0] * (self._len + 1)

    # pos に対して x を加える。
    def add_to(self, x, pos):
        pos += 1
        while pos <= self._len:
            self._tree[pos] += x
            pos = pos + (pos & -pos)

    # pos までの累積和を返す。
    def get_csum(self, pos):
        pos += 1
        result = 0
        while pos > 0:
            result += self._tree[pos]
            pos = pos - (pos & -pos)
        return result
    
    # 累積和が value となる最小のインデックスを返す。
    def get_lower(self, value):
        if value < 0:
            return 0

        result = 0
        check = self._len // 2

        # ここからBIT上で直接二分探索を行っているような感じ。
        while check > 0:
            if value > self._tree[result + check]:
                value -= self._tree[result + check]
                result += check
            check //= 2

        return result

# ここからメイン。
def main():
    L, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 座標圧縮。 0 と L も加えておく。
    x_list = [x for c, x in queries] + [0, L]
    x_list = list(set(x_list))
    x_list.sort()
    comp_dic = {x:i for i, x in enumerate(x_list)}

    # BIT 作成。0 と L の地点をあらかじめ切っておく。
    bit = Binary_Indexed_Tree(len(x_list))
    bit.add_to(1, comp_dic[0])
    bit.add_to(1, comp_dic[L])

    # クエリ処理。
    for c, x in queries:
        if c == 1:
            bit.add_to(1, comp_dic[x])
        
        else:
            # クエリで指定されているところが、
            # 左端から何回切られている地点かを求める。
            value = bit.get_csum(comp_dic[x])

            # 上記情報を元に、左側の切断地点を求める。
            lower = bit.get_lower(value)

            # 同様に、右側の切断地点を求める。
            nxt = bit.get_lower(value + 1)

            print(x_list[nxt] - x_list[lower])

main()
