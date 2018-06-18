'''
Lesson5 - CountDiv
https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    return len([x for x in range(A, B+1) if x%K == 0])