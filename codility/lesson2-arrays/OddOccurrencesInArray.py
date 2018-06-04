'''
Lesson2 - OddOccurrencesInArray
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    cnt = 0
    while cnt < len(A):
        if A.count(A[cnt]) % 2 != 0:
            return A[cnt]
        else:
            cnt += 1