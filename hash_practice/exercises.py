
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other

        The idea in general is to create hash function, that will return same hashing index  for anagrams.

        Time Complexity: O(n)
        Space Complexity: O(n)
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

    def construct_cellsping_letter_to_number(letters, numbers):
        cells = {}
        for index in range(len(letters)):
            cells[letters[index]] = numbers[index]
        return cells

    letter_to_prime_cellsping = construct_cellsping_letter_to_number(
        alphabet, prime_numbers)
    hash_table = {}

    for string in strings:
        hash_index = 1
        for character in string:
            hash_index = hash_index * letter_to_prime_cellsping[character]

        if not hash_table.get(hash_index):
            hash_table[hash_index] = [string]
        else:
            hash_table[hash_index].append(string)

    return list(hash_table.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.

        Pseudocode solution 2:
        1.Go over the input array and create unique element frequency hash table.
        2. Go over unique element frequency hash table and create new hash table with key being frequencies and values being list of unique element that share that same frequency.
        3. While iterating over unique element frequency hash table calculate the max availible frequency.
        4. Iterate over key-value pairs in descending order (starting from max frequency) and construct resulting array by adding k elements to it.

        This solution would work for both sorted and not sorted input array.

        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if len(nums) == k:
        return nums
    if len(nums) == 0:
        return []
    frequency_cells = {}
    for num in nums:
        if frequency_cells.get(num):
            frequency_cells[num] += 1
        else:
            frequency_cells[num] = 1

    max_frequency = 0
    key_frequency_cells = {}
    for num, frequency in frequency_cells.items():
        if not key_frequency_cells.get(frequency):
            key_frequency_cells[frequency] = [num]
        else:
            key_frequency_cells[frequency].append(num)
        if frequency > max_frequency:
            max_frequency = frequency

    result = []
    while max_frequency > 0 and len(result) < k:
        if key_frequency_cells.get(max_frequency):
            for num in key_frequency_cells[max_frequency]:
                if len(result) < k:
                    result.append(num)
        max_frequency -= 1

    return result


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

    frequency_cells = {}
    for num in nums:
        if frequency_cells.get(num):
            frequency_cells[num] += 1
        else:
            frequency_cells[num] = 1

    num_freq_list = []
    for num, frequency in frequency_cells.items():
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

        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    dimension = len(table)
    sub_box_dimension = dimension // 3

    def validate_row(row):
        cells = set()
        for cell in row:
            if cell == ".":
                continue
            if cell in cells:
                return False
            else:
                cells.add(cell)
        return True

    def validate_column(table, column_number, dimension):
        cells = set()
        for row in range(dimension):
            cell = table[row][column_number]
            if cell == ".":
                continue
            if cell in cells:
                return False
            else:
                cells.add(cell)
        return True

    def validate_3_by_3_sub_box(table, start_row, start_column):
        # sub_box_dimension = 3
        cells = set()
        for row in range(start_row, start_row + sub_box_dimension):
            for column in range(
                    start_column,
                    start_column +
                    sub_box_dimension):
                cell = table[row][column]
                if cell == ".":
                    continue
                if cell in cells:
                    return False
                else:
                    cells.add(cell)
        return True

    for row in table:
        if not validate_row(row):
            return False

    for column in range(dimension):
        if not validate_column(table, column, dimension):
            return False

    sub_range = sub_box_dimension * 2 - 1
    for row in range(0, sub_range, sub_box_dimension):
        for column in range(0, sub_range, sub_box_dimension):
            if not validate_3_by_3_sub_box(table, row, column):
                return False
    return True
