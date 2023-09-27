
A non-empty array A consisting of N integers is given. The amplitude of this array is defined as the largest possible difference between two of its elements, i.e.:

amplitude(A) = max{ A[P] − A[Q] : 0 ≤ P, Q < N }

## Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns its amplitude.

For example, given array A such that:

  A[0] = 10
  A[1] = 2
  A[2] = 44
  A[3] = 15
  A[4] = 39
  A[5] = 20
the function should return 42.

### Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [0..5,000,000].