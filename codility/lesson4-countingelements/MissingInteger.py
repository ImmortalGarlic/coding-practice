'''
Lesson4 - MissingInteger
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    if A[-1] <= 0:
        return 1
    if A[0] > 1:
        return 1
    length = len(A)
    candidate = 0
    for idx in range(length-1):
        # if syntax hell!
        if A[idx] <= 0:
            continue
        if idx >= 1 and A[idx] - A[idx-1] > 1:
            candidate = A[idx-1] + 1
            break
        if A[idx+1] - A[idx] > 1:
            candidate = A[idx] + 1
            break
    if candidate == 0:
        return A[-1] + 1
    else:
        return candidate