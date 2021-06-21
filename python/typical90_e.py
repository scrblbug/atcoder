from numpy import matrix
def main():
    N, B, K = map(int, input().split())
    nums = list(map(int, input().split()))

    mat = [[0] * B for _ in range(B)]

    for r in range(B):
        nr = (r * 10) % B
        for n in nums:
            mat[(nr+n)%B][r] = 1
    
    mat = matrix(mat)

    base = [1] + [0] * (B-1)
    base = matrix([[n] for n in base])

    print((mat**N) * base)

main()

