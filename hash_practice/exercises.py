
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    if not strings:
        return []

    hold_words = {}

    for word in strings:
        sorted_bit = sorted(word)
        new_bit = ''.join(sorted_bit)

        if new_bit in hold_words:
            hold_words[new_bit].append(word)
        else:
            hold_words[new_bit] = [word]

    return [word for word in hold_words.values()]

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    temp_dict = {}
    for_return = []

    if not nums:
        return for_return

    for i in range(0, len(nums)):
        if nums[i] in temp_dict:
            temp_dict[nums[i]] += 1
        else:
            temp_dict[nums[i]] = 1

    sorted_dict = sorted(temp_dict.items(), key=lambda tuple: tuple[1], reverse=True) # check with TA

    for j in range(0, k):
        for_return.append(sorted_dict[j][0])

    return for_return


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

