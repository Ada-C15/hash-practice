
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log m)
        Space Complexity: O(n)
    """
    if len(strings) < 1:
        return []

    anagrams = dict()

    for string in strings:
        key_string = "".join(sorted(string))

        if key_string in anagrams:
            anagrams[key_string].append(string)
        else:
            anagrams[key_string] = [string]

    return [anagrams[group] for group in anagrams]


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: At least O(n) assuming that max() is an O(1) look up but I strongly suspect it isn't
        Space Complexity: At least O(n + k)
        (Not sure about the big O here becuase I'm not certain how max works in this case)
    """
    if len(nums) < 1:
        return []

    freq_dict = dict()

    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    top_k = []
    for i in range(k):
        top_k.append(max(freq_dict, key=freq_dict.get))
        freq_dict.pop(top_k[i])

    return top_k


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

