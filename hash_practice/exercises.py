#This is a solution that I worked out with a study group hosted by a TA and Al. It was working 
#until I made some changes and now I cant seem to figure out what I did or how it was
#really working in the first place. I will continue to work on it but I didnt feel it was worthy 
#turning in fully. 

# def anagram_helper(word1, word2):
    
#     char_map1 = {}
#     char_map2 = {}

#     for char in word1:
#         if char not in char_map1:
#             char_map1[char] = 1
#         else:
#             char_map1[char] += 1
    
#     for chr in word2:
#         if char not in char_map2:
#             char_map2[char] = 1
#         else:
#             char_map2[char] += 1

#     if char_map1 == char_map2:
#         return True
#     else:
#         return False

# def grouped_anagrams(strings):
#     """ This method will return an array of arrays.
#         Each subarray will have strings which are anagrams of each other
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     temp = []
#     grouped_anagrams = []
#     hash_set = {}

#     for i, word1 in enumerate(strings):
#         if word1 in hash_set:
#             continue
#         temp.append(word1)
#         hash_set[word1] = 1

#         for j, word2 in enumerate(strings):
#             if anagram_helper(word1, word2):
#                 if word2 not in hash_set:
#                     temp.append(word2)
#                     hash_set[word2] = 1
        
#         grouped_anagrams.append(temp)
#         temp = []

#     return grouped_anagrams

def anagram_helper(word1, word2):
    
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


def grouped_anagrams(strings):
    hash_set = {}
    temp_array_strings = []
    anagrams = []
    
    for i, word1 in enumerate(strings):
        if word1 in hash_set:
            continue
        temp_array_strings.append(word1)
        hash_set[word1] = 1

        for j, word2 in enumerate(strings):
            if anagram_helper(word1, word2):
                if word2 not in hash_set:
                    temp_array_strings.append(word2)
                    hash_set[word2] = 1

        anagrams.append(temp_array_strings)
        print(anagrams)
        temp_array_strings = []

    return anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """

    freq_map = {}
    k_freq_elements = []

    if nums:

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        for i in range(0,k):
            key_with_max_val = max(freq_map, key=freq_map.get)
            k_freq_elements.append(key_with_max_val)
            del freq_map[key_with_max_val]
    
    return k_freq_elements


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

