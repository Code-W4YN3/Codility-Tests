// function solution(R){
//     let total_list = []
//     let joined_holes= []
//     for(i in R){
//         if(i != 0){
//             joined_holes.append(i)
//         }else{
//             joined_holes = []
//         }
//         if(i not in total_list){
//             total_list.append(joined_holes)
//         print(joined_holes)
//         }
//     max_list = []
//     for i in total_list:
//         if(len(i) > 0):
//             max_list.append((len(i)) * max(i))
//         else:
//             max_list.append(0)
//     print(max_list)
//     print(max(max_list))
//     }
// }