'''
Lesson3 - OddOccurrencesInArray
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

Correctness 20% ???? WTF

▶ empty_and_single 
empty list and single element ✘WRONG ANSWER 
got 0 expected 1
▶ missing_first_or_last 
the first or the last element is missing ✘RUNTIME ERROR 
tested program terminated with exit code 1
▶ single 
single element ✘RUNTIME ERROR 
tested program terminated with exit code 1
▶ double 
two elements ✘RUNTIME ERROR 
tested program terminated with exit code 1
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        if A[0] != 1:
            return 1
            
    A = sorted(A)
    for idx in range(len(A)):
        if idx + 1 != A[idx]:
            return idx + 1