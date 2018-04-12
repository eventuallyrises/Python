def count_sheeps(arrayOfSheeps):
  # TODO May the force be with you
  #create a variable to store the sheep we find
  numsheep=0
  #iterate through the array looking for sheep
  for x in arrayOfSheeps:
  #if we find a sheep increment our number of sheep variable
      if x == True:
          numsheep+=1
#return those sheep!
  print(numsheep)
  return numsheep


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

count_sheeps(array1)