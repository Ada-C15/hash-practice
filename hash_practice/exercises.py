
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n log n)
    """
    letters_hash = {}

    for word in strings: 
        anagram_sorted = "".join(sorted(word)) 
        if anagram_sorted in letters_hash: 
            letters_hash[anagram_sorted].append(word)
        else: 
            letters_hash[anagram_sorted] = [word]

    return list(letters_hash.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    highest_k_hash = {}
    if nums == []:
        return nums

    for num in nums:
        if num in highest_k_hash:
            highest_k_hash[num] += 1
        else:
            highest_k_hash[num] = 1

    sorted_k_values = []
    for i in range(k):
        highest_freq_value = max(highest_k_hash, key=highest_k_hash.get)
        sorted_k_values.append(highest_freq_value)
        highest_k_hash.pop(highest_freq_value)

    return sorted_k_values


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

