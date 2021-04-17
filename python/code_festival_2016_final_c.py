# CODE FESTIVAL 2016 Final C - Interpretation
# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_c
# tag: Union_Find

# 複数の通訳を介して通訳が可能ということを踏まえると、
# Union_Find を用いて、話されている言語全てが一つのグループに
# なっているかどうかを確認すればいい。

class Union_Find:
    # 親管理リストと高さ管理リストを初期化し、
    # 要素N個のUnion-Find森を作成する。
    # 親管理リストは、基本的には自分のひとつ上の親を表すが、
    # 値が負の場合には、自身が最上位の親(リーダー)であることを表し、
    # 自分を含めたグループの人数を管理することとする
    def __init__(self, N):
        self.parent = [-1] * N
        self.rank = [0] * N
        self.group_count = N
        self.N = N

    # xの所属するグループのリーダーを返す
    def find(self, x):
        # 自分自身がリーダーなら、自分を返す
        if self.parent[x] < 0:
            return x

        # 再帰的に捜索し、見つかれば繋ぎ変えておく
        # (計算量が増える＝面倒くさいので)高さ管理は行わない
        par = self.find(self.parent[x])
        self.parent[x] = par
        return par

    # xとyのグループを統合する
    def unite(self, x, y):
        # それぞれのリーダーに対する操作を行うことになる
        x = self.find(x)
        y = self.find(y)

        # リーダーが同じなら何もする必要がない
        if x == y:
            return (-1, -1)

        # 木の高さが同じ場合：
        # グループの人数を合計しつつ適当に繋ぎ、繋げられた方の高さを1増やす
        if self.rank[x] == self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.rank[x] += 1
            self.group_count -= 1
            return (x, y)

        # 木の高さが違うなら、低い方を高い方につなぐ
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.group_count -= 1
        return (x, y)

    # xとyが同じグループかどうかを調べる
    def samep(self, x, y):
        return self.find(x) == self.find(y)

    # xの所属するグループのメンバー数を返す
    def get_member_count(self, x):
        x = self.find(x)
        return -self.parent[x]

######## ここからメイン ########
def main():
    N, M = map(int, input().split())
    lang_sets = [list(map(int, input().split()[1:])) for _ in range(N)]

    # Union_Find とは別に、話されている言語のチェックに set を用意
    uft = Union_Find(M + 1)
    used = set()

    # ある人が言語 A, B, C を話している時、A, B, C を set に入れつつ、
    # (A, B), (A, C) といった感じで Union_Find で統合する。
    for ls in lang_sets:
        used.add(ls[0])
        for l in ls[1:]:
            used.add(l)
            uft.unite(ls[0], l)
    
    # 使われていた言語の数と、（なにか適当な）話されていた言語のグループの
    # メンバー数が一致すれば、一つのグループになっている
    if len(used) == uft.get_member_count(lang_sets[0][0]):
        print('YES')
    else:
        print('NO')

main()
