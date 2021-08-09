# dfs を用いて再帰で順に生成することも出来る。
def main():
    N = int(input())
    ab = 'abcdefghijklmnopqrstuvwxyz'

    result = []

    def dfs(x):
        if x == 1:
            return [[0]]
        
        result = []

        for l in dfs(x-1):
            for i in range(max(l)+2):
                result.append(l + [i])

        return result
    
    for r in dfs(N):
        print(''.join(ab[i] for i in r))

main()
