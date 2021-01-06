# %%

def old_fib(n):
    memo = {}
    if n < 3:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = old_fib(n-1) + old_fib(n-2)
        return memo[n]


old_fib(25)
# %%
memo
# %%
