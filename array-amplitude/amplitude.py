def solution(A):
    if len(A) > 1:
        return (max(A) - min(A))

solution([10, 2, 44, 15, 39, 20])