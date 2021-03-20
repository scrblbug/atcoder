# AtCoder Beginner Contest 128 C - Switches
# https://atcoder.jp/contests/abc128/tasks/abc128_c
# tag: ビット全探索

# 一見とんでもなく難しく見えるが、制限を見てみると
# 1 <= N, M <= 10 と少ない。
# 結局スイッチの状態は、2^10 = 1024 通りに過ぎず、
# 電球の数も少ないので、全探索を行いつつ状態変化を
# 確認すればいい。
# 解き方はいろいろあるが、いずれにせよビット全探索を行うと便利＆楽＆速い。

# 以下全体としてビット操作に慣れるために、やや複雑に見える方法で
# 解いている。ただ、問題の肝はスイッチの状態に応じたビット全探索に
# あると思われるので、そこだけ押さえれば、後は好きなやり方で
# いいのではないかと……。

def main():
    N, M = map(int, input().split())

    # 最初の数字は個数なので、あらかじめ抜いておく
    lamp_dat = [list(map(int, input().split()))[1:] for _ in range(M)]

    # スイッチを中心に考えることにしたので、ランプ毎に与えられている情報を、
    # スイッチ毎にどのランプに繋がっているかに変換している。
    # ついでに 1-indexed を 0-indexed にしておく。
    switches = [[] for _ in range(N)]
    for i, sw_list in enumerate(lamp_dat):
        for sw in sw_list:
            switches[sw-1].append(i)

    # ライトが全て点灯する条件を、二進法で数値に変換して持っておく
    # ことで、あとで条件を比較するのが楽になる。
    # ビット探索の関係上、順番が逆になる（ランプ 1 が下の桁になる）
    # ので注意。
    lit_cond = int(''.join(input()[::-1].split()), 2)

    # ビット全探索
    # スイッチON: 1
    # スイッチOFF: 0
    # として、二進法で 0000... ～ 1111... まで探索を行う
    result = 0
    for st in range(1<<N):
        # もちろん、ランプ毎にいくつスイッチが押されているかを確認し、
        # 2 で割って点灯しているかどうか確認するという素直な
        # 実装もあるが、ここでは少し違ったやり方で解いている。

        # 各ランプのステータスをビットで管理していく
        lamp_status = 0

        # スイッチ毎に ON になっているかどうかを確認し、
        # ON なら lamp_status を変化させる
        for i in range(N):
            # スイッチは ON ？
            if 1<<i & st:
                for lmp in switches[i]:
                    # あるランプにつながっているスイッチが押されるたびに、
                    # 該当する lamp_status のビットを xor で反転させている。
                    lamp_status = lamp_status ^ (1<<lmp)
        # 全部点灯してるなら、答えに +1
        if lamp_status == lit_cond:
            result += 1

    print(result)

main()