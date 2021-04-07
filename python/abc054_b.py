# AtCoder Beginner Contest 054 B - Template Matching
# https://atcoder.jp/contests/abc054/tasks/abc054_b
# tag: グリッド 基礎問題

# 制限が 1 <= M <= N <= 50 なので、左上をあわせて
# 一致しているかどうかを確認する、素朴な全探索 O(N^2 * M^2) で
# 十分間に合う。よって、グリッドの中から目標と一致している部分を
# 見つける、基礎的な問題ということになる。

def main():
    N, M = map(int, input().split())
    field_a = [input() for _ in range(N)]
    field_b = [input() for _ in range(M)]

    # 画像 A の(sx, sy) を左上として、画像 B と一致するかどうかを確認
    # for ～ else を用いた多重ループ脱出を用いている。
    # ……というか、実は他に for ～ else 使ってる人を見たことがない
    # 気もするので、せっかくだから詳しめにコメントを入れてみた。
    # よくわからない人は普通にフラッグで管理するのがオススメ。
    for sy in range(N-M+1):
        for sx in range(N-M+1):

            # (sx, sy) から各行を確認していく
            for dy in range(M):
                # 文字列をスライスして一致するかどうかを確認
                row_a = field_a[sy + dy][sx:sx+M]
                if field_b[dy] != row_a:
                    break

            # 全部一致したら、'Yes'にして終了 - (1)
            else:
                result = 'Yes'

                # この break は sx のループに対して働く
                break
        else:
            continue

        # 直前の else: continue のおかげで
        # ここには (1) で sx のループが break した後にしか来ない
        # これは、sy のループを break する
        break

    # 全探索が完了しても一致するところが無ければ 'No'
    else:
        result = 'No'

    print(result)

main()
