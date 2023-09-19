
There is a road consisting of N segments (numbered from 0 to N-1) described by an array R of integers. The K-th segment is described by an integer R[K]. If the segment is smooth (there is no pothole in it), then R[K] = 0; otherwise it contains a pothole of depth R[K]. Consecutive potholes join together and create a larger group of potholes.

The pothole indicator is the number of consecutive single potholes that have joined into a pothole group, multiplied by the depth of the deepest pothole among them. For example, the indicator for a group of three consecutive joined potholes of sizes [1, 4, 1] is 3 * 4 = 12.

What is the largest pothole indicator on the entire road?

## Write a function

Write a function solution(R) that, given an array R of N integers, returns the largest pothole indicator on the road.

## Examples

1. Given R = [0, 2, 1, 1, 0, 4, 1], the function should return 8. The potholes in the fragment [2, 1, 1] join into one pothole group. It is made of three segments and the deepest pothole among them is of depth 2, so its pothole indicator is equal to 3 * 2 = 6. The potholes in the fragment [4, 1] join into another pothole group. It is made of two consecutive potholes and the deepest pothole among them is of depth 4, so its pothole indicator is equal to 2 * 4 = 8.

2. Given R = [1, 4, 1, 0, 5, 2, 3, 0, 8], the function should return 15. The consecutive potholes that join into three larger pothole groups are as follows:

* [1, 4, 1] with indicator 3 * 4 = 12;
* [5, 2, 3] with indicator 3 * 5 = 15;
* [8] with indicator 1 * 8 = 8.

The largest pothole indicator is 15.

3. Given R = [9, 8, 7, 0, 0, 0, 2, 3, 6, 4], the function should return 27. The consecutive potholes that join into two larger pothole groups are as follows:

* [9, 8, 7] with indicator 3 * 9 = 27;
* [2, 3, 6, 4] with indicator 4 * 6 = 24.

The largest pothole indicator is 27.

4. Given R = [0, 0, 0], the function should return 0. There are no potholes on the road, so the highest pothole indicator is equal to 0.

## Write an efficient algorithm for the following assumptions:

* N is an integer within the range [1..100,000];
* each element of array R is an integer within the range [0..9].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


This Markdown can be used to create a README file for your code, or to document the question in a different way.