# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

array = [10, 15, 3, 7]
k = 17

# Here is a solution that is functional, but is a brute force approach that should not be applied in production
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def PairAddSlow(array, k):
    for i in array:
        for j in array:
            if i + j == k:
                return True
    return False


# Here is a solution that turns the array into a set, then find if K-array[i] is present in the set
# Time Complexity O(n)
# Space Complexity O(n)
def PairAdd(array, k):
    mySet = set(array)

    for i in array:
        if k - i in mySet:
            return True

    return False
