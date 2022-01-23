
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams = {}

    for string in strings:
        sortedString = "".join(sorted(string))
        if sortedString in anagrams:
            anagrams[sortedString].append(string)
        else:
            anagrams[sortedString] = [string]


    return list(anagrams.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: o(n)
    """
    numMap = {}
    res = []

    if nums == []:
        return nums

    for num in nums:
        numMap[num] = numMap.get(num, 0) +1

    for i in range(k):
        maxValue = max(numMap, key=numMap.get)
        res.append(maxValue)
        numMap.pop(maxValue)
                
    return res


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

