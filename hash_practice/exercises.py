
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(nlogn)
        Space Complexity: n
    """
    map = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in map:
            map[sorted_word] = [word]
        else:
            map[sorted_word].append(word)
    output = []
    for value in map.values():
        output.append(value)
    return output


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlogn)
        Space Complexity: n
    """ 
    if len(nums) == 0:
            return []

    map = {} 
    for number in nums: 
        if number not in map: 
            map[number] = 1 
        else: 
            map[number] += 1 
    
    sorted_map = dict(sorted(map.items(), key=lambda x : x[1], reverse=True))

    output = [] 
    for key in sorted_map: 
        if k > 0: 
            output.append(key)
            k -= 1 

    return output

    
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

