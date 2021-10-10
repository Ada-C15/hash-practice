
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: 
        O(m * n log n) with m number of words and n average number of chars in a word
        
        Space Complexity: O(m * n)
    """
    anagram_dict = {}
    for string in strings:
        # this will take O(n logn) time with n being the number of chars in a word
        sorted_chars = "".join(sorted(list(string))) 
        anagram_dict[sorted_chars] = anagram_dict.get(sorted_chars, []) + [string]

    return list(anagram_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n logn) n number of elements
        Space Complexity: O(n)
    """
    freq_dict = {}
    for elem in nums:
        freq_dict[elem] = freq_dict.get(elem, 0) + 1
    
    return sorted(freq_dict.keys(), key= lambda x: freq_dict[x], reverse=True)[:k]


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) Since it's a constrained problem (81 elements), it's constant time
        Space Complexity: O(1)
    """
    # check rows
    for row in table:
        row_dict = {}
        for elem in row:
            if elem != ".":
                row_dict[elem] = row_dict.get(elem, 0) + 1
                if row_dict[elem] > 1:
                    return False
    # check columns
    for i in range(9):
        col_dict = {}
        for j in range(9):
            elem = table[j][i]
            if elem != ".":
                col_dict[elem] = col_dict.get(elem, 0) + 1
                if col_dict[elem] > 1:
                    return False

    # check squares
    for i in range(3):
        for j in range(3):
            square_dict = {}
            for x in range(3):
                for y in range(3):
                    elem = table[i*3 + x][j*3 + y]
                    if elem != ".":
                        square_dict[elem] = square_dict.get(elem, 0) + 1
                        if square_dict[elem] > 1:
                            return False
    return True

