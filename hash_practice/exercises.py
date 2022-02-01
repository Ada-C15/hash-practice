#below returns an array of arrays.Each subarray 
# contains strings which are anagrams of each other
# Time/Space Complexity: O(n)

def grouped_anagrams(strings):
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

############top_k_freq helper##################
#there is no easy way to look up a key that responds to a specific value, 
# so maybe instead I should switch all of the values and keys for faster look up?

def get_keys(dict, val):
      keys = set()
      for key, value in dict.items():
         if val == value:
           keys.add(key)
      if keys:
        return keys
      return
    
################################################
# This method will return the k most common elements (numbers only)
# In the case of a tie, select the first occuring element. (a twist.)
# *Time/Space Complexity: O(n)
# *probably not jw

def top_k_frequent_elements(nums, k):
    top_k = []
    num_count = {}
    for num in nums:
        if num_count.get(num):
            num_count[num] += 1
        else:
            num_count[num] = 1

    #chris wants a rewrite of below (who can blame him)  
    #try reimagining how I can get rid of helper function 
    #to instead leverage hash more rather than loop through 
    for i in range(len(num_count.values()), 0, -1):
        flat_k = [ele for keys in top_k for ele in keys]
        if get_keys(num_count, i):
          top_k.append(get_keys(num_count, i))
        if len(flat_k) >= k:
          return flat_k
       
    return [ele for keys in top_k for ele in keys]

############sudoku helpers######################
import re 

def is_num(string):
    nums = '^[0-9]$'
    if re.search(nums, string):
        return True
    return False

def valid(line):                                ##########################behold:
    num_only = [i for i in line if is_num(i)]   ################################ the single
    if len(num_only) == len(line):              ################################ but useful 
        return len(set(num_only)) == 9 and sum(num_only) == 45 == sum(set(line))#appearance
                                                ################################ of hash sets()
    return len(set(line)) == len(num_only) + 1  ################################ in this solution
    
#################################################
### *Time/Space Complexity: O(n)
### *bc input will always be the same size tho...
###  do we need to consider it for these? 

def valid_sudoku(table):
    subgrids = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [char for chars in [row[j:j + 3] for row in table[i:i + 3]] for char in chars]
            subgrids.append(subgrid)

    nope_subgrids = [grid for grid in subgrids if not valid(grid)]
    nope_columns_rows = [line for line in table if not valid(line)]

    return not (nope_columns_rows or nope_subgrids)
