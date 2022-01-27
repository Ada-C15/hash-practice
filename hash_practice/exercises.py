
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    anagrams = {}
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    temp_dict = {}
    return_list = []

    if not nums:
        return return_list

    for i in range(0, len(nums)):
        if nums[i] in temp_dict:
            temp_dict[nums[i]] += 1
        else:
            temp_dict[nums[i]] = 1

    sorted_dict = sorted(temp_dict.items(), key=lambda tuple: tuple[1], reverse=True)

    for j in range(0, k):
        return_list.append(sorted_dict[j][0])

    return return_list


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1)
        Space Complexity: O(1)
        Will provide solution with the above time/space complexity. 
    """
    pass 