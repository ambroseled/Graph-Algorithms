def key_positions(seq, key):
    """
    Returns array filled with locations
    at which the item equal to the index of the locations
    should be placed
    """
    k = max(key(i) for i in seq) #Getting value of k which is the max key value
    positions = [0]*(k+1) #Intializing postions array filled with zeros
    for j in seq: #Looping through each value in the sequence
        positions[key(j)] += 1 #Incrementing the counter at postion of current key
    sum = 0 #Intializing sum variable
    for q in range(k+1): #Looping k + 1 times to alter postions array
        positions[q], sum = sum, sum + positions[q] #Updating index for each key postion
    return(positions) #Returning key postions array


def sorted_array(seq, key, positions):
    """helper function for performinga counting sort"""
    output = [0]*len(seq) #Intializing output array

    for i in seq: #Looping through each value in sequence
        output[positions[key(i)]] = i #Adding sequence value to correct index in output array
        positions[key(i)] += 1 #Incrementing postion of current sequence value
    return output #Returning output array


def counting_sort(iterable, key):
    positions = key_positions(iterable, key) #Getting key postions
    return sorted_array(iterable, key, positions) #Sorting and returning array




"""
Tests for key_positions()
print(key_positions([0, 1, 2], lambda x: x), '\n')
print(key_positions([2, 1, 0], lambda x: x), '\n')
print(key_positions([1, 2, 3, 2], lambda x: x), '\n')
print(key_positions([5], lambda x: x), '\n')
print(key_positions(range(-3,3), lambda x: x**2), '\n')
print(key_positions(range(1000), lambda x: 4), '\n')
print(key_positions([1] + [0] * 100, lambda x: x))


"Expected output"

[0, 1, 2]

[0, 1, 2]

[0, 0, 1, 3]

[0, 0, 0, 0, 0, 0]

[0, 1, 3, 3, 3, 5, 5, 5, 5, 5]

[0, 0, 0, 0, 0]

[0, 100]
"""

"""
Tests for sorted_array()
print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]), '\n')
print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]), '\n')
print(sorted_array([100], lambda x: x, [0]*101))

"Expected output"

[1, 2, 3]

[1, 2, 2, 2, 3]


[100]
"""

"""
Tests for Counting_Sort()
import operator
Tests for counting_sort()
objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
print(", ".join(object[0] for object in counting_sort(objects, key)))

"Expected output"

d, b, c, a

"""
