
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    result = {}

    for i in strings:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]

    return list(result.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    number_frequency = {}
    frequency_list = {}

    for i in nums:
        if i not in number_frequency:
            number_frequency[i] = 1
        else:
            number_frequency[i] += 1

    for key,value in number_frequency.items():

        if value not in frequency_list:
            frequency_list[value] = [key]
        else:
            frequency_list[value].append(key)

    result = []

    for i in range(len(nums),0,-1):
        if i in frequency_list:
            result.extend(frequency_list[i])
        if len(result) >= k:
            break

    return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    for i in range(9):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
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

