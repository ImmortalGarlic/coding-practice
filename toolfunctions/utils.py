'''
1. Fibonacci function
TODO: return the i-th fib number
'''
def fib_generator(max_range):
    init_fib = [1, 1]
    cnt = 0
    while cnt <= max_range:
        init_fib.append(init_fib[-1]+init_fib[-2])
        cnt += 1
    return init_fib

'''
2. Check if a given number is prime
TODO: the space complexity is terrible, improve this later
'''
def prime_checker(number):
    if number == 1 or number == 2:
        return True
    else:
        if 0 in list(map(lambda x: number%x, list(range(1, number)))):
            return False
        else:
            return True

'''
3. Quick sort
'''
def quicksort(array):
    low = []
    middle = []
    high = []
    
    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i < pivot:
                low.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                high.append(i)
        return quicksort(low)+middle+quicksort(high)
    else:
        return array
