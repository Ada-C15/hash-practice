
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

        Pseudocode solution 2:
        1.
        2.
        3.
        4.

        Time Complexity: ?
        Space Complexity: ?
    """
    if len(nums) == k:
        return nums
    if len(nums) == 0:
        return []


def top_k_frequent_elements_alternative_solution(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.

        pseudocode solution 1:
        This solution would work for both sorted and not sorted input array.
        0. Go over the input array and create unique element frequency hash table.
        1. Go over the frequency hash table and create an array of tuples: [(x1,y1),(x2,y2),(x3,y3),...(xn,yn)]
        where x1, x2, ..., xn - unique integer elements from the input array
        and y1, y2, ..., yn their frequencies relatively.
        2. Sort new array by key, where key is frequency (second element of each tuple).
        3. Iterate over sorted array k times to form the output by grabbing first element of each tuple and appending it to the resulting array

        Time Complexity: O(nlogn) (sorting)
        Space Complexity: O(n+k) ?

    """
    if len(nums) == k:
        return nums
    if len(nums) == 0:
        return []

    frequency_map = {}
    for num in nums:
        if frequency_map.get(num):
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    num_freq_list = []
    for num, frequency in frequency_map.items():
        num_freq_list.append((num, frequency))

    sorted_num_freq_list = sorted(
        num_freq_list,
        key=lambda tup: tup[1],
        reverse=True)

    result = []
    for i in range(k):
        result.append(sorted_num_freq_list[i][0])

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
    pass


# grouped_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
top_k_frequent_elements([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5], 3)
