
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    hash = {}
    
    for string in strings: 
        sorted_word = "".join(sorted(string))
        if sorted_word in hash:
            hash[sorted_word].append(string)
        else:    
            hash[sorted_word] = [string]
    
    return list(hash.values())


def get_tuple_key(item):
    return item[1]

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n) 
    """
    my_hash = {}
    
    if len(nums) == 0: 
        return []
    
    for num in nums:
        if num in my_hash:
            my_hash[num] = my_hash.get(num, 1) + 1
        else:
            my_hash[num] = 1
    answer = []
    temp = sorted(my_hash.items(), key=get_tuple_key, reverse=True)# helper function above
    for key, value in temp:
        answer.append(key)
    return answer[0:k]
    
        
        

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

