
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams_hash = {}

    for word in strings: 
        sorted_word = "".join(sorted(word)) 
        if sorted_word in anagrams_hash: 
            anagrams_hash[sorted_word].append(word)
        else: 
            anagrams_hash[sorted_word] = [word]

    return list(anagrams_hash.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    frequency_hash = {}
    if nums == []:
        return nums

    for num in nums:
        if num in frequency_hash:
            frequency_hash[num] += 1
        else:
            frequency_hash[num] = 1

    return_list = []
    for i in range(k):
        highest_value = max(frequency_hash, key=frequency_hash.get)
        return_list.append(highest_value)
        frequency_hash.pop(highest_value)

    return return_list

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
