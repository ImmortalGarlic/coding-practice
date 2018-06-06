'''
Lesson4 - PermCheck
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length = len(A)
    unique_length = len(set(A))
    if length != unique_length:
        return 0
    else:
        if min(A) != 1 or max(A) != length:
            return 0
        else:
            return 1