
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n3)  - is that really true?!?!  eeekk
        Space Complexity: O(n2)
    """
    final_anagram_lists = []
    anagram_set = {}
    for word1 in strings:           # for each with index loop goes through the value 
        if word1 in anagram_set:
            continue
        temp_anagrams = [word1] 
        anagram_set[word1] = 1
        for word2 in strings:
            if compare_anagrams(word1, word2):
                if word2 not in anagram_set:
                    temp_anagrams.append(word2)
                    anagram_set[word2] = 1
        final_anagram_lists.append(temp_anagrams)
        temp_anagrams = []
    return final_anagram_lists

def compare_anagrams(str1, str2):
    str1_hash = {}
    str2_hash = {}
    for letter in str1:
        if letter in str1_hash:
            str1_hash[letter] += 1
        else:
            str1_hash[letter] = 1
    
    for letter in str2:
        if letter in str2_hash:
            str2_hash[letter] += 1
        else:
            str2_hash[letter] = 1
            
    if str1_hash == str2_hash:
        return True
    else:
        return False

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    return_arr = []
    nums_dict = {}
    if len(nums) == 0:
        return []
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else: 
            nums_dict[num] += 1
    for i in range (0,k):
        highest_key = max(nums_dict, key=nums_dict.get)
        return_arr.append(highest_key)
        nums_dict.pop(highest_key)

    return return_arr

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n)  or is it O(1) since its of a fixed size?
        Space Complexity: O(n) or is it O(1) since its of a fixed size?
    """
    for row in range(0,9):
        row_dict = {}
        for col in range(0,9):
            tile = table[row][col]
            if tile == ".":
                continue
            elif tile not in row_dict:
                row_dict[tile] = 1
            else:
                print(row_dict)
                return False 
    for col in range (0,9):
        col_dict = {}
        for row in range(0,9):
            tile = table[row][col]
            if tile == ".":
                continue
            elif tile not in col_dict:
                col_dict[tile] = 1
            else:
                print(col_dict)
                return False 

    return True



table = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]


print(valid_sudoku(table))
