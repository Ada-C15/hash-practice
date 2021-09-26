
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    hash_table = {}
    for word in strings:
        sort_word = ''.join(sorted(word))
        if sort_word in hash_table:
            hash_table[sort_word].append(word)
        else:
            hash_table[sort_word] = [word]

    return list(hash_table.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums:
        return []

    hash_table = {}
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    print(hash_table)
    sort_values = sorted(hash_table, key=lambda x: hash_table[x], reverse=True)
    print(sort_values)

    elements = []
    for i in range(0, k):
        elements.append(sort_values[i])

    print(elements)
    return elements


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

