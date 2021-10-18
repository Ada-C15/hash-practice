
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(m n log n)
        Space Complexity: O(n)
    """
    return_arr = []
    str_map = {}

    for string in strings:
        sorted_str = "".join(sorted(string))

        if sorted_str not in str_map:
            str_map[sorted_str] = [string]
        elif sorted_str in str_map:
            str_map[sorted_str].append(string)

    for value in str_map.values():
        return_arr.append(value)
        
    return return_arr
    

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(m n)
        Space Complexity: O(n)
    """
    freq_map = {}

    if not nums:
        return []

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    top_k = []
    for i in range(k):
        top = max(freq_map, key=freq_map.get)
        top_k.append(top)
        del freq_map[top]

    return top_k


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n m)
        Space Complexity: O(n)
    """
    seen = set()

    # i = rows
    # j = columns
    for i in range(9):
        for j in range(9):
            current_val = table[i][j]
            if current_val != ".":
                if current_val + " in row " + str(i) in seen or \
                    current_val + " in col " + str(j) in seen or \
                    current_val + " in box " + str(i/3) + "-" + str(j/3) in seen:
                    return False
                else:
                    seen.add(current_val + " in col " + str(j)) 
                    seen.add(current_val + " in row " + str(i))    
                    seen.add(current_val + " in box " + str(i/3) + "-" + str(j/3))  
    return True