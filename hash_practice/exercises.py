
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    result = []
    dict = {}
    for string in strings:
        l = list(string)
        match_found = False
        for k in dict.keys():
            if len(k) == len(l):
                if len(set(k).difference(set(l))) == 0: # k = abc, l = bc, k - l = a if difference is a 0 they should be a match
                    dict[k].append(string)
                    match_found = True
        if not match_found:
            dict[string] = [string]
    for l in dict.values():
        result.append(l)
    return result

grouped_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(nums) == 0:
        return []
    frequency = {}
    for num in nums:
        if num in frequency.keys():
            frequency[num] += 1
        else:
            frequency[num] = 1
 
    result = []
    for i in range(k):
        max_k = 0
        max_v = 0     #list(frequency.items())[0]
        for key,v in frequency.items():
            if v > max_v:
                max_k = key
                max_v = v
        result.append(max_k)
        del frequency[max_k]
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

