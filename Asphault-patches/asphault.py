def solution(S):
    count = 0
    B = len(S)
    i = 0

    while i < B: 

         if S[i] == "X":
            count +=1
            i += 3
         else:
             i+=1
    
    return count

solution('X.XXXXX.X.')
solution('XX.XXX..')
solution('XXXX')
solution('.X...XX')