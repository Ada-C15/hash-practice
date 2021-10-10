
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # return_array = []
    # for word in strings:
    #     word_dict = {}
    #     for letter in word:
    #         if not letter:
                
        

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    return_arr = []
    nums_dict = {}
    if len(nums) == 0:
        return []
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else: 
            nums_dict[num] += 1
    for i in range (0,k):
        highest = max(nums_dict, key=nums_dict.get)
        return_arr.append(highest)
        nums_dict.pop(highest)

    return return_arr

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

nums= [1,3,3,4,4]
top_k_frequent_elements(nums, 2)

