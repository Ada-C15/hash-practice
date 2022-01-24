
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagram_table = {}
    anagram_values = []

    for word in strings:
        key = ''.join(sorted(word))
        if key in anagram_table.keys():
            anagram_table[key].append(word)
        else:
            anagram_table[key] = []
            anagram_table[key].append(word)
    
    for value in anagram_table.values():
        anagram_values.append(value)
    
    return anagram_values

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    numbers_dict = {}
    frequency_dict = {}  
    return_list = []

    for num in nums:
        if num in numbers_dict:
            numbers_dict[num] += 1
        else:
            numbers_dict[num] = 1

    for key, value in numbers_dict.items():
        if value not in frequency_dict:
            frequency_dict[value] = [key]
        else:
            frequency_dict[value].append(key)

    for i in range(len(nums), 0, -1): 
        if i in frequency_dict:
            return_list.extend(frequency_dict[i])

        if len(return_list) >= k:
            break

    return return_list


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    for i in range(len(table)):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(len(table)):
            if table[i][j]!='.' and table[i][j] in row:
                return False
        row[table[i][j]] = 1
        if table[j][i]!='.' and table[j][i] in column:
            return False
        column[table[j][i]] = 1
        rc= row_cube+j//3
        cc = column_cube + j%3
        if table[rc][cc] in block and table[rc][cc]!='.':
            return False
        block[table[rc][cc]]=1
    return True

