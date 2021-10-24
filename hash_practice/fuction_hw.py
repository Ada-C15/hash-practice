# # 1. Turn string to lower case
# def descending_frequency(s):
  
#   # Check that string is not empty
#   if not s:
#     return None

#   return_str = ""
#   # create 
#   freq_map = { } # { a: 1, b: 3, c 1, d:4}
#   for char in s.lower():
#     if freq_map[char]:
#       freq_map[char] += 1
#     else:
#       freq_map[char] = 1

#   max = 0
#   for freq in freq_map.items():
#     if freq > max:
#       max = freq
#       return_str += char
      
#     return return_str
# # 2. Create a character map of the string

# # 3. Find max count of characters that repeat in the string 

# # 4. Join the characters in the order of frequency and store in a new string 

# # 5. Return new string 

# def grouped_words(strings):
#     """ This method will return an array of arrays.
#         Each subarray will have strings which are words of each other
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     anagrams = []
#     str_map = {}
#     words = []
#     words.append(sorted(strings[0]))
#     for string in strings:
#         sorted_str = ''
#         sorted_arr = sorted(string)
#         sorted_str.join(sorted_arr)
#         if sorted_str in str_map:
#             words.append(string)
#         elif sorted_str not in str_map:
#             str_map[sorted_str] = 1
#     anagrams.append(words)
#     return anagrams

# initializing string 
test_string = "geekforgeeks"
  
# printing original string 
print("The original string : " + str(test_string))
  
# using join() + sorted()
# Sorting a string 
res = ''.join(sorted(test_string))
      
# print result
print("String after sorting : " + str(res))

# another shorter but equally complexity way

# def top_k_frequent_elements(nums, k):
#     """ This method will return the k most common elements
#         In the case of a tie it will select the first occuring element.
#         Time Complexity: ?
#         Space Complexity: ?
#     """
#     num_dict = {} 
#     for num in nums:
#         if num not in num_dict:
#             num_dict[num] = 1
#         elif num in num_dict:
#             num_dict[num] += 1

#     max_nums = []

#     for i in range(k):
#         most_common = max(num_dict, key=num_dict.get)
#         max_nums.append(most_common)
#         del num_dict[most_common]
    
#     return max_nums
