
def grouped_anagrams(words):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ? Sorting (O log n) * n log n
        Space Complexity: O(n)
    """
    anagrams = []
    str_map = {}
    for word in words:
        # sorted_word = word # initial string
        # sorted_arr = sorted(word)
        # sorted_word.join(sorted_arr)

        sorted_word = ''.join(sorted(word))
        print("------- sorted_word----------- ")
        print(sorted_word)
        if sorted_word not in str_map:
            str_map[sorted_word] = [word]
        elif sorted_word in str_map:
            str_map[sorted_word].append(word)
    print(str_map)
    for key, value in str_map.items():
        anagrams.append(value)
    return anagrams
 
def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(kn)
        Space Complexity: O(k)
    """
    if not nums:
        return []
        
    num_dict = {} 
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        elif num in num_dict:
            num_dict[num] += 1

    max_nums = []
    for i in range(k):
        max_num = 0
        max_freq = 0
        for num, frequency in num_dict.items():
            if frequency > max_freq: 
                max_freq = frequency  
                max_num = num
        max_nums.append(max_num)
        del num_dict[max_num]

    return max_nums

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

