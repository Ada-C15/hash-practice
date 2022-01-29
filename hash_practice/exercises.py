import re

def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    anagrams = dict()
    groups = []
    for word in strings:
        word_sort = ''.join(sorted(word))
        key = tuple(word_sort)
        if anagrams.get(key):
            anagrams[key].append(word)
        else:
            anagrams[key] = [word] 
    for value in anagrams.values():
        groups.append(value)
    return groups

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements (numbers only)
        In the case of a tie it will select the first occuring element. (ooh, a twist.)
        (will the numbers always be sequential?) 
        Time Complexity: O(n)*
        Space Complexity: O(n)* 
        *maybe not jw
    """
    num_count = {}
    for num in nums:
        if num_count.get(num):
            num_count[num] += 1
        else:
            num_count[num] = 1

    def get_keys(val):
      keys = set()
      for key, value in num_count.items():
         if val == value:
           keys.add(key)
      if keys:
        return keys
      return
             
    top_k = []
    for i in range(len(num_count.values()), 0, -1):
      flat_k = [ele for keys in top_k for ele in keys]
      if len(flat_k) >= k:
          return flat_k
      if get_keys(i) is not None:
          top_k.append(get_keys(i))
    return list(ele for keys in top_k for ele in keys)

############sudoku helpers#######################

def num(string):
    regex = '^[0-9]$'
    if re.search(regex, string):
        return True
    return False

def valid(line):
    for i in range(len(line)):
        if num(line[i]) == True:
            continue
        else:
            no_only = [i for i in line if num(i)]
            return len(set(no_only)) == len(no_only) #okay but this is the only place I'm using a hash tho... may need redo
    return len(line) == 9 and sum(line) == sum(set(line))       

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        (if solvable and unfinished, give it to grammie sammie to solve, 
        and check solution if you want) 
        Time Complexity: O(n)*
        Space Complexity: O(n)*
            *It will always be the same size tho...
    """
    nope_r = [row for row in table if not valid(row)]
    nope_c = [col for col in table if not valid(col)]
    subgrids = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [item for items in [row[j:j + 3] for row in table[i:i + 3]] for item in items]
            subgrids.append(subgrid)
    nope_subgrids = [grid for grid in subgrids if not valid(grid)]

    return not (nope_r or nope_c or nope_subgrids)
