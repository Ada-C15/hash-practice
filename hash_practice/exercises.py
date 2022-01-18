
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * m log(m))  (m is the max length of the word) 
        Space Complexity: O(n)
    """
    string_dict = {}
    # see if the sorted value is a key in the dict and if not add the element in the dict we are on as an array.
    for unsorted_word in strings:
        sorted_word = str(sorted(unsorted_word))
        if sorted_word in string_dict:
            string_dict[sorted_word].append(unsorted_word)
        else:
            string_dict[sorted_word] = [unsorted_word]
    return list(string_dict.values())
    # If the sorted value is in the dict add the element we are on to the key's value with the existing array.


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
        # Create an empty dict
    num_dict = {}
    # Iterate through nums and add count as the value of the dictionary.
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    # Once we have the dict full we will find the values with the largest keys k times.
    sorted_list = set(sorted(num_dict.values(), reverse=True)[:k])

    result = []
    for key, value in num_dict.items():
        if len(result) == k:
            return result
        if value in sorted_list:
            result.append(key)
    return result
    # return the keys in a list


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    rows_dict = {}
    col_dict = {}

    for i in range(9):
        col_dict[i] = {}
    for row_index in range(len(table)):
        rows_dict[row_index] = {}
        row = table[row_index]
        for index in range(len(row)):
            if row[index] == ".":
                continue
            else:
                if row[index] in rows_dict[row_index]:
                    return False
                else:
                    rows_dict[row_index][row[index]] = index

                if row[index] in col_dict[row_index]:
                    return False
                else:
                    col_dict[row_index][row[index]] = index
    return True

