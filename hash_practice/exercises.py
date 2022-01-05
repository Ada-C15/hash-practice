
import collections
from typing import Collection


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    collection = {}
        
    for word in strings:
        
        sorted_word = "".join(sorted(word))
        if sorted_word not in collection:
            collection[sorted_word] = [word]
        else:
            collection[sorted_word].append(word)
    
    return list(collection.values())  

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    collection = {}
    for num in nums:
        if num not in collection:
            collection[num] = 1
        else:
            collection[num] += 1

    frequency_list ={}
    for key,value in collection.items():
        if value not in frequency_list:
            frequency_list[value] = [key]
        else:
            frequency_list[value].append(key)

    result = []
    for i in range(len(nums),0,-1):
        if i in frequency_list:
            result.extend(frequency_list[i])
        if len(result) >=k:
            break
    return result


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    board = {}
    for i in range(1,10):
        board[str(i)] = [set(), set(), set()]
    for r, row in enumerate(table):
        for c, col in enumerate(row):
            if col != ".":
                block = (r // 3)*3 + c //3
                if r in board[col][0] or c in board[col][1] or block in board[col][2]:
                    return False
                board[col][0].add(r)
                board[col][1].add(c)
                board[col][2].add(block)
    return True

    # cols = collections.defaultdict(set)
    # rows = collections.defaultdict(set)
    # squares = collections.defaultdict(set)

    # for r in range(9):
    #     for c in range(9):
    #         if table[r][c]=='.':
    #             continue
    #         if (table[r][c] in rows[r] or 
    #             table[r][c] in cols[c] or
    #             table[r][c] in squares[(r//3,c//3)]):
    #             return False
    #         cols[c].add(table[r][c])
    #         rows[r].add(table[r][c])
    #         squares[(r//3,c//3)].add(table[r][c])
    # return True


    

