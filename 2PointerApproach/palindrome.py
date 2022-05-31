def findValSorted(arr, k):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (arr[low] + arr[high])//2
        
        if arr[mid] == k:
            return mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
        
    return False



def isPalindrom(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(isPalindrom('civi'))

arr = [1, 2, 3, 6, 8]
print(findValSorted(arr, 6))


s = 'civic'
#print(s[::] == s[::-1])