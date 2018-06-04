'''
Lesson1 - BinaryGap
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    cnt = binary.count('0')
    if cnt == 0:
        return 0
    while cnt > 0:
        if '1' + '0' * cnt + '1' in binary:
            return cnt
        else:
            cnt -= 1
    if cnt == 0:
        return 0