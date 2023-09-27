Initially, string S of length N is given. Then N-1 operations are applied to it: move the first letter of S to the end. How many times is the first letter of S the same as the last letter?

For example, given S = "abbaa", the obtained sequence of strings is:

abbaa -> bbaaa -> baaab -> aaabb -> aabba

Three of them have the same first and last letter.

## Write a function:

def solution(S)

that, given a string S of length N, consisting of letters 'a' and/or 'b', returns the number of times the first letter is the same as the last in the obtained sequence of strings.

Examples:

1. Given S = "abbaa", the function should return 3, as described above.

2. Given S = "aaaa", the function should return 4. The first and last letters are always the same.

3. Given S = "abab", the function should return 0. The first and last letters are always different.

### Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..200,000];
string S is made only of the characters 'a' and/or 'b'.
