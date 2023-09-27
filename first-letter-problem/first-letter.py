def first_letter(S):
    count = 0
    for i in range(len(S)):
        swapped = S[1:] + S[0]
        S = swapped
        if(swapped[-1] == swapped[0]):
            count += 1
    return count

first_letter("abbaa")