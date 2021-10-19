
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams_table = {}

    # iterate over each word: sort it, then check if it's in anagrams table.
    # if not, add it
    # -> creates a table wherein each key is the sorted anagram and its value is an array of anagram strings 
    for word in strings:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams_table:
            anagrams_table[sorted_word].append(word)
        else:
            anagrams_table[sorted_word] = [word]

    # the anagrams table already has the anagrams grouped - just need to
    # get each array and add to a list
    # I am lazy and using this here built-in method
    return list(anagrams_table.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    num_freq_table = {}
    freq_list = {}

    for num in nums:
        if num in num_freq_table:
            num_freq_table[num] += 1
        else:
            num_freq_table[num] = 1

    for key,value in num_freq_table.items():
        if value not in freq_list:
            freq_list[value] = [key]
        else:
            freq_list[value].append(key)

    k_elements = []

    for i in range(len(nums), 0, -1):
        if i in freq_list:
            k_elements.extend(freq_list[i])
        if len(k_elements) >= k:
            break

    return k_elements

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    # checking rows
    for row in table:
        check={}
        for num in row:
            if num==".":
                continue
            if check.get(num):
                return False
            else:
                check[num]=1
        
    # checking columns
    for column in range(9):
        check={}
        for row in range(9):
            num = table[row][column]
            if num == ".":
                continue
            elif check.get(num):
                return False
            else:
                check[num]=1
                   
    # checking squres
    for i in range(0,7,3):
        for j in range(0,7,3): # finding start point of each squares
            check={}
            for row in range(i,i+3):  # traversing through the square
                for col in range(j,j+3):
                    num = table[row][col]
                    if num == ".":
                        continue
                    if check.get(num):
                        return False
                    else:
                        check[num] = 1
        return True     

