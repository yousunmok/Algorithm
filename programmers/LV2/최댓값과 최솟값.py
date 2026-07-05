def solution(s):
    arr = list(map(int, s.split()))
    mn = min(arr)
    mx = max(arr)
    return str(mn) + " " + str(mx)