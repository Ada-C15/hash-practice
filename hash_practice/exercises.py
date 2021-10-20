
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    freq_hash = {}

    for word in strings:
        key = ''.join(sorted(word))
        if key not in freq_hash.keys():
            freq_hash[key] = []

        freq_hash[key].append(word)
    values_list = []
    for value in freq_hash.values():
        values_list.append(value)
    return values_list


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if nums == []:
        return nums

    freq_table = {}
    for num in nums:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    max_freq = 0
    common_elemnts = []
    for key, value in freq_table.items():

        if freq_table[key] > max_freq:
            max_freq = freq_table[key]
            common_elemnts.append(key)
        elif freq_table[key] == max_freq:
            common_elemnts.append(key)

    return common_elemnts


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same
        row, column or 3x3 subgrid
        Time Complexity: O(n)3 
        Space Complexity: O(n)
    """

    for col in range(0, len(table)):
        column_hash = {}
        for square in table[col]:
            if square != ".":
                if square not in column_hash:
                    column_hash[square] = 1
                else:
                    return False

    for row in range(3):
        for col in range(3):
            block_dict = {}
            block = [
                table[3*row][3*col:3*col+3],  # finding index in sudoku board
                table[3*row+1][3*col:3*col+3],
                table[3*row+2][3*col:3*col+3]
            ]
            for segment in block:
                for elem in segment:
                    if elem != ".":
                        if elem in block_dict:
                            return False
                        else:
                            block_dict[elem] = 1

    return True
