# Recursive function to print all
# possible subsequences for given array
def printSubsequences(arr, index, subset): 
      
    # Print the subsequence when reach
    # the leaf of recursion tree
    if index == len(arr): 
          
        # Condition to avoid printing
        # empty subsequence
        #if len(subarr) != 0:
        print(subset) 
      
    else: 
        # Subsequence without including the element at current index
        printSubsequences(arr, index + 1, subset) 

        # Subsequence including the element
        # at current index
        printSubsequences(arr, index + 1, subset+[arr[index]]) 
    return
          
arr = [1, 2, 3] 
printSubsequences(arr, 0, [])