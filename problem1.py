# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Task
You are given a 2-D array of size NXM. Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None

Input Format
The first line contains the space separated values of N and M. The next NN lines contains M space separated integers.

Output Format
First, print the mean. Second, print the var. Third, print the std.

Sample Input
2 2
1 2
3 4

Sample Output
[ 1.5  3.5]
[ 1.  1.]
1.11803398875

"""
import numpy
if __name__ == '__main__':
    arr = input().split()
    N, M = int(arr[0]), int(arr[1])
    new_arr = []
    for i in range(0, N):
        row = list(map(int, input().split()))
        new_arr.append(row)
    print(numpy.mean(new_arr, axis=1))
    print(numpy.var(new_arr, axis=0))
    std = numpy.std(new_arr, axis=None)
    if std == 0:
        print("0.0")
    else:
        print(f"{std:.11f}")
