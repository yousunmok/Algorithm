def solution(s):
    s = s.lower()
    arr = s.split(" ")

    ans = []
    for st in arr:
        if st:
            ans.append(st[0].upper() + st[1:])
        else:
            ans.append("")

    return " ".join(ans)