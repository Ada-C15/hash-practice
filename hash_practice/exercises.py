import heapq
import re


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
    values = []
    for value in hash_table.values():
        values.append(value)
    return values


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(1)
        Space Complexity: O(n)


        Input: nums = [1,1,1,2,2,3], k = 2 (Amount of returned elements of the final array)
        Output: [1,2] 2 numbers returned
    """

    number_frequency = {}
    # {1: 4, 2: 2, 3: 1}

    frequency_list = {}  # flip the values and keys
    # {4: [1], 2: [2], 1: [3]}

    # Count the amount of times the numbers appear
    for i in nums:
        if i not in number_frequency:
            number_frequency[i] = 1
        else:
            number_frequency[i] += 1

    #  put items into frequency list by value: key pairs so that they are filled
    for key, value in number_frequency.items():
        if value not in frequency_list:
            frequency_list[value] = [key]
        else:
            # if two keys are the same frequency, add to same value
            frequency_list[value].append(key)

    result = []  # [1, 2]
    for range_i in range(len(nums), 0, -1):  # range visual[6,5,4,3,2,1,0]
        if range_i in frequency_list:  # if the index matches the key
            # add value of key to result list
            result.extend(frequency_list[range_i])

        if len(result) >= k:  # if len of result list greater or equeal to k / '2', break/stop
            break

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
