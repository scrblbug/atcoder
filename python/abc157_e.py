# AtCoder Beginners Contest 157 E - Stimple String Queries
# https://atcoder.jp/contests/abc157/tasks/abc157_e
# 範囲クエリ 典型問題 セグメント木

# セグメント木でどの文字を持っているかを管理してやる

class Segment_Tree:
    # リストもしくは要素数にて初期化を行う。
    # デフォルトでは最小値を求めるが、op(operation=演算内容、デフォルトはmin的関数)、
    # ie(identity element単位元)を指定することも可能(f.e: op=operator.add, ie=0)
    import math
    def __init__(self, arg1, op=lambda x, y:x if x < y else y, ie=math.inf):
        self.op = op
        self.ie = ie

        if type(arg1) == int:
            default_list = []
            self.length = arg1
        else:
            default_list = list(arg1)
            self.length = len(arg1)

        # 上部構造分の配列個数(オフセット)を求める
        self.offset = 2 ** ((self.length - 1).bit_length())

        # 木の初期化。上部構造は1-indexedで使用していくことにする
        self.tree = [self.ie] * (self.offset * 2)
        if default_list:
            self.tree[self.offset:self.offset+self.length] = default_list
            self.refresh()

    # 全体の再計算(愚直に下から……)
    def refresh(self):
        for idx in range(self.offset - 1, 0, -1):
            self.tree[idx] = self.op(self.tree[idx*2], self.tree[idx*2+1])

    # 値のセット、及び関連する部分の再計算
    def set(self, idx, value):
        idx = idx + self.offset
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            old = self.tree[idx]
            new = self.op(self.tree[idx*2], self.tree[idx*2+1])
            if old == new:
                break
            else:
                self.tree[idx] = new

    # データ領域の値をindexに応じて返す
    def get(self, x):
        return self.tree[x+self.offset]
        
    # 半開区間[left, right)における欲しい値(アレっすよ、アレ)を求める
    # 一番下の階層からボトムアップ的に必要な部分を見ていく
    def rangeq(self, left, right):
        # 区間がおかしなときは、エラー代わりに単位元でも返しておく？
        if left >= right:
            return self.ie
        
        # 左端と右端から上位を見ていく
        result = self.ie
        left = left + self.offset
        right = right + self.offset - 1

        # 左端と右端が重なるとこまで演算
        # 最後に重なった場合も、下記の条件分けから一度しか演算されない(念の為)
        while left <= right:
            # 左端は、自身が親の右側の子の時(=ノード番号が奇数のとき)にだけ
            # (自分が左側の時は次の演算に含まれるため)演算する
            if left % 2 == 1:
                result = self.op(result, self.tree[left])
            # 一段上に移動
            left = (left + 1) // 2

            # 右端は、自身が親の左側の(以下略
            # C++だとみんな半開放の値を生かして--rightとかエレガントに書いてるけど……
            if right % 2 == 0:
                result = self.op(result, self.tree[right])
            right = (right - 1) // 2
       
        return result
    
    # 全領域を対象にした計算値を返す
    def allq(self):
        return self.tree[1]

def main():
    N = int(input())
    S = input()
    Q = int(input())
    queries = [list(input().split()) for _ in range(Q)]

    # ある文字を持っているかどうかを010010...といった
    # ビットで管理する。そのため、あらかじめ文字→インデックスの
    # 辞書を作成しておく。
    # ちなみに{chr(i+97):i for i in range(26)}
    # みたいな書き方もできる
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_to_idx = {k:v for k, v in zip(alphabet, range(26))}

    # セグメント木を作成
    # 各ビット毎にある文字を持っているかどうかを管理するので、
    # op = (x, y) => x | y となる
    segtree = Segment_Tree(N, lambda x, y: x | y, ie=0)

    # 値を直接配列に放り込んでいった後、初期化する
    for i, c in enumerate(S):
        segtree.tree[segtree.offset + i] = 1<<char_to_idx[c]
    segtree.refresh()

    for op, a, b in queries:
        if op == '1':
            segtree.set(int(a)-1, 1<<char_to_idx[b])
        else:
            tmp_r = segtree.rangeq(int(a)-1, int(b))
            print(bin(tmp_r).count('1'))

main()
