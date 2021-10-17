
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    anagram_list = []

    word_dict = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    for value in word_dict.values():
        anagram_list.append(value)

    return anagram_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n) (This may actually be O(n^2) because of the max function on line 46, but I'm not sure)
        Space Complexity: O(n)
    """

    if len(nums) == 0:
        return []

    frequent_elements = []
    element_dict = {}

    for elem in nums:
        if elem in element_dict:
            element_dict[elem] += 1
        else:
            element_dict[elem] = 1

    while len(frequent_elements) < k:
        highest_key = max(element_dict, key=element_dict.get)
        frequent_elements.append(highest_key)

        del element_dict[highest_key]

    return frequent_elements

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same
        row, column or 3x3 subgrid
        Time Complexity: O(1) (because it is always a 9x9 grid??)
        Space Complexity: O(1)
    """
    # validates rows in sudoku table
    for row in table:
        # could this dict be a set, because we are just checking for duplicates?
        row_dict = {}
        for square in row:
            if square != ".":
                if square not in row_dict:
                    row_dict[square] = 1
                else:
                    return False

    # validates columns in sudoku table
    for col in range(0, len(table)):
        col_dict = {}
        for square in table[col]:
            if square != ".":
                if square not in col_dict:
                    col_dict[square] = 1
                else:
                    return False

    # validates smaller 3x3 tables within larger sudoku table
    # this is horrendously bad time complexity, but if the table is always 9x9, does it matter?
    for row in range(3):
        for col in range(3):
            block_dict = {}
            block = [
                table[3*row][3*col:3*col+3],
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
