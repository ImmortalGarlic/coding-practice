'''
Lesson1 - BinaryGap
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
'''
	
int solution(int N) {
    // write your code in C++14 (g++ 6.2.0)
    int MaxGap = 0;
    int GapCount = 0;
    int flag = 0;
    while (N > 0) {
        if ((N & 1) == 1 and flag == 1) {
            MaxGap = std::max(MaxGap, GapCount);
            GapCount = 0;
        }
        else if ((N & 1) == 1 and flag == 0) {
            flag = 1;
        }
        else if ((N & 1) != 1 and flag == 1) {
            GapCount += 1;
        }
        N >>= 1;
    }
    return MaxGap;
}
