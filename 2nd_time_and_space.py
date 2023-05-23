# 6 kyu
# Find the odd int


# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(arr):
    freq_map = {}
    for integer in arr:
        if integer in freq_map:
            freq_map[integer] += 1
        else:
            freq_map[integer] = 1
    
    for integer, frequency in freq_map.items():
        if frequency % 2 != 0:
            return integer
        
        
# so the loop iterates through each element is "arr" and in the worst case where all elements in arr a distinct and the loop will iterate "n" times, where "n" is the length of "arr". the ops in the loop are checking/updating and are constant time ops so this is a complexity of the first loop is O(n).
# the space complexity on second loop is  <= the first one and teh complexity is still O(n)
# the Total Tim/Spa is still just O(n) so LINEAR over all.
