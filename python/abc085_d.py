# AtCoder Beginner Contest 085 D - Katana Thrower
# https://atcoder.jp/contests/abc085/tasks/abc085_d
# tag: 考察 事前ソート 累積和

# 攻撃方法としては、適切な回数振ってから、
# 最後にまとめて投げると仮定する。

# 投げずに振る刀については、振ったときの攻撃力が
# 最大のものを振る以外の意味がない。

# また、投げる刀については、投げたときの攻撃力が
# 最大のものから順番に投げていくことになる。

# 投げる本数は 0 ～ N 本になるので、これを
# 全探索する。

def main():
    N, H = map(int, input().split())
    katanas = [list(map(int, input().split())) for _ in range(N)]

    # 振るときの攻撃力を求める（最大値）
    swings = [k[0] for k in katanas]
    max_swing = max(swings)

    # 投げたときの攻撃力を高い順にソートしておき、
    # 累積和を取っておく
    throws = [k[1] for k in katanas]
    throws.sort(reverse=True)
    csum_throws = [0]
    for d in throws:
        csum_throws.append(csum_throws[-1] + d)
    
    result = 10**9

    # cnt_throw 本投げるとして……
    for cnt_throw in range(N+1):
        tmp_h = H - csum_throws[cnt_throw]

        # 投げた後、体力が残っていれば刀を振る
        # （実際の動作としては振ってから投げることになる）
        if tmp_h > 0:
            tmp_r = cnt_throw + (tmp_h - 1) // max_swing + 1
        
        # 投げた刀だけで倒せる場合は、振る攻撃は不要
        else:
            tmp_r = cnt_throw

        if tmp_r < result:
            result = tmp_r
        
    print(result)

main()
