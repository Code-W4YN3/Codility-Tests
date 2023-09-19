def solution(R):
    total_list = []
    joined_holes= []
    for i in R:
        if i != 0:
            joined_holes.append(i)
        else:
            joined_holes = []
        total_list.append(joined_holes)
    unique = []
    for i in total_list:
        if i not in unique:
            unique.append(i)
    print(unique)
    max_list = []
    for i in unique:
        max_list.append((len(i)) * max(i))
    print(max(max_list))
        
solution([0, 2, 1, 1, 0, 4, 1])
solution([1, 4, 1, 0, 5, 2, 3, 0, 8])