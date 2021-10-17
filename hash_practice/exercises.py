
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    anagram_list = []

    word_dict = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    for value in word_dict.values():
        anagram_list.append(value)

    return anagram_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n) (This may actually be O(n^2) because of the max function on line 46, but I'm not sure)
        Space Complexity: O(n)
    """

    if len(nums) == 0:
        return []

    frequent_elements = []
    element_dict = {}

    for elem in nums:
        if elem in element_dict:
            element_dict[elem] += 1
        else:
            element_dict[elem] = 1

    while len(frequent_elements) < k:
        highest_key = max(element_dict, key=element_dict.get)
        frequent_elements.append(highest_key)

        del element_dict[highest_key]

    return frequent_elements

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
