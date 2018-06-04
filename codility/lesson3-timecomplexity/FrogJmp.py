'''
Lesson3 - FrogJmp
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    return (Y-X)//D + ((Y-X)%D != 0)