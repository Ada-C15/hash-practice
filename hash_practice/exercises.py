from hash_practice.linkedlist import LinkedList


# sums might be bb ac might add to same number. Consider prime hash in future #imlementation
# split each word 
# get ascii for each letter
# add letters/ascii values together for each word
# make that the key and add word to anagram/value list 
# return anagram list for each key  

def hash_helper(word): 
    """ This method will takes a set of inputs of any arbitrary size and fits it into a table or other data structure that contains fixed-size elements.   
        Time Complexity: O(n) checking each word
        Space Complexity: O(1) rewriting to unicode_char
    """ 
    hash = 0
    for letter in word:
        unicode_char = ord(letter)
        hash += unicode_char
    return hash

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
    
        Time Complexity: O(n) checking each word
        Space Complexity: O(n) at worse case might have to create a node
    """ 

    
    anagrams = {}
    if strings == []:
        return []
    for word in strings:
        hash = hash_helper(word)
        # If it is not in anagrms make a new linked list
        if hash not in anagrams:
            anagrams[hash] = LinkedList()
        # regardless add to linked list
        anagrams[hash].add_node(word)


    return create_anagram_list(anagrams)

def create_anagram_list(anagrams):
    """ This method the values into linked lists
        and returns the anagrams
    
        Time Complexity: O(n) checking each word
        Space Complexity: O(n) adds each word
    """ 
    grouped_anagrams = []
    #keys are numbers and values are linked lists 
    for key, value in anagrams.items():
        grouped_anagrams.append(value.to_list())
    return grouped_anagrams


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlogn)
        Space Complexity: O(logn)

        numbers = [1, 2, 2, 2, 3, 3, 3]
        k = 2
        answer.sort()
        assert answer == [2, 3]

        Time: O(n)
        Space: O(n) 
    """
  
    frequent_elements = {}
    if nums == []:
        return []

    for num in nums:
        if num in frequent_elements:
            frequent_elements[num] += 1
        else:
            frequent_elements[num] = 1
  

    # Time and Space O(n) might need to append all the values
    my_sorted_list = sorted(frequent_elements.values(),reverse=True)
    s1 = slice(k)
    numbers = my_sorted_list[s1]
    # n log n quicksort
    k_list = []
    # for loop 0(n)
    for key,value in frequent_elements.items():
        if value in numbers:
            k_list.append(key)
            #after you matchremove from numbers so it doesn't match twice
            numbers.remove(value)
    return k_list
    

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

