
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    word_dict = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]
        else:
            word_dict[sorted_word].append(word)

    return list(word_dict.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    sorted_num_freq = sorted(
        num_dict.keys(), key=lambda x: num_dict[x], reverse=True)

    return sorted_num_freq[:k]


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
