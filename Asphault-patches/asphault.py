def solution(S):
    patchable = S[S.index('X'):]
    # print(patchable)

    groups = [(patchable[i:i+3]) for i in range(0, len(patchable), 3)]

    # print(groups)

    count = 0

    for i in groups:
        if "X" in i:
            count += 1
    # print(count)
    return count

solution('X.XXXXX.X.')
solution('XX.XXX..')
solution('XXXX')
solution('.X...XX')