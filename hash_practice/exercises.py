


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """ 

    
    anagrams = {}
    if strings == []:
        return []
    for word in strings:
        hash = 0
        for letter in word:
            unicode_char = ord(letter)
            hash += unicode_char
        if hash in anagrams:
            anagrams[hash].append(word)
        else:
            anagrams[hash] = [word]


    return create_anagram_list(anagrams)

def create_anagram_list(anagrams):
    grouped_anagrams = []
    for key, value in anagrams.items():
        grouped_anagrams.append(value)
    return grouped_anagrams

    # split each word 
    # get ascii for each letter
    # add letters/ascii values together for each word
    # make that the key and add word to anagram/value list 
    # return anagram list for each key  

    

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    pass


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

