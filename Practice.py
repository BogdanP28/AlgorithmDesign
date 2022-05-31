import math
from turtle import left

def ans2(str1, k):
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
    
  print(char_frequency)
  return max_length

def ans2(str1, k):
  window_start = 0
  max_length = 0
  char_frequency = {}
  stringer = ''
  end, begin = 0, 0
  
  aux = []
  
  for window_end in range(len(str1)):
    char_frequency[str1[window_end]] = char_frequency.get(str1[window_end], 0) + 1
    
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
        
      window_start += 1
      
    if end - begin < window_end - window_start:
      begin = window_start
      end = window_end

      
    max_length = max((max_length, window_end-window_start + 1))
    
  print(str1[begin:end+1])
  return max_length

def ans(arr, s):
    window_start = 0
    min_length = math.inf
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end-window_start + 1)
            window_sum = window_sum - arr[window_start]
            window_start += 1
    return min_length
  
def ans3(lister):
  window_start = 0
  max_length = 0
  bascket = {'0': [], '1': []}
  dict = {}
  aux = []
  end, begin = 0, 0
  for window_end in range(len(lister)):
    dict[lister[window_end]] = dict.get(lister[window_end], 0) + 1
    
    while len(dict) > 2:
      left_fruit = lister[window_start]
      dict[left_fruit] -= 1
      if not dict[left_fruit]:
        del dict[left_fruit]
      
      aux.append(lister[window_end - window_start + 1])
      window_start += 1
      if len(set(bascket['0'])) == len(bascket['0']):
        del bascket['0'][0]

    if end - begin < window_end - window_start:
      end, begin = window_end, window_start
      
    max_length = max(max_length, window_end - window_start + 1)
    
    bascket['0'].append(lister[window_end])

    
    
    if len(aux) > 2:
      del aux[0]
      
  print(max_length)
  print(lister[begin:end+1])
    
def ans4():
  lister = 'abccde'
  window_start = 0
  aux = ''
  end, begin = 0, 0
  dict = {}
  for window_end in range(len(lister)):
    dict[lister[window_end]] = dict.get(lister[window_end],0) + 1
    
    while dict.get(lister[window_end],0) > 1:
      left_char = lister[window_start]
      dict[left_char] -= 1
      if not dict[left_char]:
        del dict[left_char]
      window_start += 1
    
    if end - begin < window_end - window_start:
      end, begin = window_end, window_start
      
  print(lister[begin:end+1])
  print("Finished")
    
    
def ans5():
    nums = [23,2,6,4,7]
    k = 13
    
    nums = [1,0,1,0,1]
    k = 4
    #nums.sort()
    ct =0
    
    window_start = 0
    sum = 0
    end, begin = 0, 0
    for window_start in range(len(nums)):
      sum = nums[window_start]
      if sum == 0: ct += 1      
      for window_end in range(window_start + 1, len(nums)):
        sum = sum + nums[window_end]
        if ct == 1:
          if nums[window_end]==0: ct == 2
          
        
        if sum == k or (sum >k  and sum % k == 0) and ct == 2:
          print(True)

        
      #if end-begin > window_end - window_start
    
    print("here")

      

    

            
def main():
     print("Maximum sum of a subarray of size K: " + 
           str(ans([2, 1, 5, 2, 3, 2], 7)))
def main2():
    print(ans2("araaci", 2))
    
def main3():
    ans3(['A', 'B', 'C', 'A', 'C'])

if __name__ == '__main__':
    #main2()
    ans5()