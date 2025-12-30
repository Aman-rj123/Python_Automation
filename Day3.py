# Return the first Duplicate in the list 


def remove_duplciate(list):
    
  seen =set()
  for x in list:
      if x in seen: #Python uses in for direct membership checking, while C++ uses find() or count() to check existence in a container.
          return x   #if (seen.find(x) != seen.end()) In c++
      seen.add(x)
      
  return None

print("The first  Duplicate Number is:",remove_duplciate([1,2,3,8,7,9,9]))
        
    