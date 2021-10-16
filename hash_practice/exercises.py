# Time Complexity: ?
# Space Complexity: O(n)
def grouped_anagrams(strings):
    # check to see if the list is empty
    words = []
    if not strings:
        return words
    # sort every item in list
    sorted_list = []
    for word in strings:
        x = sorted(word)
        y = ''.join(x)
        sorted_list.append(y)

    # declare empty hash
    word_dict = {}
    # iterate over list, if item is not in dict, add a new key (sorted item), and value in a list, unsorted
    index = 0
    for word in sorted_list:
        if word not in word_dict:
            word_dict[word] = [strings[index]]
            index += 1
        else:
            word_dict[word] += [strings[index]]
            index += 1

    for value in word_dict.values():
        words.append(value)

    return words


def top_k_frequent_elements(nums, k):
    # build a dict with keys being item in nums, value being frequency
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    num_list = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)

    i = 0
    return_list = []
    while i < k:
        return_list.append(num_list[i][0])
        i += 1

    return return_list

    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    pass


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
