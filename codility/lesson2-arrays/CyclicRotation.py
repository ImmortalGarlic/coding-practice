'''
Lesson2 - CyclicRotation
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    length = len(A)
    if length <= 1:
        return A
    new_array = [None] * length
    for i in range(length):
        new_array[(i+K)%length] = A[i]
    return new_array