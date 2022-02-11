def returnReOccuringElement (arr):
  #initialize a empty hash table to hold previopusly checked elements and the indecies
  checkedNumbers = dict()

  #loop through the array
  for i in range(0,len(arr)): # 0(n)
    #temp assignment of current element (arr[i]) to currentElement variable
    currentElement = arr[i] # 0(1)
    #if current element exists in dict (checking to see if currentElement is a key)
    if currentElement in checkedNumbers: #o(1) in Python3 
      #return the current element
      return currentElement #o(1)
    else:
      #add currentElement as a key and the index as its value 
      checkedNumbers[currentElement] = i #o(1)
  # if we loop through entire array and no keys are foudn ,return this statement
  return "Item was not duplicated" #o(1)


print(returnReOccuringElement([1,2,4,6,7,8,6,5,3]))