
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams_map = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams_map:
            anagrams_map[sorted_word] = [word]
        else:
            anagrams_map[sorted_word].append(word)
    return list(anagrams_map.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    frequency_hash = {}
    most_frequent_items = []
    if len(nums) == 0:
        return []
    for item in nums:
        if item in frequency_hash:
            frequency_hash[item] += 1
        else:
            frequency_hash[item] = 1
    
    for i in range(k):
        highest_frequency = max(frequency_hash, key = lambda num: frequency_hash[num])
        most_frequent_items.append(highest_frequency) 
        frequency_hash.pop(highest_frequency)
    return most_frequent_items


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n2)
        Space Complexity: O(n2)
    """
    
    #row
    for row in range(9):
        row_map = {}
        for column in range(9):
            tile = table[row][column]
            if tile == ".":
                continue
            elif tile not in row_map:
                row_map[tile] = 1
            else:
                return False

    #column
    for column in range(9):
        column_map = {}
        for row in range(9):
            tile = table[row][column]
            if tile == ".":
                    continue
            elif tile not in column_map:
                column_map[tile] = 1
            else:
                return False

    #sub-boxes
    def squares(R, C):
        squares_map = {}
        for row in range(R, R+3):
            for column in range(C, C+3):
                tile= table[row][column]
                if tile == ".":
                    continue
                elif tile not in squares_map:
                    squares_map[tile] = 1             
                else:
                    return False
        return True
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not squares(row, column):
                return False
    return True



