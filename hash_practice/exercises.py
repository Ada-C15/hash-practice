import heapq

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
