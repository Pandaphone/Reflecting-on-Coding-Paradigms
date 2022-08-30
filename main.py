#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flat_sort(unFlat_array):
  array = []
  for x in unFlat_array:
    for y in x:
      array.append(y)
      
  return sorted(array)

some_Array = [[6, 61], [5.3, 53], [5.9, 67], [6.2, 63]]

print(flat_sort(some_Array))
#How does this solution ensure data immutability?
#The solution does not alter the numbers within the array, therefore ensuring immutability.


#Is this solution a pure function? Why or why not?
#Yes. It does not alter anything outside the funtion.


#Is this solution a higher order function? Why or why not?
#It is not, as it does not return a function.


#Would it have been easier to solve this problem using a different programming style?
#No, it'd only be more tedious.


#Why in particular is functional programming a helpful paradigm when solving this problem?
#It allows for the problem to be solved simply and efficiently.