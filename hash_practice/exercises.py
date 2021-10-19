
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """

    if not strings:
        return []

    word_dict = {}
    for word in strings:
        sorted_word = sorted(word)
        new_word = ''.join(sorted_word)
        if new_word in word_dict:
            word_dict[new_word].append(word)
        else:
            word_dict[new_word] = [word]

    return [word for word in word_dict.values()]


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: o(n log n) 
        Space Complexity: o(n)  
    """

    a_dict = {}
    return_list = []
    if not nums:
        return return_list

    for i in range(0, len(nums)):
        if nums[i] in a_dict:
            a_dict[nums[i]] += 1
        else:
            a_dict[nums[i]] = 1

    sorted_dict = sorted(a_dict.items(), key=lambda tup: tup[1], reverse=True)

    for j in range(0, k):
        return_list.append(sorted_dict[j][0])

    return return_list


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
