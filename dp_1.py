# D - Digits Parade
# https://atcoder.jp/contests/abc135/tasks/abc135_d

# ポイント
# 123 = 100 + 20 + 3 = 9 + 7 + 3 = 6 mod 13と桁ごとに分割して考えられる
# →　桁で区切って漸化式化し、テーブルを埋める

S = input()
N = 13
mod = 1000000007
mul = 1

# 1?2?3なら 0 -> 3 -> ?3 -> 2?3 -> ...と逐次的に計算していく
dp = [0 for i in range(N)]
dp[0] = 1 # dp[k] = 13で割ったあまりがkになるパターン数

for s in S[::-1]:
    next_dp = [0 for i in range(N)]
    if s == "?":
        for k in range(10):
            for j in range(N):
                next_dp[(k*mul+j)%N] += dp[j]
                next_dp[(k*mul+j)%N] %= mod
    else:
        k = int(s)
        for j in range(N):
            next_dp[(k*mul+j)%N] += dp[j]
            next_dp[(k*mul+j)%N] %= mod
    
    mul *= 10
    mul %=N
    dp = next_dp
    
print(dp[5])
