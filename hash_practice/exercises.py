import heapq
import re

class MaxHeapObj(object):
    def __init__(self, num_and_count):
        self.num = num_and_count['num']
        self.count = num_and_count['count']

    def __lt__(self, other):
        return self.count > other.count
    def __eq__(self, other):
        return self.count == other.count

    def __str__(self):
        return f"{self.num}: {self.count}"

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    
    anagrams_dict = {}

    for word in strings:
        word_as_list = [char for char in word]
        word_as_list.sort()
        key = tuple(word_as_list)
        if anagrams_dict.get(key):
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]
    
    answer = []

    for key, value in anagrams_dict.items():
        answer.append(value)
    return answer


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    number_count = {}
    for num in nums:
        if number_count.get(num):
            number_count[num] += 1
        else:
            number_count[num] = 1

    maxHeap = []
    for num, count in number_count.items():
        heapq.heappush(maxHeap, (count, num))
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    
    topK = []
    while maxHeap:
        topK.append(heapq.heappop(maxHeap)[1])

    return topK

def get_valid_digit_count():
    return {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 1,
        9: 1,
    }

def is_digit(string):
    regex = '^[0-9]$'
    if re.search(regex, string):
        return True
    return False

def check_subgrid(table, subgrid):
    digit_count = get_valid_digit_count()

    for current_row in range(subgrid[0], subgrid[0] + 3):
        for current_col in range(subgrid[1], subgrid[1] + 3):
            if is_digit(table[current_row][current_col]):
                digit_count[ int(table[current_row][current_col])] -= 1
            
                if digit_count[ int(table[current_row][current_col]) ] < 0:
                    return False
    return True

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    for i in range(0, len(table)):
        row_count = get_valid_digit_count()
        col_count = get_valid_digit_count()
        for j in range(0, len(table)):
            # check the current row
            if is_digit(table[i][j]):
                row_count[ int(table[i][j])] -= 1
                if row_count[int(table[i][j])] < 0:
                    return False
            # get the current col
            if is_digit(table[j][i]):
                col_count[ int(table[j][i])] -= 1
                if col_count[ int(table[j][i])] < 0:
                    return False

    subgrids = [[0, 0], [0, 3], [0, 6],
                [3, 0], [3, 3], [3, 6],
                [6, 0], [6, 3], [6, 6]]

    for subgrid in subgrids:
        if not check_subgrid(table, subgrid):
            return False
    
    return True

