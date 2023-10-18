import math, random

def solution(A, F, M):
    total_roll_number = (len(A) + F)
    print(total_roll_number)
    total_roll_sum = (total_roll_number * M)
    print(total_roll_sum)
    f_sum = (total_roll_sum - sum(A))
    print(f_sum)
    

solution([3, 2, 4, 3], 2, 4)