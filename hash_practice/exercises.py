
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagram_dict = {}

    for word in strings:
        # Hash Formula maps anagrams into same bucket
        # by alphabetically sorting the word
        # Alpha sort ensures words with same length and same freq
        # of characters get mapped into same bucket
        word_key = "".join(sorted(word))
        if (word_key in anagram_dict):
            anagram_dict[word_key].append(word)
        else:
            anagram_dict[word_key] = [word]

    output = []
    for word_key in anagram_dict:
        output.append(anagram_dict[word_key])

    return output

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    num_dict = {}
    result = []
    freq_dict = {}
    num_freqs = []

    #populate the first dictionary
    for i in nums:
        #map key to value
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1

    #populate another dictionary with frequency as key and values with 
    #nums with that frequency
    for key, value in num_dict.items():
        if (value not in freq_dict):
            freq_dict[value] = [key]
        else:
            freq_dict[value].append(key)

        # num_freqs is a list of unique frequencies
        if (value not in num_freqs):
            num_freqs.append(value)
        
    num_freqs.sort(reverse=True)

    for freq in num_freqs:
        #list of numbers for this frequency
        nums_for_freq = freq_dict[freq]
        for num in nums_for_freq:
            if(len(result) < k):
                result.append(num)
            else:
                break
        
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
    
    row_counts = []
    col_counts = []
    subgrid_counts = [] # hash of hash where each sub hash represents a 3x3 grid
    
    row_index = 0
    
    for row in table:
        col_index = 0
        #initialize the hashtable for a specific row
        row_counts.append({})
        
        for element in row:
            
            # initialize the hashtable for a specific col if it doesnt exist
            if (len(col_counts) <= col_index):
                col_counts.append({})
            
            if (element != "."):
                if(not update_and_validate_hash(element, row_counts[row_index])):
                    return False
                
                if(not update_and_validate_hash(element, col_counts[col_index])):
                    return False    
            
            col_index += 1        
        
        row_index += 1
        
    return True           

# helper function to add element to hashtable for a specific row or col and validate counts    
def update_and_validate_hash(element, hashtable):
    if(element not in hashtable):
        hashtable[element] = 1
    else:
        hashtable[element] += 1
    
    return (hashtable[element] <= 1)


# table = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# output = valid_sudoku(table)
# print(f"output={output}")

# numbers = [1, 2, 3]
# k = 3
# output = top_k_frequent_elements(numbers, k)
# print(output)

#input = [] #["eat", "tea", "tan", "ate", "nat", "bat"]
#output = grouped_anagrams(input)
#print(output)
