
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n) (or maybe O(n^2) because of the sorting of each word?)
        Space Complexity: O(n)
    """
    hash_map = {}
    for word in strings:
        new_string = ''.join(sorted(word))
        if new_string in hash_map:
            hash_map[new_string].append(word)
        else:
            hash_map[new_string] = [word]
    
    words_list = []
    for value in hash_map.values():
        words_list.append(value)
    
    return words_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n) (not completely sure about the complexity of the sorted() method though)
        Space Complexity: O(n)
    """

    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    new_hash = {}
    for key, value in hash_map.items():
        if value in new_hash:
            new_hash[value].append(key)
        else:
            new_hash[value] = [key]

    occurrences = sorted(new_hash.keys(), reverse=True)

    k_nums = []
    for item in occurrences:
        k_nums += new_hash[item]

    while len(k_nums) > k:
        k_nums.pop()

    return k_nums


def valid_sudoku(table):
    """
    This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) (because the sudoku is a set size, so it will never change?)
        Space Complexity: O(1)
    """
    # checks columns
    for i in range(9):
        hash_column= {}
        for row in table:
            if row[i].isnumeric():
                if row[i] in hash_column:
                    return False
                else:
                    hash_column[row[i]] = 1
    # checks rows
    for row in table:
        hash_row = {}
        for i in range(9):
            if row[i].isnumeric():
                if row[i] in hash_row:
                    return False
                else:
                    hash_column[row[i]] = 1
    # checks squares
    square = []
    for row in range(3):
        r = row*3
        for col in range(3):
            c = col*3

            square.append(table[r][c:c+3])
            square.append(table[r+1][c:c+3])
            square.append(table[r+2][c:c+3])

            square_hash = {}
            print(square)
            for line in square:
                for index in line:
                    if index.isnumeric():
                        if index in square_hash:
                            return False
                        else:
                            square_hash[index] = 1
            square = []

    return True
