from Counting_sort import counting_sort

def radix_sort(numbers, d):
    """
    Using a counting as the stable
    sort to perform a radix sort
    """
    output = [] #Initializing outout array

    for index, num in enumerate(numbers): #Looping through numbers to add leading 0 if needed
        if len(str(num)) < d: #A leading 0 needs to be added
            numbers[index] = ('0')*(d-len(str(num))) + str(num) #Adding leading 0
        else: #No leading zero is needed
            numbers[index] = str(num) #Converting to str for sorting
    for i in range(1, d+1): #Looping for sorting
        key = lambda x: int(x[-i]) #Defining key dependent on value of d
        numbers = counting_sort(numbers, key) #Sorting
    for j in numbers: #Converting number bakc to intergers
        output.append(int(j)) #Appending int value to output
    return output #Returning output



"""
"Tests for radix_sort()"

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3), '\n')
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1), '\n')
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))

"Expected output"

[329, 355, 436, 457, 657, 720, 839]

[720, 355, 436, 457, 657, 329, 839]

[720, 329, 436, 839, 355, 457, 657]
"""
