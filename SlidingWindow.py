import math
import numpy as np

def max_sub_array_size_k(k, arr):
    
    '''
    Given an array of positive numbers and a positive number k
    find the maximum sum of any contiguous subarray of size k.
    '''
    
    max_sum, window_sum = 0, 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

def smallest_subarray_sum(s, arr):
    '''
    Given an array of positive numbers and a positive number S 
    find the length of the smallest contiguous subarray whose sum is 
    greater than or equal to S.
    Return 0 if no such subarray exists.
    '''
    window_sum = 0
    min_length = math.inf
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length

def longest_substring_with_k_distinct(k, str1):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in 
    # the char_frequency
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length

def longest_substring_k_distinct1(k, arr):
    window_sum, window_start = 0, 0
    max_length = math.inf
    max_elem = 0
    counts = dict()
    for window_end in range(len(arr)):
        counts[arr[window_end]] = counts.get(arr[window_end], 0) + 1
        for item in counts:
            if counts[item] >= k:
                max_length = (max_length, window_end - window_start + 1)
                window_start
        print('test')
        
    print("here")
        



def main():
     print("Maximum sum of a subarray of size K: " + 
           str(max_sub_array_size_k(3, [2, 1, 5, 1, 3, 2])))
     
def main1():
  print("Smallest subarray length: " 
     + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  
def main2():
  print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct(2, "araaci")))
     
if __name__ == '__main__':
    main2()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    dat = np.array(matrix)
    print("here")