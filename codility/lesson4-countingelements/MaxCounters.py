'''
Lesson4 - MaxCounters
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_val = 0
    for idx, a in enumerate(A):
        if a <= N:
            try:
                counters[a-1] += 1
                max_val = max(counters)
            except IndexError:
                continue
        elif a == N+1:
            counters = [max_val] * N
    return counters