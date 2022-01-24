
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: 0(n)
        Space Complexity: O(n)
    """
    if not strings:
        return []

    map={}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in map:
            map[sorted_string].append(string)
        else:
            map[sorted_string]=[string]

    result=[]
    for value in map.values():
        result.append(value)
    return result


def top_k_frequent_elements(nums,k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    if not nums:
        return []

    map = {}
    for num in nums:
        count = map.get(num,0)
        map[num]= count +1
    
    result= []
    for i in range(k):
        k = max(map, key=map.get)
        result.append(k)
        del map[k]

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

