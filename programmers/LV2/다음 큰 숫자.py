def solution(n):
    n_bin_cnt = bin(n)[2:].count("1")
    next = n
    for _ in range(1000001):
        next += 1
        next_bin_cnt = bin(next)[2:].count("1")

        if n_bin_cnt == next_bin_cnt:
            break

    return next