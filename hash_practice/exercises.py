
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(k logn)
        Space Complexity: ?
    # """

    

    word_hash = {}
    return_group = []
    # O(k logk) <-- greatest impact and happens with each iteration O(n klogk)
    for word in strings: # for loop O(n)<p-- not inside loop 
        # body of entire for loop time complexity is  O(k)+ O(k logk) + O(1)+ O(1) + O(1)+ O(1)    
        letter_list = list(word) #O(k)<-- what it takes to create a new list for one word
        letter_list.sort() # sort method O(k logk)
        str_key = ''.join([str(letter) for letter in letter_list]) # nested for loop O(k)
        if str_key not in word_hash: #O(1)
            word_hash[str_key]= list() #O(1)
            word_hash[str_key].append(word) #O(1)
        else:
            word_hash[str_key].append(word)#O(1)
    for key, values in word_hash.items():#O(n)
        return_group.append(values)
    return return_group




def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """

    """
    input -> [1,4,3,1,1,3], 2
    output -> [1,3]
    input-> [2,2,2,2,3,1], 2
    output -> [2,3]
    
   
    2. mapping number to count
    
    """
    hash = {}
    if not nums:
        return nums
    
    for num in nums:# loops through array O(n)
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] += 1
      
    hash_values_list=list(hash.values()) # creating a new list with hash values
    
    hash_values_list.sort(reverse=True) # sorting the list O(k logk)
    kth_frequency = []
    
    # time complexity for entire for loop body: O(n)+ O(n) =  O(n^2) 
    for i in range(k): # O(n)
        for key, values in hash.items(): #O(n)
            if values == hash_values_list[i] and key not in kth_frequency:
                kth_frequency.append(key) #O(n)
    return kth_frequency
    

        
   
 







def valid_sudoku(table):
    """"
        This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    Input:
    [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being 
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

    """