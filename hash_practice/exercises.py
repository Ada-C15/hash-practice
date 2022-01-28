
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    basket = {} 

    for value in strings: 
        key = ''.join(sorted(value)) 
        if key in basket.keys(): 
            basket[key].append(value) 
        else: 
            basket[key] = [] 
            basket[key].append(value) 

    result = []
    for key,value in basket.items(): 
        result.append(value)
    return result 


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: O(n)
    """
    freq_map = {}
    if nums == []:
        return nums
    for i in nums:
        if i in freq_map:
            freq_map[i] += 1
        elif i not in freq_map:
            freq_map[i] = 1
    
    result = []
    for i in range(k):
        highest_value = max(freq_map, key=freq_map.get)
        result.append(highest_value)
        freq_map.pop(highest_value)
    return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n2)
        Space Complexity: O(1)
    """
    for i in range(9):
        board = {}
        for j in range(9):
            if table[i][j] in board:
                return False
            elif table[i][j] is not '.':
                board[table[i][j]]
                return True

    # Check columns
    for j in range(9):
        for i in range(9):
            if table[i][j] in board:
                return False
            elif table[i][j] is not '.':
                board[table[i][j]]
                return True

    for subI in range(0, 9, 3):
        for subJ in range(0, 9, 3):
            if table[i][j] in board:
                return False
            elif table[i][j] is not '.':
                board[table[i][j]]
                return True
    return True