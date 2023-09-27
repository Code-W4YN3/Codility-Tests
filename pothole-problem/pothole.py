def solution(R):
    total_list = []
    joined_holes= []
    for i in R:
        if i != 0:
            joined_holes.append(i)
        else:
            joined_holes = []
        if i not in total_list:
            total_list.append(joined_holes)
    max_list = []
    for i in total_list:
        if(len(i) > 0):
            max_list.append((len(i)) * max(i))
        else:
            max_list.append(0)
    return(max(max_list))
        
solution([0, 2, 1, 1, 0, 4, 1])
solution([1, 4, 1, 0, 5, 2, 3, 0, 8])
solution([9, 8, 7, 0, 0, 0, 2, 3, 6, 4])
solution([0, 0, 0])