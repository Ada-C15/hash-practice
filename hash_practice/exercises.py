
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagram_dict = {}
    output = []
    
    for word in strings:
        word_key = "".join(sorted(word))
        if (word_key in anagram_dict):
            anagram_dict[word_key].append(word)
        else:
            anagram_dict[word_key] = [word]
    
    for word_key in anagram_dict:
        output.append(anagram_dict[word_key])
        
    return output

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nk)
        Space Complexity: O(n)
    """
    frequency_dict = {}
    result = []
    if not nums:
        return []

    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    for i in range(k):
        highest_value = max(frequency_dict, key=frequency_dict.get)
        result.append(highest_value)
        frequency_dict.pop(highest_value)
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
    for row in table:
        row_dict = {}
        for square in row:
            if square != ".":
                if square not in row_dict:
                    row_dict[square] = 1
                else:
                    return False

    for col in range(0, len(table)):
        col_dict = {}
        for square in table[col]:
            if square != ".":
                if square not in col_dict:
                    col_dict[square] = 1
                else:
                    return False

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

