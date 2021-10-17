
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in dict:
                dict[sorted_string].append(string)
        else:
            dict[sorted_string] = [string]
    return_list = []
    for key, value in dict.items():
        return_list.append(value)
    return return_list



def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    frequency_dict = {}
    if nums == []:
        return nums

    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    return_list = []
    for i in range(k):
        highest_value = max(frequency_dict, key=frequency_dict.get)
        return_list.append(highest_value)
        frequency_dict.pop(highest_value)
    return return_list



# optional
def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

