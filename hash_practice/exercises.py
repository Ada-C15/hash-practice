import heapq


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(1)
        Space Complexity: O(n)
    """

    hash_table = {}

    for word in strings:
        key = ''.join(sorted(word))
        if key not in hash_table.keys():
            hash_table[key] = []

        hash_table[key].append(word)
    values_list = []
    for value in hash_table.values():
        values_list.append(value)
    return values_list


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(1)
        Space Complexity: O(n)
    """
    nums_dict = {}
    frequency_values = {}

    for number in nums:
        if number not in nums_dict:
            nums_dict[number] = 1
        nums_dict[number] += 1
    for key, value in nums_dict.items():
        if value not in frequency_values:
            frequency_values[value] = [key]
        else:
            frequency_values[value].append(key)

    k_result = []
    for num in range(len(nums), 0, -1):
        if num in frequency_values:
            k_result.extend(frequency_values[num])
        if len(k_result) >= k:
            break
    return k_result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same
        row, column or 3x3 subgrid
        Time Complexity: O(1)
        Space Complexity: O(n)
    """

    for i in range(9):
        row = {}
        column = {}
        block = {}
        row_box = 3 * (i//3)
        column_box = 3 * (i % 3)
        for j in range(9):
            if table[i][j] != '.' and table[i][j] in row:
                return False
            row[table[i][j]] = 1
            if table[j][i] != '.' and table[j][i] in column:
                return False
            column[table[j][i]] = 1
            rc = row_box+j//3
            cc = column_box + j % 3
            if table[rc][cc] in block and table[rc][cc] != '.':
                return False
            block[table[rc][cc]] = 1
    return True

