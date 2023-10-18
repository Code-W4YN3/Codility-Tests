def solution(S):
    setS = set(S)
    # print(setS)
    count = 0
    for i in setS:
        if(S.count(i) % 2 != 0):
            count += 1
    # print(count)
    return count

# solution("acbcbba")
# solution("axxaxa")
# solution("aaaa")