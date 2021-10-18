
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    dict = {}
    result = []

    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dict:
                dict[sorted_word].append(word)
        else:
            dict[sorted_word] = [word]

    for key, value in dict.items():
        result.append(value)

    return result


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    d = {}
    cur_max = 1
    result = []
    
    # create dict to get freqency of each number
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    while k > 0:
    
        # find current max
        for key, value in d.items():
            if value >= cur_max:
                cur_max = value
                    
        # only decrease k by 1 when a number is added to the result array
        for key, value in d.items():
            if value == cur_max:
                result.append(key)
                k -= 1
                d[key] = 0

        # continue to decrease cur_max by 1 to see if matches any value in dict       
        cur_max -= 1
 
    return result


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

