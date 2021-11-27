import heapq
# Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams_dict = {}
    answer = []
    for word in strings:
        word_as_list = [char for char in word]
        # print(word_as_list)
        word_as_list.sort()
        key = tuple(word_as_list)
        if anagrams_dict.get(key):
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]
    
    for key, value in anagrams_dict.items():
        answer.append(value)
    return answer

# print(grouped_anagrams(Input))   

    # returnArray = []
    # hashOfAnagrams = {}

    # if len(strings) == None:
    #     return None

    # for word in strings:
    #     hashed = "".join(sorted(word))
    #     if hashed not in hashOfAnagrams:
    #         hashOfAnagrams[hashed] = []
    #     hashOfAnagrams[hashed].append[word]

    # for i in hashOfAnagrams.values():
    #     returnArray.append(i)
    # return returnArray

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.

        Time complexity: O(N log(k)).
        Space complexity: O(N).
    """
    if nums == []:
        return []

    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        
    heap = []
    for key, value in count.items():
        heapq.heappush(heap, (-value, key))
    results = []
    
    for i in range(k):
        count, element = heapq.heappop(heap)
        results.append(element)

    return results

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n2)
        Space Complexity: O(n)
    """
    # Check rows
    for i in range(9):
        d = {}
        for j in range(9):
            if table[i][j] == '.':
                pass
            elif table[i][j] in d:
                return False
            else:
                d[table[i][j]] = True
    # Check columns
    for j in range(9):
        d = {}
        for i in range(9):
            if table[i][j] == '.':
                pass
            elif table[i][j] in d:
                return False
            else:
                d[table[i][j]] = True
    # Check sub-boxes
    for m in range(0, 9, 3):
        for n in range(0, 9, 3):
            d = {}
            for i in range(n, n + 3):
                for j in range(m, m + 3):
                    if table[i][j] == '.':
                        pass
                    elif table[i][j] in d:
                        return False
                    else:
                        d[table[i][j]] = True
    return True


