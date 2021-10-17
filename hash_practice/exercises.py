def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # expected_answer = [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    # helper_function?
    def check_permutation(str1, str2):          # helper_function
        frequency_hash = {}
        frequency_hash_2 = {}
        
        for letter in str1:
            if letter in frequency_hash:
                frequency_hash[letter] += 1
            else:
                frequency_hash[letter] = 1
        
        for letter in str2:
            if letter in frequency_hash_2:
                frequency_hash_2[letter] += 1
            else:
                frequency_hash_2[letter] = 1
                
        # if len(str1) == len(str2):
        if frequency_hash == frequency_hash_2:
            return True
        else:
            return False

    final_anagram_lists = []
    hash_set = {}

    for i, word1 in enumerate(strings):           # for each with index loop goes through the value 
        if word1 in hash_set:
            continue
        temp_anagrams = [word1] 
        hash_set[word1] = 1
        for j, word2 in enumerate(strings):
            # if j > i:
            if check_permutation(word1, word2):
                if word2 not in hash_set:
                    temp_anagrams.append(word2)
                    hash_set[word2] = 1

        final_anagram_lists.append(temp_anagrams)
        temp_anagrams = []

    return final_anagram_lists

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# answer = grouped_anagrams(words)

# For-loop:
# // for i in len(strings):
# //   word = strings[i]

# For-each loop:
# // for word in strings:

# For each with index:
# // for word, i in enumerate(strings):


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    pass
    # top_k_elements = []
    # frequency_hash = {}
    return_arr = []
    nums_dict = {}
    if len(nums) == 0:
        return []
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] +=1
    for i in range (0,k):
        highest = max(nums_dict, key=nums_dict.get)
        
        return_arr.append(highest)
        nums_dict.pop(highest)

    return return_arr


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass
    # what is sudoku? 
    # a puzzle in which players insert the numbers one to nine into a 
    # grid consisting of nine squares subdivided into a further 
    # nine smaller squares in such a way that every number appears 
    # once in each horizontal line, vertical line, and square.

# The same digit cannot appear twice or more in the same

# rows =

# columns =

# 3x3 subgrid = 

    
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
        
    for col in range(0,9):
        col_dict = {}
        for row in range (0,9):
            title = table[row][col]
            if tile == ".":
                continue
            elif tile not in col_dict:
                col_dict[tile] = 1
            else:
                print(col_dict)
                return False
        box = None
        boxlet = None
        for box in range (0,9):
            box_dict = {}
            print("--------")
            for boxlet in range(0,9):
                row = box * 3 + boxlet
                col = boxlet


    return True
