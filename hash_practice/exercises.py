
def grouped_anagrams(d1):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # empty dictionary for anagrams together 
    dict = {} 

    # traversal 
    for val in d1: 
        # sorts list
        key = ''.join(sorted(val)) 

        if key in dict.keys(): 
            dict[key].append(val) 
        else: 
            dict[key] = [] 
            dict[key].append(val) 

    # traverse dictionary and join keys together 
    result = []
    for key,value in dict.items(): 
        # result = result + ' '.join(value) + ' '
        result.append(value)
    return result 

def top_k_frequent_elements(numbers, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: o(n)
        Space Complexity: o(n)
    """
    freq_map = {}
    if numbers == []:
        return numbers
    for i in numbers:
        if i in freq_map:
            freq_map[i] += 1
        elif i not in freq_map:
            freq_map[i] = 1
    
    new_list = []
    for i in range(k):
        highest_value = max(freq_map, key=freq_map.get)
        new_list.append(highest_value)
        freq_map.pop(highest_value)
    return new_list

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

