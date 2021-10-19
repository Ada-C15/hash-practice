
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
    


# def top_k_frequent_elements(nums, k):
#     """ This method will return the k most common elements
#         In the case of a tie it will select the first occuring element.
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     num_dict = {} #num_dict = {1:3, 2:2, 3: 3, 4:4, 7:1, 5:4, 6:4}
#     # k = 2
#     #  [4, 4]
#     for num in nums:
#         if num not in num_dict:
#             num_dict[num] = 1
#         elif num in num_dict:
#             num_dict[num] += 1
#     # reverse dictionary so I have max as key and number as value
#     reversed_dictionary = {value : key for (key, value) in num_dict.items()}
#     print(' ------ num_dict -----')
#     print(reversed_dictionary)

#     max_nums = []
#     max = 0
#     key = 0
#     value = 0
#     for i in range(k):
#         for key, value in num_dict.items():
#             if key > max: # 0>1
#                 max = key # max 
#             else:
#                 max = max
#         max_nums.append(max)
#         # max_nums.append(num_dict[key])
#         # print('--- max_nums ---')
#         # print(max_nums)
# # ---------------
#         # print(f'--- deleting {num_dict[key]} ---')
#         # del num_dict[key]
#         # print('---  now num_dict is ---')
#         # print(num_dict)

    
#     # print(max_nums)
#     return max_nums

#     # Works?? 
#     # for i in range(k):
#     #     top = max(freq_map, key=freq_map.get)
#     #     top_k.append(top)
#     #     del freq_map[top]

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    num_dict = {} #num_dict = {1:3, 2:2, 3: 3, 4:4, 7:1, 5:4, 6:4}
    # k = 2
    #  [4, 4]
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        elif num in num_dict:
            num_dict[num] += 1

    max_nums = []
    max = 0
    
    for i in range(k):
        most_common = max(num_dict, key=num_dict.get)
        max_nums.append(most_common)
        del num_dict[most_common]
    
    return max_nums

# for i in range(k):
#     #     top = max(freq_map, key=freq_map.get)
#     #     top_k.append(top)
#     #     del freq_map[top]

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

