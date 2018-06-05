'''
Lesson4 - FrogRiverOne
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    existed = []
    for idx, a in enumerate(A):
        if a not in existed:
            existed.append(a)
            if len(existed) == X:
                return idx
        else:
            pass
    if len(existed) < X:
        return -1