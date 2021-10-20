
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nlogn) - beacuse of the sort
        Space Complexity: O(n)
    """
    repeated_words = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word not in repeated_words:
            repeated_words[sorted_word] = [word]
        else:
            repeated_words[sorted_word].append(word)
    
    anagrams_list = []
    for words in repeated_words.values():
        anagrams_list.append(words)
    
    return anagrams_list



def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    final_list = []
    if len(nums) == 0:
        return final_list
    repeated_nums = {}
    most_repeated = 0
    for val in nums:
        if val in repeated_nums:
            repeated_nums[val] += 1
        else:
            repeated_nums[val] = 1
        if repeated_nums[val] > most_repeated:
            most_repeated = repeated_nums[val]
    
    order_repeated = {}
    for key, val in repeated_nums.items():
        if val in order_repeated:
            order_repeated[val].append(key)
        else:
            order_repeated[val] = [key]
        
    while most_repeated > 0 and len(final_list) < k:
        if most_repeated in order_repeated:
            for num in order_repeated[most_repeated]:
                final_list.append(num)
        most_repeated -= 1
    
    return final_list





def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1) - the grid size will not change.
        Space Complexity: O(n)
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


    subgrid = 3
    for row in range(subgrid):
        for col in range(subgrid):
            block_dict = {}
            block = [
                table[subgrid*row][subgrid*col:subgrid*col+3], 
                table[subgrid*row+1][subgrid*col:subgrid*col+3],
                table[subgrid*row+2][subgrid*col:subgrid*col+3]
            ]
            for segment in block:
                for elem in segment:
                    if elem != ".":
                        if elem in block_dict:
                            return False
                        else:
                            block_dict[elem] = 1

    return True

