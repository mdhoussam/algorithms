"""
Define a bitonic sequence as a sequence of integers such that:
    x_1 < ... < x_k > ... > x_n-1 for some k, 0 <= k < n.
For example:
    1, 2, 3, 4, 5, 4, 3, 2, 1
is a bitonic sequence. Write a program to find the largest element in such a
sequence. In the example above, the program should return "5".
We assume that such a "peak" element exists.
"""

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
def find_highest_number(A):
    low = 0
    high = len(A) -1
    #require at least 3 element fora valide sequence
    if len(A) <3:
        return None
    while low<=high:
        mid = (low + high)//2

        mid_lef = A[mid - 1] if mid - 1 > 0 else float(" -inf")
        mid_right = A[mid+1] if mid +1 <len(A) else float("inf")
        if mid_lef<A[mid] and mid_right>A[mid]:
            low = mid+1
        elif mid_lef>A[mid] and mid_right<A[mid]:
            hight = mid -1
        elif mid_lef<A[mid] and mid_right <A[mid]:
            return A[mid]
        else:
            return None
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
x = find_highest_number(A)
print(x)