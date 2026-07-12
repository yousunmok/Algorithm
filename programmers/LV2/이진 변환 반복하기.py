def solution(s):
    ans = []
    length = cnt = 0
    while True:
        temp = s.replace("0", "")
        length += (len(s) - len(temp))
        s = bin(len(temp))[2:] # Ob제거하기 위해 2번째부터
        cnt += 1

        if s == "1": break

    ans.append(cnt)
    ans.append(length)

    return ans

