
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if (sorted_word in anagram_dict):
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    anagrams_array = []
    for words in anagram_dict.values():
        anagrams_array.append(words)
    return anagrams_array

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    
    final_result = []
    if not nums:
        return final_result

    most_freq_nums = {}
    for i in range(0, len(nums)):
        if nums[i] in most_freq_nums:
            most_freq_nums[nums[i]] += 1
        else:
            most_freq_nums[nums[i]] = 1

    sorted_nums = sorted(most_freq_nums.items(), 
        key=lambda tuple: tuple[1], reverse=True)
    
    for j in range(0, k):
        final_result.append(sorted_nums[j][0])
    return final_result


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

