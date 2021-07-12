# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
#   While there is a solution that solves the problem without division, it does not improve the time or space efficiency (actully makes space worse) and thus not an optimal solution

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# The solution to this problem is fairly straight forward and is fairly time efficient, but space efficiency could be better if there is a solution that can be done in place
# Time Complexity: O(n)
# Space Complexity: O(n)


def MultAllButSelf(array):
    total = 1
    for num in array:
        total = total * num

    outputArray = []
    for num in array:
        outputArray.append(total / num)
    return outputArray


print(MultAllButSelf(input))