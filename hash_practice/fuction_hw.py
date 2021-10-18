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