'''
Lesson3 - TapeEquilibrium
https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    summ = sum(A)
    length = len(A)
    cnt = 1
    temp = 2*A[0]
    
    if length == 1:
        return 0
    
    while cnt < length:
        res = abs(summ - temp)
        if abs(summ - temp - 2*A[cnt]) < res:
            temp += 2*A[cnt]
            cnt += 1
        else:
            return res