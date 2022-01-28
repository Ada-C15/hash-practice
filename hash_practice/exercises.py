
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """

    result = []
    hash = {}

    for word in strings:
        new_word = "".join(sorted(word))
        if new_word in hash:
            hash[new_word].append(word)
        else:
            hash[new_word] = [word]

    for value in hash.values():
        result.append(value)
    
    return result
    
            


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not nums or k <= 0: 
        return []

    hash = {}
    result = []

    for n in nums:
        if n not in hash: 
            hash[n] = 1
        else: 
            hash[n] += 1
        
    while len(result) < k:
        biggest = max(hash, key=hash.get)
        result.append(biggest)

        del hash[biggest]
    
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
    hash = {}
    for n in range(1, 10):
        hash[str(n)] = 0

    #check rows first
    for row in table:
        for sq in row:
            if sq != ".":
                if hash[sq] == 0:
                    hash[sq] = 1
                elif hash[sq] != 0:
                    return False
        #wipe clean 
        for n in range(1, 10):
            hash[str(n)] = 0
    
    #wipe clean
    for n in range(1, 10):
        hash[str(n)] = 0

    #check columns
    row = 0 
    col = 0
    for col in range(9):
        for row in range(9):
            sq = table[row][col]
            if sq != ".":
                if hash[sq] == 0:
                    hash[sq] = 1
                elif hash[sq] != 0:
                    return False
        #wipe clean
        for n in range(1, 10):
            hash[str(n)] = 0

    #wipe clean
    for n in range(1, 10):
        hash[str(n)] = 0

    #check 3x3 tables
    r = 0
    c = 0

    while (r < 9 and c < 9): 
        for row in range(r, r+3):
            for col in range(c, c+3):
                sq = table[row][col]

                if sq != ".":
                    if hash[sq] == 0:
                        hash[sq] = 1
                    elif hash[sq] != 0:
                        return False
            
        #go to next block
        # reset r, c
        r += 3
        c += 3
        # wipe hash clean
        for n in range(1, 10):
            hash[str(n)] = 0

    return True




