def solution(S):
    initial_dots = 0
    for segment in S:
        if segment != ".":
            break
        initial_dots += 1
    patchable = S[initial_dots:]
    # print(patchable)

    groups = [(patchable[i:i+3]) for i in range(0, len(patchable), 3)]

    # print(groups)

    count = 0

    for i in groups:
        if "X" in i:
            count += 1
    
    return count

# solution('X.XXXXX.X.')
# solution('XX.XXX..')
# solution('XXXX')
# solution('.X...XX')