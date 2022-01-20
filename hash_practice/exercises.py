from hash_practice.linkedlist import LinkedList

# sums might be bb ac might add to same number. 
def hash_helper(word):
    hash = 0
    for letter in word:
        unicode_char = ord(letter)
        hash += unicode_char
    return hash

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: 2logn
        Space Complexity: 0(n)
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
    grouped_anagrams = []
    #keys are numbers and values are linked lists 
    for key, value in anagrams.items():
        grouped_anagrams.append(value.to_list())
    return grouped_anagrams

    # split each word 
    # get ascii for each letter
    # add letters/ascii values together for each word
    # make that the key and add word to anagram/value list 
    # return anagram list for each key  

    

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(nlogn)
        Space Complexity: O(logn)

    """
  
    frequent_elements = {}
    if nums == []:
        return []

    for num in nums:
        if num in frequent_elements:
            frequent_elements[num] += 1
        else:
            frequent_elements[num] = 1
    # Python program to demonstrate
    # slice() operator
 
    # List slicing
    # L = [1, 2, 3, 4, 5]
    # s1 = slice(3)
    # s2 = slice(1, 5, 2)
    # print("List slicing")
    # print(L[s1])
    # print(L[s2])

    my_sorted_list = sorted(frequent_elements.values(),reverse=True)
    s1 = slice(k)
    numbers = my_sorted_list[s1]
    # n log n quicksort
    k_list = []
    # for loop 0(n)
    for key,value in frequent_elements.items():
        if value in numbers:
            k_list.append(key)
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

