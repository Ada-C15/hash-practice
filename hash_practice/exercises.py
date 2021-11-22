
def grouped_anagrams(strings):
    """
    1. Map each ordered string as a key, appending subsequent matching ordered strings as lists
    2. Return the list values in an array 
    """
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n) 
        Space Complexity: O(n) in worst case (no anagrams)
    """

    if strings == []:
        return []

    anagrams_dict = {}
    for word in strings:                            # O(n)
        temp = "".join(sorted(word))                # * (O(m) + O(m log(m))) = O(n * m * log(m))
        if not anagrams_dict.get(temp): 
            anagrams_dict[temp] = [word] 
        else:
            anagrams_dict[temp].append(word)
    
    return list(anagrams_dict.values())             # O(n) for worst case -> 2n

def top_k_frequent_elements(nums, k):
    """
    1. Count occurrences for each num, map them in dict
    2. Sort nums/values by value, in descending order
    3. Return first k nums from sorted tuple list
    """
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n)
        Space Complexity: O(n) for worst case (each element once)
    """
    if nums == []:
        return []

    nums_values = {}
    for num in nums:                                # O(n)
        if nums_values.get(num):
            nums_values[num] += 1
        else:
            nums_values[num] = 1
    
    sorted_by_value = sorted(nums_values.items(), key = lambda x: x[1], reverse=True)
                                                    # sorted() is Timsort -> O(n log n)

    result = []
    for i in range(k):                              # O(k) -> close to constant
        result.append(sorted_by_value[i][0])
    return result

def valid_sudoku(table):
    """
    1. Check each row for duplicates
    2. Check each column for duplicates
    3. Check each sub grid for duplicates
    """
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(1)
        Space Complexity: O(1)
    """
    rows = [[] for x in range(9)]
    columns = [[] for x in range(9)]
    sub_grids = [[[] for x in range(3)] for x in range(3)]

    for row in range(0, 9):                         # O(n)
        for col in range(0, 9):                     # * O(n) -> O(n^2) = 81, which is the given n, which is a constant
            if table[row][col] == ".":
                continue
            elif table[row][col] in rows[row]:
                return False
            elif table[row][col] in columns[col]:
                return False
            elif table[row][col] in sub_grids[row // 3][col // 3]:
                return False
            else:
                rows[row].append(table[row][col])
                columns[col].append(table[row][col])
                sub_grids[row // 3][col // 3].append(table[row][col])

    return True