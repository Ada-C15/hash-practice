
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other.
        Time Complexity: O(n^2) -- or is it O(n) bc of the "continue"s?
        Space Complexity: O(n)
    """
    result = []

    for i in range(len(strings)):
        if strings[i] == None:
            continue

        anagrams = [strings[i]]
        strings[i] = None

        for j in range(len(strings)):
            if strings[j] == None:
                continue

            if __is_anagram(anagrams[0], strings[j]):
                anagrams.append(strings[j])
                strings[j] = None

        result.append(anagrams)

    return result

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n x m), where n is length of original list and m is number of repeats for each repeated value
        Space Complexity: O(n)
    """
    top_k = []

    freqs = __create_indexed_freq_map(nums)
    reverse_freqs = __create_reverse_indexed_freq_map(freqs)

    print(reverse_freqs)

    sorted_freqs = sorted(reverse_freqs.keys(), reverse=True)
    
    for freq in sorted_freqs:
        if k - len(top_k) >= len(reverse_freqs[freq]):
            for index_num in reverse_freqs[freq]:
                top_k.append(index_num[1])
        else:
            sorted_index_nums = sorted(reverse_freqs[freq])
            for index_num in sorted_index_nums:
                top_k.append(index_num[1])
                if len(top_k) == k:
                    return top_k
        
        if len(top_k) == k:
            return top_k

    return top_k


def valid_sudoku(board):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n) ? its a little complicated and im tired
    """
    
    sudoku_map = {}
    quadrants = [[], [], [], [], [], [], [], [], []]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ".":
                if board[i][j] in sudoku_map:
                    if i in sudoku_map[board[i][j]][0]:
                        return False
                    if j in sudoku_map[board[i][j]][1]:
                        return False
                    sudoku_map[board[i][j]][0].add(i)
                    sudoku_map[board[i][j]][1].add(j)
                else:
                    m = [{i}, {j}]
                    sudoku_map[board[i][j]] = m

                x = int(j)
                y = int(i)

                if y < 3 and x < 3:
                    quadrants[0].append(board[i][j])
                elif y < 3 and 3 <= x and x < 6:
                    quadrants[1].append(board[i][j])
                elif y < 3 and 6 <= x:
                    quadrants[2].append(board[i][j])
                elif 3 <= y and y < 6 and x < 3:
                    quadrants[3].append(board[i][j])
                elif 3 <= y and y < 6 and 3 <= x and x < 6:
                    quadrants[4].append(board[i][j])
                elif 3 <= y and y < 6 and x >= 6:
                    quadrants[5].append(board[i][j])
                elif 6 <= y and x < 3:
                    quadrants[6].append(board[i][j])
                elif 6 <= y and 3 <= x and x < 6:
                    quadrants[7].append(board[i][j])
                elif 6 <= y and x >= 6:
                    quadrants[8].append(board[i][j])

    for quadrant in quadrants:
        if len(set(quadrant)) != len(quadrant):
            return False
            
    return True




def __is_anagram(str1, str2):
    return __create_freq_map(str1) == __create_freq_map(str2)

def __create_freq_map(iterable):
    freq = {}
    for el in iterable:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1
    return freq

def __copy_list(list):
    copy = []
    for el in list:
        copy.append(el)
    return copy

def __create_indexed_freq_map(iterable):
    '''
    Creates a frequency map, but with a twist. It also stores the index of the key,
    where it first appears in the original iterable. The value for each key in the resulting 
    map will be a list. the zeroeth index of this list will represent the frequency. The 
    next value in this list will be the first index of the key.
    '''
    freq = {}
    for i in range(len(iterable)):
        if iterable[i] in freq:
            freq[iterable[i]][0] += 1
        else:
            freq[iterable[i]] = [1, i]
    return freq

def __create_reverse_indexed_freq_map(freq_map):
    '''
    Creates a reverse frequency map. The keys represent frequencies, and the value for each key
    is a list of tuples. Each of these tuples contians the original index of the number, and 
    the number itself.
    '''
    reverse_map = {}
    for key, value in freq_map.items():
        if value[0] in reverse_map:
            reverse_map[value[0]].append((value[1], key))
        else:
            reverse_map[value[0]] = [(value[1], key)]
    return reverse_map
