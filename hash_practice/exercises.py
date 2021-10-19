
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: On^4 (?)
        Space Complexity: On
    """
    groupings = []

    j = 0
    while j < len(strings):

        letter_map = {}
        sub_group = [strings[j]]

        for letter in strings[j]:
            if letter not in letter_map:
                letter_map[letter] = 1
            else:
                letter_map[letter] += 1

        k = j + 1
        while k < len(strings):

            comparison_letter_map = {}

            for letter in strings[k]:
                if letter not in comparison_letter_map:
                    comparison_letter_map[letter] = 1
                else:
                    comparison_letter_map[letter] += 1

            if comparison_letter_map == letter_map:
                sub_group.append(strings[k])
                strings.remove(strings[k])
                k = k
            else:
                k += 1
        
        groupings.append(sub_group)

        j += 1

    return groupings


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: On^2
        Space Complexity: On
    """
    most_frequent_elements = []

    if not nums:
        return most_frequent_elements

    num_frequency_map = {}

    for num in nums:
        if num not in num_frequency_map:
            num_frequency_map[num] = 1
        else:
            num_frequency_map[num] += 1

    frequencies_list = []

    for freq_value in num_frequency_map.values():
        frequencies_list.append(freq_value)

    frequencies_list.sort()

    for i in range(k):

        search_specific_freq = frequencies_list[-(i+1)] 

        for num in num_frequency_map:
            if num_frequency_map[num] == search_specific_freq:
                most_frequent_elements.append(num)
            
            if len(most_frequent_elements) == k:
                return most_frequent_elements


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

