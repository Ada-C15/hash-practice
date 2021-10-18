
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    prime_numbers = [
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103]
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if len(strings) == 0:
        return []

    def construct_mapping_letter_to_number(letters, numbers):
        map = {}
        for index in range(len(letters)):
            map[letters[index]] = numbers[index]
        return map

    letter_to_prime_mapping = construct_mapping_letter_to_number(
        alphabet, prime_numbers)
    hash_table = {}

    for string in strings:
        hash_index = 1
        for character in string:
            hash_index = hash_index * letter_to_prime_mapping[character]

        if not hash_table.get(hash_index):
            hash_table[hash_index] = [string]
        else:
            hash_table[hash_index].append(string)

    return list(hash_table.values())


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


grouped_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
