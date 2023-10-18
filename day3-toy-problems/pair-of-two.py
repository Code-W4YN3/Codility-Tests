def solution(S):
    numbers = []
    for i in range(0, len(S)):
        numbers.append((max([int(S[i] + S[i+1]), int(S[i+1] + S[i+2])])))
        i=+ 3   
    print(numbers)

solution("43798")