
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
"""
    hash_table = {}
    for word in strings:
        # sort each char of word into a list
        sorted_word = sorted(word)
        # join the sorted chars back into a word
        anagram = ''.join(sorted_word)
        if anagram in hash_table:
            # if anagram is already a key in hash table,
            # append the current word to the value
            hash_table[anagram].append(word)  
        else:
            # else, assign anagram as a key in the hash table
            # and the current word as its value in list form
            hash_table[anagram] = [word]
    print(hash_table)     
    # return just the list of all the values
    return list(hash_table.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not nums:
        return nums

    hash_table = {}
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    print(hash_table.items())

    # didn't grasp 100%, so listed out steps
    # grab key-value pairs in hash_table
    # let key be the second value in tuple
    # reverse sort tuples by value into list
    sorted_by_value = sorted(hash_table.items(), key = lambda tuple: tuple[1], reverse=True)                                      
    print(sorted_by_value)
    result = []
    # for first k nums in reversed list of tuples
    # append the value, or first value of tuple to result list
    for i in range(k):                             
        result.append(sorted_by_value[i][0])
    return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?

        2powerful4me
    """
    pass

