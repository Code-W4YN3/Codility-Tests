# Task 1: Even word
In an even word, each letter occurs an even number of times.

Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.

Examples:

1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).

2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).

3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).

Write an efficient algorithm for the following assumptions:

 

N is an integer within the range [0..200,000];
string S is made only of lowercase letters (a−z). 

# Task 2: Pair of Two Digit Sums

You are given a string S consisting of N digits. What is the largest sum of two two-digit fragments of S? The selected fragments cannot overlap.

### Write a function:

def solution(S)

that, given a string S, returns the largest sum of two two-digit numbers that are non-overlapping fragments of S.

Examples:

1. Given S = "43798", the function should return 141. The chosen fragments are "43" and "98": "43 7 98"

2. Given S = "00101", the function should return 10. The chosen fragments are "00" and "10": "00 10 1". Note that fragments "01" and "10" cannot be chosen as they overlap.

3. Given S = "0332331", the function should return 66. The chosen fragments are "33" and "33": "0 33 2 33 1".

4. Given S = "00331", the function should return 34. The chosen fragments are "03" and "31": "0 03 31"

Assume that:

N is an integer within the range [4..100];
string S is made only of digits (0−9).
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# Task 3: Angry Frogs

There are N blocks, numbered from 0 to N-1, arranged in a row. A couple of frogs were sitting together on one block when they had a terrible quarrel. Now they want to jump away from one another so that the distance between them will be as large as possible. The distance between blocks numbered J and K, where J ≤ K, is computed as K − J + 1. The frogs can only jump up, meaning that they can move from one block to another only if the two blocks are adjacent and the second block is of the same or greater height as the first. What is the longest distance that they can possibly create between each other, if they also chose to sit on the optimal starting block initially?

### Write a function:

def solution(blocks)

that, given an array blocks consisting of N integers denoting the heights of the blocks, returns the longest possible distance that two frogs can make between each other starting from one of the blocks.

Examples:

1. Given blocks = [2, 6, 8, 5], the function should return 3. If starting from blocks[0], the first frog can stay where it is and the second frog can jump to blocks[2] (but not to blocks[3]).

"Graphical representation of example 1."

2. Given blocks = [1, 5, 5, 2, 6], the function should return 4. If starting from blocks[3], the first frog can jump to blocks[1], but not blocks[0], and the second frog can jump to blocks[4].

"Graphical representation of example 2."

3. Given blocks = [1, 1], the function should return 2. If starting from blocks[1], the first frog can jump to blocks[0] and the second frog can stay where it is. Starting from blocks[0] would result in the same distance.

"Graphical representation of example 3."

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..200,000];
each element of array blocks is an integer within the range [1..1,000,000,000].