def solution(n):
    answer = 0
    sm = 0
    rt = lt = 1
    for _ in range(2 * n + 1):
        if sm <= n:
            sm += rt
            rt += 1
        else:
            sm -= lt
            lt += 1

        if sm == n:
            answer += 1

    return answer